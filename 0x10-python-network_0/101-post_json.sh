#!/bin/bash
# Sends JSON POST request to given URL with given JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
