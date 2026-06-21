#!/usr/bin/env bash
set -euo pipefail

# Package byescaleira plugin into a .zip for Claude Code marketplace releases.

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VERSION="${1:-}"

if [ -z "$VERSION" ]; then
  echo "Usage: $0 <version>"
  echo "Example: $0 v0.2.0"
  exit 1
fi

OUT_DIR="${REPO_ROOT}/dist"
OUT_FILE="${OUT_DIR}/byescaleira-plugin-${VERSION}.zip"

mkdir -p "${OUT_DIR}"
rm -f "${OUT_FILE}"

cd "${REPO_ROOT}"

zip -r "${OUT_FILE}" \
  .claude-plugin/ \
  SKILL.md \
  agents/ \
  hooks/ \
  scripts/ \
  .claude/ \
  README.md \
  PROPOSAL.md \
  ROADMAP.md \
  CHANGELOG.md \
  ARCHITECTURE.md \
  DECISIONS.md \
  DESIGN.md \
  LICENSE \
  .gitignore \
  -x "*.DS_Store" \
  -x "dist/*"

echo "Packaged ${OUT_FILE}"
