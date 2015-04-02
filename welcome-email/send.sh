#!/bin/bash
ID=$1

echo "Sending email to: $ID"
mail -a informasjon.pdf -a vedtekter.pdf -t < emails/$ID.txt
