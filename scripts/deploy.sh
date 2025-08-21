#!/usr/bin/env bash
set -euo pipefail

VERSION=$(cat VERSION)
echo "Deploying Willful Demo v${VERSION}..."
# simulate deploy
sleep 1
echo "Deployed!"
