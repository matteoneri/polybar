#!/bin/sh
echo Next events in gcal:
/usr/bin/gcalcli --calendar "Matteo Neri @FNA" --calendar "nremtt@gmail.com" --calendar "matteo.neri920114@gmail.com" agenda "12am" "11pm" --nostarted --tsv |
    awk '{print " " $2"-"$4, $5, $6, $7, $8}' |
    while read -r line; do
        sleep 0.02
        echo "$line"
        sleep 2
    done

/usr/bin/gcalcli --calendar "Matteo Neri @FNA" --calendar "nremtt@gmail.com" --calendar "matteo.neri920114@gmail.com" agenda "12am" "11pm" --nostarted --tsv |
    head -1 |
    awk '{print " " $2"-"$4, $5, $6, $7, $8}'
