# Changelog

## [Unreleased]

## [0.3.0] — Stratosphere — 2026-06-21

### Added
- Expanded `SKILL.md` with identity, voice, principles, codenames, skeleton, rules, and task instructions.
- Enhanced `@byescaleira` agent with templates and operational guidance.
- Lightweight MCP server `scripts/byescaleira-mcp.py` exposing:
  - `list_codenames`
  - `suggest_codename`
  - `validate_skeleton`
- CI workflow with shellcheck, markdown lint, JSON/YAML validation, frontmatter checks, and skeleton generation test.

## [0.2.0] — Atmosphere — 2026-06-21

### Added
- Claude Code native plugin manifest `.claude-plugin/plugin.json`.
- Marketplace manifest `.claude-plugin/marketplace.json`.
- `SKILL.md` and `agents/byescaleira.md` for native plugin loading.
- GitHub Releases packaging script `scripts/package.sh`.

### Changed
- README now documents marketplace install as the recommended path.

## [0.1.0] — Dust — 2026-06-21

### Added
- Public GitHub repository `byescaleira-plugin`.
- Initial README with installation instructions.
- PROPOSAL.md, ROADMAP.md, ARCHITECTURE.md, DECISIONS.md.
- GitHub issue and PR templates.
- MIT license.
