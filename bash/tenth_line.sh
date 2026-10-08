#!/bin/bash
# Read from the file file.txt and output the tenth line to stdout.
tail -n +10 file.txt | head -n 1

# awk 'NR == 10' file.txt
# sed -n 10p file.txt