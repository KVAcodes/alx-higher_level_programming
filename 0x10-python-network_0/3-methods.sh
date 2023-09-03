#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.
curl -X OPTIONS -sL "$1" -i | awk '/Allow: / { sub(/Allow: /, ""); print }'
