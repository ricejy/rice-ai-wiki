# AI Cooker

A personal AI knowledge wiki fully maintained by LLMs. Sources go in, structured wiki pages come out. Obsidian serves as the frontend UI.

Inspired by Karpathy's "second brain" idea — except the brain does its own reading, summarizing, cross-referencing, and organizing.

## Architecture

```
┌─────────────────────┐       ┌────────────────┐       ┌──────────────────┐
│  Telegram Channel   │──────▶│  Bot (local)   │──────▶│  GitHub Repo     │
│  "Impt AI News"     │ poll  │  saves + push  │ git   │  raw/telegram/   │
└─────────────────────┘       └────────────────┘       └────────┬─────────┘
                                                                │
                                                    daily @ midnight SGT
                                                                ▼
┌─────────────────────┐       ┌────────────────────────────────────────────┐
│  Obsidian (local)   │◀──────│  Claude Code Remote Agent (Anthropic cloud)│
│  reads wiki/ pages  │ pull  │  ingests pending → creates wiki pages      │
└─────────────────────┘       └────────────────────────────────────────────┘
```

**Two actors, fully decoupled via git:**

1. **Telegram Bot** — runs on your machine, captures channel messages, commits and pushes raw markdown files to GitHub
2. **Scheduled Claude Agent** — runs daily in Anthropic's cloud, reads pending messages, produces structured wiki pages, pushes back

You interact with the wiki through Obsidian (or any markdown editor). The LLM does all the writing.

## Directory Structure

```
raw/                    # Immutable source documents — never modified after creation
  telegram-export/      # One-time Telegram JSON export (historical backfill)
  telegram/             # Live messages captured by the bot (status: pending → ingested)
  assets/               # Downloaded images from sources

wiki/                   # LLM-maintained wiki — all content here is AI-generated
  sources/              # One summary page per ingested source
  concepts/             # Topic pages (e.g., quantization, agentic-systems, kv-cache)
  entities/             # People, organizations, models, products
  analyses/             # Comparisons, syntheses, deep dives
  index.md              # Catalog of all wiki pages
  log.md                # Chronological record of all operations

scripts/                # Automation
  telegram-bot.py       # Bot that listens to Telegram channel
  requirements.txt      # Python dependencies
  .env.example          # Template for secrets

CLAUDE.md               # Wiki schema, page templates, and operational instructions for the LLM
```

## How Ingestion Works

### Live pipeline (ongoing)

1. You forward/post something to your Telegram channel
2. Bot saves it as `raw/telegram/2026-05-10-143022-article-title.md` with `status: pending`
3. Bot commits and pushes to GitHub
4. At midnight, the scheduled agent wakes up:
   - Reads each pending file
   - Creates a source page in `wiki/sources/`
   - Creates or updates concept pages in `wiki/concepts/`
   - Creates or updates entity pages in `wiki/entities/`
   - Updates `wiki/index.md` and `wiki/log.md`
   - Marks the raw file as `status: ingested`
   - Commits and pushes all wiki changes
5. You `git pull` and see the updated wiki in Obsidian

### Manual ingestion

Drop any article, paper, or notes into `raw/` and ask Claude Code to ingest it. The LLM follows the same workflow — create source page, update concepts/entities, cross-reference with wikilinks.

### Queries

Ask questions against the wiki. Claude reads the index, finds relevant pages, and synthesizes an answer. Substantial answers can be filed as analysis pages for future reference.

## Setup

### Prerequisites

- Python 3.11+
- Git
- A Telegram bot (created via [@BotFather](https://t.me/BotFather))
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (for local ingestion and the scheduled agent)

### 1. Clone and install

```bash
git clone https://github.com/ricejy/ai-cooker.git
cd ai-cooker
pip install -r scripts/requirements.txt
```

### 2. Configure the bot

```bash
cp scripts/.env.example scripts/.env
```

Edit `scripts/.env`:
```
TELEGRAM_BOT_TOKEN=<your token from @BotFather>
TELEGRAM_CHANNEL_ID=<your channel ID in -100xxxxx format>
```

To get the channel ID: add the bot as an admin to your channel, send a message, then check `https://api.telegram.org/bot<TOKEN>/getUpdates`.

### 3. Run the bot

```bash
python scripts/telegram-bot.py
```

The bot runs in the foreground. For persistent background operation on Windows, use Task Scheduler:

```powershell
$action = New-ScheduledTaskAction -Execute "pythonw.exe" `
  -Argument "C:\path\to\scripts\telegram-bot.py" `
  -WorkingDirectory "C:\path\to\scripts"
$trigger = New-ScheduledTaskTrigger -AtLogOn
Register-ScheduledTask -TaskName "TelegramBot" -Action $action -Trigger $trigger
```

### 4. Set up the scheduled agent (optional)

The daily ingestion agent runs via [Claude Code Routines](https://docs.anthropic.com/en/docs/claude-code). Configure a routine that:
- Clones this repo
- Checks `raw/telegram/` for files with `status: pending`
- Runs the ingest workflow defined in `CLAUDE.md`
- Commits and pushes wiki updates

## Wiki Schema

Every wiki page follows a consistent template with YAML frontmatter:

```markdown
---
title: Page Title
type: source | concept | entity | analysis
created: 2026-05-10
updated: 2026-05-10
tags: [tag1, tag2]
sources: [source-filename, ...]
---

# Page Title

Content with [[wikilinks]] for cross-references.

## See also
- [[Related Page]]
```

Pages are interlinked with `[[wikilinks]]` that Obsidian resolves automatically. The full schema, naming conventions, and operational rules are in [CLAUDE.md](CLAUDE.md).

## Tech Stack

- **LLM**: Claude (Sonnet 4.6 for scheduled ingestion, Opus 4.6 for interactive sessions)
- **Orchestration**: [Claude Code](https://docs.anthropic.com/en/docs/claude-code) + Claude Code Routines
- **Bot**: [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) v21+
- **Frontend**: [Obsidian](https://obsidian.md) (reads the `wiki/` directory as a vault)
- **Storage/sync**: Git + GitHub

## License

Personal project. Feel free to fork the structure for your own knowledge wiki.
