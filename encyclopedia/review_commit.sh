#!/bin/sh
# review_commit.sh "message" — validate every committed/modified record, full test build, commit records + review logs.
set -e
cd "$(dirname "$0")"
for f in $(git ls-files records); do python3 check_records.py "$f" > /dev/null || { echo "FAIL $f"; python3 check_records.py "$f"; exit 1; }; done
S=/tmp/claude-0/-home-user-Wedding-2025-/8abde12b-5763-5676-9c3c-adf385173048/scratchpad/build
rm -rf $S && mkdir -p $S/records
cp -r src parts fix_base.py make_catalogue.py add_examples.py build_merged.py reclib.py build_tail.py build_conditions.py apply_micro.py micro_new.py build_all.sh $S/
for r in $(git ls-files records); do cp "$r" $S/records/; done
(cd $S && ./build_all.sh | tail -3)
cp $S/CORRECTIONS.md .
git add $(git ls-files -m records parts micro_new.py) review CORRECTIONS.md fix_base.py review_commit.sh 2>/dev/null || true
git commit -q -m "$1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_011BDMkBxhKtuuvArx9ZY1jK"
git push -q origin claude/new-session-0cayvq 2>&1 | tail -1
git log --oneline -1
