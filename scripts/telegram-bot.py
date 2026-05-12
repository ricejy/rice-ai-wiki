"""
Telegram Bot — listens to "Impt AI News" channel and saves messages to raw/telegram/.
Run with: python scripts/telegram-bot.py
"""

import os
import json
import logging
import subprocess
import time
from pathlib import Path

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

load_dotenv()

# Bot token and channel ID are set in the .env file. Was created by @BotFather on telegram itself.
BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHANNEL_ID = int(os.environ.get("TELEGRAM_CHANNEL_ID", "0"))
ADMIN_CHAT_ID = int(os.environ.get("TELEGRAM_ADMIN_CHAT_ID", "0"))

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "raw" / "telegram"
ASSETS_DIR = RAW_DIR / "assets"

RAW_DIR.mkdir(parents=True, exist_ok=True)
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

# Logger for when the bot is running and when it encounters errors.
logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Cleans up messages to make them safe to use as filenames.
def sanitize_filename(text: str, max_len: int = 50) -> str:
    safe = "".join(c if c.isalnum() or c in " -_" else "" for c in text)
    return safe.strip().replace(" ", "-")[:max_len].lower().rstrip("-")

# Extract text from tele messages which can come in diff forms like captions of immages or docs/plain text.
def extract_text(message) -> str:
    """Extract full text from a telegram message."""
    parts = []
    if message.text:
        parts.append(message.text)
    if message.caption:
        parts.append(message.caption)
    return "\n".join(parts)

# cleans up and extracts urls from the message entities.
def extract_urls(message) -> list[str]:
    """Extract URLs from message entities."""
    urls = []
    entities = message.entities or message.caption_entities or []
    text = message.text or message.caption or ""
    for entity in entities:
        if entity.type == "url":
            urls.append(text[entity.offset : entity.offset + entity.length])
        elif entity.type == "text_link":
            urls.append(entity.url)
    return urls

_push_failed = False

def git_commit_and_push(filepath: Path, filename: str, bot=None) -> None:
    cwd = str(PROJECT_ROOT)
    global _push_failed

    try:
        subprocess.run(["git", "add", "raw/telegram/"], cwd=cwd, check=True, capture_output=True)
        subprocess.run(
            ["git", "commit", "-m", f"telegram: {filename}"],
            cwd=cwd, check=True, capture_output=True,
        )
    except subprocess.CalledProcessError as e:
        logger.error(f"Git commit failed: {e.stderr.decode() if e.stderr else e}")
        return

    last_err = None
    for attempt in range(3):
        try:
            subprocess.run(
                ["git", "pull", "--rebase", "origin", "main"],
                cwd=cwd, check=True, capture_output=True,
            )
            subprocess.run(["git", "push"], cwd=cwd, check=True, capture_output=True)
            logger.info(f"Pushed: {filename}")
            if _push_failed:
                _push_failed = False
                _notify_admin(bot, f"Git push recovered. Backlog cleared.")
            return
        except subprocess.CalledProcessError as e:
            last_err = e.stderr.decode() if e.stderr else str(e)
            logger.warning(f"Push attempt {attempt + 1}/3 failed: {last_err}")
            if attempt < 2:
                time.sleep(2 ** attempt)

    _push_failed = True
    logger.error(f"Git push failed after 3 attempts: {last_err}")
    _notify_admin(bot, f"Git push failed after 3 retries.\n\n{last_err}")


def _notify_admin(bot, text: str) -> None:
    if not bot or not ADMIN_CHAT_ID:
        return
    import asyncio
    try:
        loop = asyncio.get_running_loop()
        loop.create_task(bot.send_message(chat_id=ADMIN_CHAT_ID, text=f"[ai-cooker bot] {text}"))
    except RuntimeError:
        asyncio.run(bot.send_message(chat_id=ADMIN_CHAT_ID, text=f"[ai-cooker bot] {text}"))

# core of this script. Handles incoming messages from the channel and saves them to the raw/telegram/ directory.
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.channel_post or update.message
    if not message:
        return
    # If the message is not from the channel, return.
    if CHANNEL_ID and message.chat_id != CHANNEL_ID:
        return

    # Get the date, time, and message ID.
    msg_date = message.date.strftime("%Y-%m-%d")
    msg_time = message.date.strftime("%H%M%S")
    msg_id = message.message_id
    # Extract the text from the message.
    text = extract_text(message)
    # Extract the URLs from the message.
    urls = extract_urls(message)

    # Sanitize the filename.
    slug = sanitize_filename(text[:60]) if text else f"msg-{msg_id}"
    # Create the filename.
    filename = f"{msg_date}-{msg_time}-{slug}.md"
    filepath = RAW_DIR / filename

    # If the file already exists, log it and return.
    if filepath.exists():
        logger.info(f"Already saved: {filename}")
        return

    # If the message has media, download it and save it to the assets/ directory.
    media_paths = []

    if message.photo:
        # Download the highest resolution photo.
        photo = message.photo[-1]  # highest resolution
        file = await context.bot.get_file(photo.file_id)
        ext = "jpg"
        asset_name = f"{msg_date}-{msg_time}-photo-{msg_id}.{ext}"
        asset_path = ASSETS_DIR / asset_name
        await file.download_to_drive(str(asset_path))
        media_paths.append(f"assets/{asset_name}")
        logger.info(f"Downloaded photo: {asset_name}")

    if message.document:
        doc = message.document
        file = await context.bot.get_file(doc.file_id)
        ext = Path(doc.file_name).suffix if doc.file_name else ""
        asset_name = f"{msg_date}-{msg_time}-{doc.file_name or f'file-{msg_id}{ext}'}"
        asset_path = ASSETS_DIR / asset_name
        await file.download_to_drive(str(asset_path))
        media_paths.append(f"assets/{asset_name}")
        logger.info(f"Downloaded document: {asset_name}")

    # Build markdown content
    lines = []
    lines.append("---")
    lines.append(f"date: {msg_date}")
    lines.append(f"time: {message.date.strftime('%H:%M:%S')}")
    lines.append(f"message_id: {msg_id}")
    if urls:
        lines.append(f"urls: {json.dumps(urls)}")
    if media_paths:
        lines.append(f"media: {json.dumps(media_paths)}")
    lines.append("status: pending")
    lines.append("---")
    lines.append("")

    if text:
        lines.append(text)
        lines.append("")

    if media_paths:
        lines.append("## Attachments")
        for p in media_paths:
            lines.append(f"- [{Path(p).name}]({p})")
        lines.append("")

    filepath.write_text("\n".join(lines), encoding="utf-8")
    logger.info(f"Saved: {filename}")

    git_commit_and_push(filepath, filename, bot=context.bot)


if __name__ == "__main__":
    # Create the application and add the handler for the channel messages, these make use of telegrams api.
    app = Application.builder().token(BOT_TOKEN).build()

    # Add the handler for the channel messages.
    app.add_handler(MessageHandler(
        filters.Chat(chat_id=CHANNEL_ID) if CHANNEL_ID else filters.ALL,
        handle_message,
    ))

    # Start the bot.
    logger.info("Bot started. Listening for channel messages...")
    app.run_polling()
