#Quick and dirty twitter chatbot
#Using tweepy and chatterbot from https://github.com/gunthercox/ChatterBot
#Author: Blake Oliver <oliver2213@me.com>

from chatterbot import ChatBot
import tweepy
from keys import * #import our user keys
# do twitter auth stuff
auth = tweepy.OAuthHandler(c_key, c_secret) 
auth.set_access_token(token, token_secret)
api = tweepy.API(auth) # Get our API object

#Set up our chat bot:
chatbot = ChatBot("Terminal", storage_adapter="chatterbot.adapters.storage.JsonDatabaseAdapter", logic_adapter="chatterbot.adapters.logic.ClosestMeaningAdapter", database="database.db", io_adapter="chatterbot.adapters.io.NoOutputAdapter")

class StdOutListener(tweepy.StreamListener):
    """Class that handles tweepy events.
E.g: on_connect, on_disconnect, on_status, on_direct_message, etc."""
    def on_connect( self ):
        print("Connection to twitter established!!")
        self.me = api.me()
        try:
            api.update_status(None, 'Chat bot online!')
        except tweepy.error.TweepError as e:
            print("Error sending bot online tweet.")
            print("Message: %s" %(e))

    def on_disconnect( self, notice ):
        print("Connection to twitter lost!! : ", notice)
        try:
            api.update_status(None, 'Chat bot bot now offline.')
        except tweepy.error.TweepError as e:
            print("Error sending bot offline tweet.")
            print("Message: %s" %(e))


    def on_status( self, status ):
        print(status.user.name+": \""+status.text+"\"")
        return True

    def on_direct_message(self, status):
        print("Direct message received.")
        try:
            if status.direct_message['sender_screen_name'] != self.me.screen_name:
                print(status.direct_message['sender_screen_name']+": \""+status.direct_message['text']+"\"")
                response = chatbot.get_response(status.direct_message['text'])
                print "chat bot response: %s" %(response)
                api.send_direct_message(user_id =status.direct_message['sender_id'], text =response)
            return True
        except BaseException as e:
            print("Failed on_direct_message()", str(e))

    def on_error( self, status ):
        print(status)
        try:
            api.update_status(None, 'Chat bot encountered an error... Now offline.')
        except tweepy.error.TweepError as e:
            print("Error sending bot offline-error tweet.")
            print("Message: %s" %(e))


def main():

    try:
        me = api.me()
        print "Starting userstream for %s ( %s )" %(me.name, me.screen_name)
        stream = tweepy.Stream(auth, StdOutListener())
        stream.userstream()

    except KeyboardInterrupt:
        print("Shutting down the twitter chatbot...")
        api.update_status(None, 'Chat bot bot now offline.')
        print('goodbye!')

if __name__ == '__main__':
    main    ()