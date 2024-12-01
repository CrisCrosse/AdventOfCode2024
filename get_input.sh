#!/bin/bash

echo "Getting input for advent of code day $1"
curl -s https://adventofcode.com/2024/day/$1/input --cookie "session=$AOC_SESSION" > input.txt