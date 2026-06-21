# Decisions

| Date | Decision | Context | Consequences | Status |
|---|---|---|---|---|
| 2026-06-21 | Claude Code marketplace install via `claude plugin install byescaleira@marketplace` | Native plugin distribution through Claude Code marketplace | Users can install with two commands; repository stays source of truth | active |
| 2026-06-21 | Skills directory as fallback install path | Marketplace may not be available in older Claude Code versions | Users can install now via `~/.claude/skills/byescaleira/` | active |
| 2026-06-21 | GitHub repo as plugin source over zip | Zip source type not supported by marketplace schema | HTTPS git URL works and auto-clones | active |
| 2026-06-21 | Plugin as set of Claude Code extension files | Native integration, no extra tooling | Limited to Claude Code users | Active |
| 2026-06-21 | English for all plugin documentation | Aligns with professional identity | Consistent with public projects | Active |
| 2026-06-21 | MIT license | Personal/open-source projects | Simple reuse by others | Active |

## Decision details

### 2026-06-21 — Repository name: `byescaleira-plugin`

**Problem:** Need a clear name for the public repository containing the personal OS.
**Options:** `byescaleira-os`, `byescaleira`, `cosmos`, `project-constellation`, `byescaleira-plugin`.
**Decision:** Use `byescaleira-plugin`.
**Reasoning:** It clearly identifies the repository as a Claude Code plugin and keeps the operating system name (`byescaleira`) free for a future website or central hub.
**Consequences:** The repository URL is `github.com/byescaleira/byescaleira-plugin`. It may be confused with an MCP server or IDE plugin, but the README clarifies it is for Claude Code.
**Status:** Active

### 2026-06-21 — Plugin as set of Claude Code extension files

**Problem:** How to implement the personal OS as a usable tool.
**Options:** Hermes skill only, Claude Code CLAUDE.md only, full CLI tool, set of Claude Code extension files.
**Decision:** Start with Claude Code extension files (`CLAUDE.md`, commands, agents).
**Reasoning:** It requires no build step, is native to the tool Rafael uses for coding, and can be versioned in GitHub.
**Consequences:** Users must manually copy files into `~/.claude/`. Later, an install script or MCP server can automate this.
**Status:** Active

### 2026-06-21 — English for all plugin documentation

**Problem:** What language to use for public project documentation.
**Options:** Portuguese (native), English (professional audience).
**Decision:** Use English for all documentation in the plugin and generated projects.
**Reasoning:** Rafael's public identity and portfolio target an international engineering audience.
**Consequences:** Personal notes and some communications can remain in Portuguese, but all READMEs, proposals, and roadmaps are in English.
**Status:** Active

### 2026-06-21 — MIT license

**Problem:** What license to use for personal/open-source repositories.
**Options:** MIT, Apache 2.0, proprietary.
**Decision:** MIT.
**Reasoning:** Simple, permissive, and aligned with personal project defaults.
**Consequences:** Others can freely use and modify the plugin. If a commercial product emerges later, the license can be revisited.
**Status:** Active
