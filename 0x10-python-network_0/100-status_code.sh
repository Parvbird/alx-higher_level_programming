#!/bin/bash
# sends request to URL passed as argument, and displays only status code of response. (no pipe)
awk 'NR==1{printf "%s", $2}' test7 $(curl -sI "$1" -o test7)
