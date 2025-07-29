#!/bin/bash

SESSION_ID="s-$(date +'%Y%m%d-%H%M%S')"

git config user.name "create-session-action[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git config pull.rebase false
git fetch --all
git checkout main
git pull origin main

echo $SESSION_ID >| .sims/session.lock

git add .sims/session.lock
git commit -m "New session $SESSION_ID"
git push origin main

echo $SESSION_ID