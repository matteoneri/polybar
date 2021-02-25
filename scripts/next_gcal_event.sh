#!/bin/bash

/home/matteo/miniforge3/bin/gcalcli --calendar "Matteo Neri @FNA" --calendar "nremtt@gmail.com" --calendar "matteo.neri920114@gmail.com" agenda "12am" "11pm" --nostarted --tsv | head -1 | awk '{print " " $2"-"$4, $5, $6, $7, $8}'
