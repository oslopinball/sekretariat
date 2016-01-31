#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs
import os


IdKey = 0
FirstNameKey = 2
LastNameKey = 3
TagKey = 4
AddressKey = 5
PostcodeKey = 6
CityKey = 7
DobKey = 8
CellphoneKey = 11
EmailKey = 12
Paid2016Key = 25

def checkPayment(paidField):
    return not (len(paidField) == 0 or paidField.isspace() or paidField == '-')

def saneField(memberFields, key):
    value = memberFields[key].decode('utf-8')
    if len(value) == 0:
        value = u'—'
    return value

def sendPaymentEmail(memberFields, who):
    pinid = memberFields[IdKey]
    firstName = saneField(memberFields, FirstNameKey)
    lastName = saneField(memberFields, LastNameKey)
    tag = saneField(memberFields, TagKey)
    address = saneField(memberFields, AddressKey)
    postcode = saneField(memberFields, PostcodeKey)
    city = saneField(memberFields, CityKey)
    dob = saneField(memberFields, DobKey)
    cell = saneField(memberFields, CellphoneKey)
    if len(cell) == 0:
        cell = u'—'
    email = memberFields[EmailKey].decode('utf-8')
    year = 2016


    emailText = u"""Subject: Oslo Flipperspillklubb: Årskontengent {2}
From: sekretariat@oslopinball.no
To: {0}
CC: sekretariat@oslopinball.no
Reply-to: sekretariat@oslopinball.no

Hei {1},

nå er det {2}, og det er tide å betale årskontingent for {2}.

Årskontigent {2}
=============
Kontonummer: 1503.57.12779
Kroner: 50,-

NB: Husk å legg ved fullt navn som kommentar.

Din informasjon
===========
Vi har følgene informasjon om deg, si i fra hvis noe ikke stemmer:

Ditt medlemsnummer er {3}.
Fornavn: {1}
Etternavn: {4}
TAG: {5}
Adresse: {6}
Postnummer: {7}
Sted: {8}
Fødelsdato (år-måned-dag): {9}
Mobil: {10}

Mvh,
{11}
på vegne av Oslo Flipperspillklubbs sekretariat
http://www.oslopinball.no/
""".format(email, firstName, year, pinid, lastName, tag, address, postcode, city, dob, cell, who)

    emailBody = codecs.open("emails/{}".format(pinid), 'w', 'utf-8')
    emailBody.write(emailText)
    emailBody.close()

def runEmails(filename, who):

    for line in codecs.open(filename, 'r', 'utf-8').xreadlines():
        if line.startswith("Id"):
            continue
        splitFields = line.split('\t')
        firstName = splitFields[FirstNameKey]
        lastName = splitFields[LastNameKey]
        paid2016 = splitFields[Paid2016Key]

        # A bad member
        if len(firstName) == 0 and len(lastName) == 0:
            continue

        paid2016 = checkPayment(paid2016)

        if paid2016 == True: # No need to process more this person is paid up
            print '{} {} is paid up'.format(firstName, lastName)
            continue
        else:
            print '{} {} MUST PAY'.format(firstName, lastName)
            sendPaymentEmail(splitFields, who)


def main():
    if len(sys.argv) != 2:
        sys.stderr.write(sys.argv[0]+": I need an ID (email file), exiting.\n")
        return

    who = u"Trenton Schulz"
    print "Sending mails as {}".format(who.encode('utf-8'))
    runEmails(sys.argv[1], who)



if __name__ == "__main__":
    main()


