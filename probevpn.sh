#!/bin/bash

while IFS= read -r line; do
    if [ "$line" -eq 0 ]; then
        echo '{"text":"󰦞"}'
    elif [ "$line" -eq 1 ]; then
        echo '{"text":"󰕥"}'
    fi
done < "/home/ates-isf/Scripts/.vpnstatus.txt"

