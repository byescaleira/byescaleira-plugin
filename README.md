# byescaleira plugin

A personal operating system plugin for Claude Code.

It helps Rafael Escaleira (`byescaleira`) start, organize, build, and ship personal projects using a lightweight set of rules: space-themed codenames, a universal repository skeleton, branding definitions, and engineering rituals.

## What this plugin does

- Loads a global `CLAUDE.md` with Rafael's identity, voice, principles, codenames, and processes.
- Adds slash commands for common project operations.
- Provides a `@byescaleira` agent specialized in the operating system.
- Keeps projects consistent, documented, and shippable.

## How to install

### Option 1: Claude Code skills directory (recommended today)

This is the way Claude Code currently loads user-defined skills. It works on Claude Code 2.1.181 and does not depend on an unreleased marketplace feature.

```bash
git clone git@github.com:byescaleira/byescaleira-plugin.git ~/.claude/skills/byescaleira
```

Claude Code loads skills from `~/.claude/skills/<name>/SKILL.md` automatically on startup. The `byescaleira` skill will be available in every session.

### Option 2: local path install (when supported by your Claude Code version)

```bash
claude plugin install ./byescaleira-plugin
```

### Option 3: legacy manual install

```bash
./byescaleira-plugin/scripts/install.sh
```

This copies `.claude/` files into `~/.claude/`. Use this if you prefer the older extension format.

### Option 4: Claude Code marketplace (future)

The plugin is packaged as a Claude Code native plugin and includes a `.claude-plugin/marketplace.json`. When Anthropic opens plugin marketplaces for external sources, the intended install will be:

```bash
claude plugin marketplace add byescaleira/byescaleira-plugin
claude plugin install byescaleira@byescaleira-marketplace
```

As of Claude Code 2.1.181 this path returns `source type not supported`, so the skills directory method is the recommended working option today.

After installing, restart Claude Code or run `/reload-plugins`.

## What gets installed

When installed as a Claude Code native plugin:

```
~/.claude/skills/byescaleira/
├── .claude-plugin/
│   └── plugin.json
├── SKILL.md
└── agents/
    └── byescaleira.md
```

When installed via the legacy script:

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
├── .claude-plugin/       # Claude Code native plugin manifest
│   └── plugin.json
├── SKILL.md              # Skill loaded by Claude Code
├── agents/               # Specialist agents
│   └── byescaleira.md
├── hooks/                # Claude Code hooks
│   └── hooks.json
├── scripts/              # Helper scripts
│   ├── install.sh        # Legacy local installer
│   └── welcome.sh        # Silent SessionStart hook
├── .claude/              # Legacy extension files
│   ├── CLAUDE.md
│   ├── commands/
│   ├── agents/
│   ├── rules/
│   └── settings.json
├── .github/              # GitHub templates and workflows
├── README.md
├── PROPOSAL.md
├── ROADMAP.md
├── CHANGELOG.md
├── ARCHITECTURE.md
├── DECISIONS.md
├── DESIGN.md
├── LICENSE
└── .gitignore
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
