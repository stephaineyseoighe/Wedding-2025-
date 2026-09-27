#!/bin/sh
# accept.sh records/<file>.py "commit message" — validate, test-build with all committed records, commit and push.
set -e
cd "$(dirname "$0")"
f="$1"; msg="$2"
python3 check_records.py "$f"
S=/tmp/claude-0/-home-user-Wedding-2025-/8abde12b-5763-5676-9c3c-adf385173048/scratchpad/build
rm -rf $S && mkdir -p $S/records
cp -r src parts fix_base.py make_catalogue.py add_examples.py reclib.py build_tail.py build_conditions.py apply_micro.py micro_new.py build_all.sh $S/
for r in $(git ls-files records) "$f"; do cp "$r" $S/records/; done
(cd $S && ./build_all.sh | tail -2)
git add "$f" && git commit -q -m "$msg

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_011BDMkBxhKtuuvArx9ZY1jK"
git push -q origin claude/new-session-0cayvq 2>&1 | tail -1
git log --oneline -1
