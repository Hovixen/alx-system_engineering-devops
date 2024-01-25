#!/bin/bash
# Script takes URL and sends request to URL and displays the size body of response
curl -sI $1 | grep -i content-length | awk '{print $2}' | tr -d '\r'
