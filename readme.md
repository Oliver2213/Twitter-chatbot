#Simple Twitter Chat bot

This is a small, simple chatter bot using [The awesome twitter library Tweepy](https://github.com/tweepy/tweepy) and [this simple yet fun chatter bot](https://github.com/gunthercox/ChatterBot)  
##Setup
To get twitter-chatbot up and talking, do the following:  
* Install tweepy, iether with [pip](http://pip.readthedocs.org/en/latest/installing.html#install-pip), or it's [git hub page](https://github.com/tweepy/tweepy])
* Install chatterbot, iether with [pip](http://pip.readthedocs.org/en/latest/installing.html#install-pip), or it's [git hub page](https://github.com/gunthercox/ChatterBot)
* Get a twitter app from [apps.twitter.com](https://apps.twitter.com), and optionally get a different account to use it with
* Modify the apps permission level to "Read and write", so it can send direct messages (This is what the bot is set up to do now, though of course you can change it)
* Put you're app's API keys in a file called keys.py like:
  * c_key = 'Consumer key here'
  * c_secret = 'Consumer secret here'
* You can also optionally put tokens in (if you had twitter generate them), as:
  * token = 'Token here'
  * token_secret = 'Token secret here'
* If everything worked, you should be able to run the bot like: 
  * python chatbot.py
* Now just send what ever account you set it up on a DM and the bot will begin learning and responding!  

Note that this is a really simple bot, suggestions for more complex / smarter ones are welcome!
