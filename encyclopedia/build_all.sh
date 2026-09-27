#!/bin/sh
# Full rebuild from the pristine base: micro-skills, Reference Parts G–J, Conditions sheet.
set -e
cd "$(dirname "$0")"
cp src/base.xlsx The_Encyclopedia.xlsx
python3 fix_base.py
python3 make_catalogue.py
python3 apply_micro.py
python3 build_tail.py
python3 build_conditions.py
python3 add_examples.py
python3 build_merged.py
