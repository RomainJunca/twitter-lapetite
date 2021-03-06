from datetime import datetime
from datetime import timedelta
from time import sleep
from word_manager import pick_word
from word_manager import register_published
from settings import TWEET_INTERVAL

def publish_tweet(tw):
	lastTweets = tw.get_user_timeline()
	lastTweetDate = datetime.strptime(lastTweets[0]["created_at"],"%a %b %d %H:%M:%S +0000 %Y")
	timeSinceLastTweet = datetime.today() - lastTweetDate
	delay = int(TWEET_INTERVAL - timeSinceLastTweet.total_seconds())
	if delay > 0:
		print("Tweet publication in "+str(delay)+"s")
		sleep(delay)

	word = pick_word()
	tweet = tw.update_status(status=word.capitalize()[:-1]+" la petite")
	register_published(word,tweet["id"])
	print("Tweet published")