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
│   ├── CLAUDE.md              # Global memory and rules
│   ├── commands/              # Slash commands
│   │   ├── byescaleira-init.md
│   │   ├── byescaleira-proposal.md
│   │   ├── byescaleira-roadmap.md
│   │   └── byescaleira-ship.md
│   ├── agents/                # Specialist agents
│   │   └── byescaleira.md
│   └── settings.json          # Hooks and permissions (future)
├── .github/                   # Repository governance
│   ├── workflows/
│   │   └── ci.yml
│   ├── pull_request_template.md
│   └── issue_templates/
│       ├── bug_report.md
│       └── feature_request.md
├── README.md
├── PROPOSAL.md
├── ROADMAP.md
├── CHANGELOG.md
├── ARCHITECTURE.md
├── DECISIONS.md
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
2. User copies `.claude/` contents into their own `~/.claude/` directory.
3. Claude Code loads `CLAUDE.md`, commands, and agents on next startup.

## Future Evolution

- Split `CLAUDE.md` into `.claude/rules/` when it grows beyond ~200 lines.
- Add `settings.json` for hooks and default permissions.
- Consider an MCP server for advanced scaffolding.
