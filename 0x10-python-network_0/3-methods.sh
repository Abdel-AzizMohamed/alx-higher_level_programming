#!/usr/bin/bash
# displays all HTTP methods the server will accept
curl -sX OPTIONS "$1" | grep "Allow" | cut -d " " -f 2-
