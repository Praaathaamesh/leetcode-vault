#!/bin/bash
# Read from the file file.txt and output all valid phone numbers to stdout.

# use std/exact regex grep

grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt