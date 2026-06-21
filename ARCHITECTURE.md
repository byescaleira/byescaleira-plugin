# Architecture: byescaleira plugin

## Overview

The byescaleira plugin is now packaged as a Claude Code native plugin. It exposes:

- `SKILL.md` — loaded as a skill inside Claude Code sessions.
- `agents/byescaleira.md` — specialist agent invoked with `@byescaleira`.
- `.claude-plugin/plugin.json` — manifest declaring the plugin components.
- Legacy `.claude/` files for users who prefer the older extension format.

It is intentionally lightweight: no compiled code, no external runtime dependencies beyond Claude Code itself. The goal is portability and easy installation.

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
├── .claude-plugin/
│   └── plugin.json            # Claude Code native plugin manifest
├── SKILL.md                   # Skill loaded by Claude Code
├── agents/
│   └── byescaleira.md         # Specialist agent
├── hooks/
│   └── hooks.json             # Hook definitions
├── scripts/
│   ├── install.sh             # Legacy local installer
│   └── welcome.sh             # Silent SessionStart hook handler
├── .claude/                   # Legacy extension files
│   ├── CLAUDE.md              # Global memory entry point
│   ├── commands/              # Slash commands
│   ├── agents/                # Specialist agents (duplicate for legacy)
│   ├── rules/                 # Modular operating system rules
│   └── settings.json          # Hooks and permissions (legacy)
├── .github/                   # Repository governance
│   ├── workflows/
│   │   ├── ci.yml
│   │   └── release.yml
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

1. User installs the plugin via Claude Code:
   ```bash
   claude plugin install byescaleira
   ```
   or directly from the repository:
   ```bash
   claude plugin install git@github.com:byescaleira/byescaleira-plugin.git
   ```
2. Claude Code places the plugin in `~/.claude/skills/byescaleira/`.
3. On the next session, the skill, agent, and hooks are loaded automatically.

A legacy install path is still available via `scripts/install.sh` for users who prefer the older `~/.claude/` extension format.

## Current state

- `SKILL.md` is the primary entry point for the native plugin.
- `agents/byescaleira.md` provides a specialist agent.
- `.claude-plugin/plugin.json` declares the plugin manifest.
- Legacy `.claude/` files remain for backward compatibility.
- `DESIGN.md` contains the visual and brand definitions.

## Future Evolution

- [ ] Test Claude Code native plugin install via marketplace zip
- [ ] Document marketplace install flow in README
- [ ] Update ARCHITECTURE.md with packaging details
- [ ] Create release v0.2.1 with marketplace.json pointing to zip
