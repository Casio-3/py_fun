awk -F '[=,]' '/flag.*?377/ {printf "%c", $5}' access.log | base64 -d
