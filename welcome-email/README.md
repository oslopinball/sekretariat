# Welcome e-mail documentation #

This is a some quickly scrambled notes for how to send out welcome emails from
a Mac using Mutt and msmtp. If you want to do something similar on Linux see
the smtp.txt file (or take the plunge and actually put the thing here)

## Software you will need ##

Assuming you already have a Mac and an Internet connection, you only need a little bit more to get things going.

* Mutt installed and configured (out of the scope of this document for the moment)
* msmtp set up and configured to send mails via Google Mail (also outside the scope at the moment)

## Basic steps ##

These are the broad strokes for sending out the email

1. Set up the data for the new members.
2. Export a copy of the members.
3. Run the scripts.
4. Update the final member list.

Let's look at these in bits

### Set up the data for the new members ###

1. The member register is on Google drive and called "Ny Medlemsliste" and look at the "Innmelding" tab; this is the raw data we get from the Google web form.
2. Look at new items in this tab and make sure the information makes sense. Clean out the bad lines that make no sense.
3. Copy the new lines over to the "Medlemmer" tab and make sure the right information is in the right columns.
4. Go back to "Innmelding" tab and mark the moved lines as green (so we know they've been taken care of).

### Export a copy of the members ###

1. In the "Medlemmer" tab, choose File * Download As * Tab-separated values.
2. Open up this downloaded file and remove the members that already have received a message.
3. Save the file.

### Run the scripts ###

1. Run the welcome-email.sh script as follows:

    ./welcome-email.sh /path/to/tab-delimited-file.tsv

This will create a bunch of the messages as text files in the emails directory. They are named after each row in the other file. 

2. Inspect the messages and make sure the information is correct.

3. Run the send-mutt.py script to send each message:

    ./send-mutt.py X

Where X is the number of the text file in the email directory.

### Update thi final member list ###

1. Mark each new member that received an email as complete.
