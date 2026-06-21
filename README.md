# byescaleira plugin

A personal operating system plugin for Claude Code.

It helps Rafael Escaleira (`byescaleira`) start, organize, build, and ship personal projects using a lightweight set of rules: space-themed codenames, a universal repository skeleton, branding definitions, and engineering rituals.

## What this plugin does

- Loads a global `CLAUDE.md` with Rafael's identity, voice, principles, codenames, and processes.
- Adds slash commands for common project operations.
- Provides a `@byescaleira` agent specialized in the operating system.
- Keeps projects consistent, documented, and shippable.

## How to install

### Option 1: install script (recommended)

```bash
git clone git@github.com:byescaleira/byescaleira-plugin.git
./byescaleira-plugin/scripts/install.sh
```

The script backs up your existing `~/.claude/` and copies the plugin files in place.

### Option 2: manual copy

```bash
git clone git@github.com:byescaleira/byescaleira-plugin.git ~/.claude/byescaleira-plugin
cp -R ~/.claude/byescaleira-plugin/.claude/* ~/.claude/
```

After installing, restart Claude Code or open a new session.

## What gets installed

```
~/.claude/
├── CLAUDE.md
├── commands/
│   ├── byescaleira-init.md
│   ├── byescaleira-proposal.md
│   ├── byescaleira-roadmap.md
│   └── byescaleira-ship.md
└── agents/
    └── byescaleira.md
```

## Available commands

| Command | Purpose |
|---|---|
| `/byescaleira-init` | Generate the universal repository skeleton in the current directory. |
| `/byescaleira-proposal` | Create a `PROPOSAL.md` for a new project. |
| `/byescaleira-roadmap` | Review or create a `ROADMAP.md`. |
| `/byescaleira-ship` | Prepare a release: version bump, changelog, and tag. |

## Agent

Use `@byescaleira` to invoke a specialist agent that knows the full operating system.

Example:

```
@byescaleira review this project's roadmap and suggest the next 3 priorities.
```

## Repository structure

This repository is also an example of the byescaleira skeleton:

```
byescaleira-plugin/
├── .claude/              # Claude Code plugin files
├── .github/              # GitHub templates and workflows
├── scripts/              # Helper scripts
│   └── install.sh        # Local installation script
├── README.md             # This file
├── PROPOSAL.md           # Why this plugin exists
├── ROADMAP.md            # What comes next
├── CHANGELOG.md          # Release history
├── ARCHITECTURE.md       # How the plugin is structured
├── DECISIONS.md          # Important technical decisions
├── LICENSE               # MIT
└── .gitignore            # Ignored files
```

## Documentation

- [PROPOSAL.md](./PROPOSAL.md) — why this plugin exists
- [ROADMAP.md](./ROADMAP.md) — what is coming next
- [ARCHITECTURE.md](./ARCHITECTURE.md) — how it is structured
- [DECISIONS.md](./DECISIONS.md) — important choices
- [CHANGELOG.md](./CHANGELOG.md) — release history

---

Built by [Rafael Escaleira](https://byescaleira.com) · [@byescaleira](https://x.com/byescaleira)

If something here helped you, let me know. If something is wrong, tell me louder.
