#!/bin/bash
# Bash script that takes in a URL and displays all
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
