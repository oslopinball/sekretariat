#!/usr/bin/env python
# -*- coding: utf-8 -*-

# for those that want to send stuff on their Mac. You need to have mutt set up and configured actually.

import sys
import codecs
import subprocess
import os

def main():
    if len(sys.argv) != 2:
        print "I need an ID (email file), exiting."
        return

    sekretariatAddress = "sekretariat@oslopinball.no"
    os.environ['REPLYTO'] = sekretariatAddress
    emailText = codecs.open("emails/" + sys.argv[1] + ".txt", 'r', 'utf-8').readlines()
    header = emailText[:6]
    subject = header[0][9:].strip()
    to = header[2][3:].strip()
    
    body = emailText[6:]
    muttBody = codecs.open("emails/tmp.txt", 'w', 'utf-8')
    muttBody.write("".join(body))
    muttBody.close()
    command = "mutt -c '%s' -s '%s' -a Informasjon.pdf vedtekter.pdf -- %s < emails/tmp.txt" % (sekretariatAddress, subject, to)
#    print command
    os.system(command)

main()

#ID=$1
#
#echo "Sending email to: $ID"
#RECIPIENT=`cat emails/$ID.txt | grep "^To:" | awk '{ print $2 }'`
#SUBJECT=`cat emails/$ID.txt` | grep "^Subject:" | awk '{ print $2 " " $3 " " $4 " " $5 }'
#TOTALLINES=`wc -l emails/$ID.txt | awk '{ print $1 }'`
#BODYLINES=`expr $TOTALLINES - 6`
#BODY=`tail -$BODYLINES emails/$ID.txt`
#echo $BODY | mutt -s "$SUBJECT" -a informasjon.pdf vedtekter.pdf -- $RECIPIENT
