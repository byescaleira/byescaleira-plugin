# Repository Skeleton

Every byescaleira project starts with a definitions layer. No source code until this layer is complete and approved via `PROPOSAL.md`.

## Structure

```
<project>/
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

## Optional additions

| File / directory | When to add |
|---|---|
| `scripts/` | When CI needs setup, lint, test, or build scripts |
| `DESIGN.md` | When the project has visual/branding decisions to document |
| `.github/CONTRIBUTING.md` | When external contributors are expected |

## Rules

- `README.md` must include the byescaleira README signature.
- `LICENSE` defaults to MIT with copyright to Rafael Escaleira.
- `CHANGELOG.md` must start with an `[Unreleased]` section.
- `ROADMAP.md` must use the Now / Next / Later / Maybe / Never structure.
- `DECISIONS.md` must use the table format with Date, Decision, Context, Consequences, Status.
