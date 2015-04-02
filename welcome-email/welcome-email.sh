#!/bin/bash

# cat ~/msmtp.log | grep -v EX_OK
# mars 15 19:58:40 host=smtp.gmail.com tls=on auth=on user=ole.k.lien@gmail.com from=ole.k.lien@gmail.com recipients=oyvind@lindahl.no,sekretariat@oslopinball.no mailsize=460025 smtpstatus=250 smtpmsg='250 2.0.0 OK 1426445920 dk5sm1711913lad.41 - gsmtp' exitcode=EX_OK

INPUT="person.txt"

WHO="Ole Kristian Lien"

if [[ `whoami` == "trenton" ]]; then
    WHO="Trenton Schulz"
fi

echo "Sending emails as $WHO"

#for LINE in $(cat person.txt); do
cat $INPUT | while read LINE; do

ID=$(echo "$LINE" | awk '{print $1}')
FIRST=$(echo "$LINE" | awk -F'\t' '{print $3}')
LAST=$(echo "$LINE" | awk -F'\t' '{print $4}')
TAG=$(echo "$LINE" | awk -F'\t' '{print $5}')
ADDRESS=$(echo "$LINE" | awk -F'\t' '{print $6}')
POSTCODE=$(echo "$LINE" | awk -F'\t' '{print $7}')
CITY=$(echo "$LINE" | awk -F'\t' '{print $8}')
DOB=$(echo "$LINE" | awk -F'\t' '{print $9}')
CELLPHONE=$(echo "$LINE" | awk -F'\t' '{print $12}')
EMAIL=$(echo "$LINE" | awk -F'\t' '{print $13}')
PAIDDATE=$(echo "$LINE" | awk -F'\t' '{print $16}') # trim

echo "Writing email to: $ID"

PAID=""

if [[ "$PAIDDATE" != "-" ]]; then
	PAID="
Du har allerede betalt kontigenten den $PAIDDATE, takk! :)
"
fi

cat << EOF > emails/$ID.txt
Subject: Velkommen til Oslo Flipperspillklubb!
From: sekretariat@oslopinball.no
To: $EMAIL
CC: sekretariat@oslopinball.no
Reply-to: sekretariat@oslopinball.no

Hei $FIRST,

vi ønsker deg velkommen som nytt medlem i foreningen Oslo Flipperspillklubb! :)

Ditt medlemsnummer er $ID.

Vedlagt finner du to pdf-dokumenter med informasjon og vedtekter til foreningen.
Hvis det er noe du lurer på, er det bare å svare på denne e-posten.

Årskontigent 2015
=============
Kontonummer: 1503.57.12779
Kroner: 50,-

NB: Husk å legg ved fullt navn som kommentar.
$PAID
Din informasjon
===========
Vi har følgene informasjon om deg, si i fra hvis noe ikke stemmer:

Fornavn: $FIRST
Etternavn: $LAST
TAG: $TAG
Adresse: $ADDRESS
Postnummer: $POSTCODE
Sted: $CITY
Fødelsdato (år-måned-dag): $DOB
Mobil: $CELLPHONE

Mvh,
$WHO,
på vegne av Oslo Flipperspillklubbs sekretariat
http://www.oslopinball.no/
EOF
done
