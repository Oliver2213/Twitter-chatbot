#Quick twitter chat bot authorization tester
import os
import sys
import tweepy
import webbrowser
from keys import *
print "Starting authorization check..."
#Value exist error checking
if c_key and not c_secret:
    print "error, Can not authorize your twitter app, no app secret API key (consumer secret) was found."
    print "Please add this value to keys.py like:"
    print 'c_secret = "YOUR KEY HERE"'
elif c_secret and not c_key:
    print "error, Can not authorize your twitter app, no app API key (consumer key) was found."
    print "Please add this value to keys.py like:"
    print 'c_key = "YOUR KEY HERE"'
elif not (c_key and c_secret):
    print "Error, can not authorize you're twitter app, keys.py has no c_key and c_secret values set"
    print "Please enter you're app's API keys from Twitter and run this program again."
    sys.exit()
elif c_key and c_secret:
    print "App API keys exist"

if token and not token_secret:
    print "error, Can not authorize your twitter app, no  user token secret was found in keys.py."
    print "Please add this value to keys.py like:"
    print 'token_secret = "YOUR TOKEN SECRET HERE"'
elif token_secret and not token:
    print "error, Can not authorize your twitter app, no  user token was found in keys.py."
    print "Please add this value to keys.py like:"
    print 'token = "YOUR TOKEN HERE"'
elif not (token and token_secret):
    print "No user spesific tokens exist, retrieving them..."
    auth = tweepy.OAuthHandler(c_key, c_secret)
    authURL = auth.get_authorization_url()
    print "Opening the following URL to get your app authorized:"
    print authURL
    print "Once you have verified you're app with twitter, return here and enter the pin it gives you."
    os.sleep(2)
    webbrowser.open(authURL)
    pin = raw_input('PIN: ').strip()
    tokens = auth.get_access_token(verifier=pin)
    tokenfile= open("keys.py",'a')
    tokenfile.write("token = \""+tokens[0]+'\"\n')
    tokenfile.write("token_secret = \""+tokens[1]+'\"\n')
    tokenfile.close()
    print "The tokens should now be saved in keys.py"
elif token and token_secret:
    print "User spesific tokens exist"
    print "All values necessary for successful twitter app authentication are present in keys.py..."
    print "Nothing for me to do here."
    sys.exit()