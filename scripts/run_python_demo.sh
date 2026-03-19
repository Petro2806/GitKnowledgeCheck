#!/usr/bin/env bash
set -euo pipefail
python3 -c "from src.python.calc import add, div; print('add', add(2,3)); print('div', div(10,2))"
