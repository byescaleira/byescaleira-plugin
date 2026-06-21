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

1. User adds the marketplace and installs the plugin:
   ```bash
   claude plugin marketplace add byescaleira/byescaleira-plugin
   claude plugin install byescaleira@marketplace
   ```
2. Claude Code clones the repository and places the plugin in `~/.claude/plugins/`.
3. On the next session, the skill and agent are loaded automatically.

A skills-directory fallback and legacy install script are also documented for users on older Claude Code versions or those who prefer manual installation.

## Current state

- `SKILL.md` is the primary entry point for the native plugin and the skills directory.
- `agents/byescaleira.md` provides a specialist agent (legacy path).
- `.claude-plugin/plugin.json` declares the native plugin manifest.
- `.claude-plugin/marketplace.json` enables `claude plugin install byescaleira@marketplace`.
- GitHub repo is used as the plugin source via HTTPS git URL.
- Legacy `.claude/` files remain for backward compatibility.
- `DESIGN.md` contains the visual and brand definitions.

## Future Evolution

- Switch recommended install to `claude plugin install byescaleira` once Anthropic supports top-level marketplace lookup.
- Strengthen CI with markdown lint, shellcheck, and frontmatter validation.
