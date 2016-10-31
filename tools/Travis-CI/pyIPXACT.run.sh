#! /usr/bin/env bash

# define color escape codes
RED='\e[0;31m'			# Red
GREEN='\e[1;32m'		# Green
YELLOW='\e[1;33m'		# Yellow
MAGENTA='\e[1;35m'		# Magenta
CYAN='\e[1;36m'			# Cyan
NOCOLOR='\e[0m'			# No Color

ROOT=$(pwd)

TRAVIS_DIR=$POCROOT/tools/Travis-CI

echo -e "${MAGENTA}========================================${NOCOLOR}"
echo -e "${MAGENTA}         Running pyIPXACT tests         ${NOCOLOR}"
echo -e "${MAGENTA}========================================${NOCOLOR}"

echo -e "Running all tests..."
python3 $ROOT/Test.py
ret=$?

# Cleanup and exit
exit $ret
