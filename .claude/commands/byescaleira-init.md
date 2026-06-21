# /byescaleira-init

Generate the byescaleira universal repository skeleton in the current directory.

## Steps

1. Confirm or ask for the project codename from the byescaleira space dictionary.
   Main projects: Apollo, Artemis, Voyager, Pioneer, Nova, Orion, Kepler, Hubble, Sputnik, Galileo, Osiris, Titan.
2. If the current directory already contains skeleton files, ask before overwriting.
3. Create the following structure:

```
./
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   └── release.yml
│   ├── pull_request_template.md
│   └── issue_templates/
│       ├── bug_report.md
│       └── feature_request.md
├── .gitignore
├── LICENSE
├── README.md
├── PROPOSAL.md
├── ROADMAP.md
├── CHANGELOG.md
├── ARCHITECTURE.md
└── DECISIONS.md
```

4. Fill each file using the templates below, replacing `<project>` with the chosen codename and `<description>` with a one-line summary.
5. Use English for all generated documentation.
6. Apply the byescaleira voice (direct, personal, no corporate fluff).
7. Add the README signature at the end of README.md.
8. Suggest a commit message: `chore: bootstrap <project> repository skeleton`.
9. Do NOT generate source code yet. Only the definitions layer.

---

## README.md template

```markdown
# <project>

> <description>

## What is <project>?

[2-3 paragraphs explaining the problem and solution.]

## Features

- ✅ Feature one
- ✅ Feature two

## Quick start

```bash
git clone git@github.com:byescaleira/<project>.git
cd <project>
# stack-specific setup
```

## Documentation

- [PROPOSAL.md](./PROPOSAL.md) — why this project exists
- [ROADMAP.md](./ROADMAP.md) — what is coming next
- [ARCHITECTURE.md](./ARCHITECTURE.md) — how it is built
- [DECISIONS.md](./DECISIONS.md) — important technical choices
- [CHANGELOG.md](./CHANGELOG.md) — release history

## Requirements

- [language/framework] [version]
- [dependency] [version]

## License

MIT © Rafael Escaleira

---

Built by [Rafael Escaleira](https://byescaleira.com) · [@byescaleira](https://x.com/byescaleira)

If something here helped you, let me know. If something is wrong, tell me louder.
```

## PROPOSAL.md template

```markdown
# Proposal: <project>

## 1. Problem
[What pain or opportunity?]

## 2. Audience
[Who is this for?]

## 3. Solution
[How does it solve it?]

## 4. Success criteria (90 days)
- [ ] ...

## 5. MVP
[Smallest shippable version.]

## 6. Out of scope
[What is NOT in v1.0?]

## 7. Differentiation
[Why this and not an existing solution?]

## 8. Risks
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| ... | ... | ... | ... |

## 9. Why now?
[Why is this the right time?]

## 10. Open questions
- [ ] ...

## Decision
| Date | Decision | By |
|------|----------|----|
| YYYY-MM-DD | Approved for MVP | Rafael Escaleira |
```

## ROADMAP.md template

```markdown
# Roadmap: <project>

> Last updated: YYYY-MM-DD

## Now (current cycle)
- [ ] ...

## Next (next cycle)
- [ ] ...

## Later
- [ ] ...

## Maybe
- [ ] ...

## Never / deliberately out of scope
- ❌ ... — reason
```

## CHANGELOG.md template

```markdown
# Changelog

## [Unreleased]

## [0.1.0] — Dust — YYYY-MM-DD

### Added
- Initial repository skeleton.
```

## ARCHITECTURE.md template

```markdown
# Architecture: <project>

## Overview
[One paragraph.]

## Goals
1. Simplicity
2. Testability
3. Maintainability
4. Performance
5. Extensibility

## Non-goals
[What it does not try to solve.]

## Stack
| Layer | Technology |
|-------|------------|
| Language | ... |
| Framework | ... |
| Storage | ... |
| Networking | ... |
| Testing | ... |
| CI/CD | GitHub Actions |

## Structure
[Diagram or tree.]

## Conventions
See [DECISIONS.md](./DECISIONS.md).
```

## DECISIONS.md template

```markdown
# Decisions

| Date | Decision | Context | Consequences | Status |
|---|---|---|---|---|
| YYYY-MM-DD | ... | ... | ... | Active |
```

## .github/pull_request_template.md

```markdown
## What
[Short description.]

## Why
[Why this change.]

## How
[Implementation.]

## Testing
- [ ] Unit tests
- [ ] Integration tests
- [ ] Manual testing

## Checklist
- [ ] Code follows conventions
- [ ] CHANGELOG.md updated (if applicable)
- [ ] README.md updated (if applicable)
- [ ] DECISIONS.md updated (if applicable)
- [ ] CI passes
```

## .github/issue_templates/bug_report.md

```markdown
---
name: Bug report
about: Report a bug
---

## Description
[What happened?]

## Steps to reproduce
1. ...

## Expected behavior

## Actual behavior

## Environment

## Logs / screenshots
```

## .github/issue_templates/feature_request.md

```markdown
---
name: Feature request
about: Suggest an idea
---

## Problem
[What problem does this solve?]

## Proposed solution

## Alternatives

## Additional context
```

## .github/workflows/ci.yml

```yaml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: ./scripts/setup.sh || echo "No setup script"
      - run: ./scripts/lint.sh || echo "No lint script"
      - run: ./scripts/test.sh || echo "No test script"
      - run: ./scripts/build.sh || echo "No build script"
```

For iOS/macOS, use `runs-on: macos-latest`.

## .github/workflows/release.yml

```yaml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: ./scripts/setup.sh
      - run: ./scripts/test.sh
      - run: ./scripts/build.sh
```

## .gitignore base

```gitignore
.DS_Store
.idea/
.vscode/
*.swp
*.swo
node_modules/
.build/
vendor/
*.log
logs/
.env
.env.local
.env.*.local
build/
dist/
DerivedData/
*.xcuserdata
```

## LICENSE

MIT. Copyright (c) [year] Rafael Escaleira.
