# Architecture: byescaleira plugin

## Overview

The byescaleira plugin is a set of Claude Code extension files that encode a personal operating system for Rafael Escaleira.

It is intentionally lightweight: no compiled code, no external dependencies, only markdown files and one JSON file. The goal is portability and easy installation.

## Goals

1. **Consistency** — every project follows the same skeleton and conventions.
2. **Actionability** — rules are available at the moment of creation.
3. **Modularity** — easy to extend with new commands or agents later.
4. **Portability** — installable by copying files into `~/.claude/`.

## Non-goals

- Complex build systems.
- Cross-platform support beyond Claude Code.
- Automated enforcement of rules (hooks may be added later).

## Structure

```
byescaleira-plugin/
├── .claude/
│   ├── CLAUDE.md              # Global memory entry point
│   ├── commands/              # Slash commands
│   │   ├── byescaleira-init.md
│   │   ├── byescaleira-proposal.md
│   │   ├── byescaleira-roadmap.md
│   │   └── byescaleira-ship.md
│   ├── agents/                # Specialist agents
│   │   └── byescaleira.md
│   ├── rules/                 # Modular operating system rules
│   │   ├── identity.md
│   │   ├── voice.md
│   │   ├── principles.md
│   │   ├── codenames.md
│   │   ├── skeleton.md
│   │   ├── operating.md
│   │   └── visual.md
│   └── settings.json          # Hooks and permissions
├── .github/                   # Repository governance
│   ├── workflows/
│   │   ├── ci.yml
│   │   └── release.yml
│   ├── pull_request_template.md
│   └── issue_templates/
│       ├── bug_report.md
│       └── feature_request.md
├── scripts/                   # Helper scripts
│   └── install.sh
├── README.md
├── PROPOSAL.md
├── ROADMAP.md
├── CHANGELOG.md
├── ARCHITECTURE.md
├── DECISIONS.md
├── DESIGN.md                  # Visual and brand definitions
├── LICENSE
└── .gitignore
```

## Conventions

- All documentation is in English.
- All codenames are in English and follow the space theme.
- File names are lowercase with hyphens.
- Markdown files are readable by both humans and Claude Code.

## Installation Flow

1. User clones the repository.
2. User runs `scripts/install.sh`, which backs up existing `~/.claude/` and copies the plugin files.
3. Claude Code loads `CLAUDE.md`, rules, commands, agents, and settings on next startup.

## Current state

- `CLAUDE.md` is now an entry point; rules live in `.claude/rules/`.
- `settings.json` configures default permissions and a hook to chmod new shell scripts.
- `DESIGN.md` contains the visual and brand definitions.

## Future Evolution

- Consider an MCP server for advanced scaffolding.
- Strengthen CI with markdown lint, shellcheck, and frontmatter validation.
