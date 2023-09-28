#!/bin/bash
# Send GET request to given URL with header variable.
curl -sH "X-School-User-Id: 98" "${1}"
