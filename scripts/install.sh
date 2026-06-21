#!/usr/bin/env bash
set -euo pipefail

# byescaleira-plugin install script
# Safely installs the plugin into ~/.claude/

PLUGIN_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="${HOME}/.claude"
BACKUP_DIR="${HOME}/.claude.backup.$(date +%Y%m%d%H%M%S)"

echo "Installing byescaleira-plugin into ${TARGET_DIR}..."

# Backup existing ~/.claude if it exists and is not empty
if [ -d "${TARGET_DIR}" ] && [ "$(ls -A "${TARGET_DIR}" 2>/dev/null)" ]; then
  echo "Existing ~/.claude found. Creating backup at ${BACKUP_DIR}..."
  cp -R "${TARGET_DIR}" "${BACKUP_DIR}"
fi

# Ensure target directory exists
mkdir -p "${TARGET_DIR}"

# Copy plugin files
if [ -d "${PLUGIN_DIR}/.claude" ]; then
  cp -R "${PLUGIN_DIR}/.claude"/* "${TARGET_DIR}"
else
  echo "Error: .claude directory not found in plugin source."
  exit 1
fi

echo "byescaleira-plugin installed successfully."
echo "Backup saved at: ${BACKUP_DIR}"
echo "Restart Claude Code or open a new session to load the plugin."
