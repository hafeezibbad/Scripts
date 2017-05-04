import email
import sys

# Download attachment from gmail when google does not allow to 
# download the attachment because of security risk
#
# Note: Use at your own risk.
#
# usage python get_attachments.py original_message.txt
# Choose "show original" from email context menu and 
# choose "download original"to download the email as *.txt file.

if __name__=='__main__':
    if len(sys.argv)<2:
        print "Please enter a file to extract attachments from"
        sys.exit(1)

    msg = email.message_from_file(open(sys.argv[1]))
    for pl in msg.get_payload():
        if pl.get_filename(): # automatically extracts the filename from attachment. 
            open(pl.get_filename(), 'wb').write(pl.get_payload(decode=True)
