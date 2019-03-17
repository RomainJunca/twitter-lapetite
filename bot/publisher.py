from datetime import datetime
from datetime import timedelta
import dateutil
from time import sleep
from word_manager import pick_word
from word_manager import register_published

TIME_BETWEEN_TWEETS = 60

def publish_tweet(tw):
	lastTweets = tw.get_user_timeline()
	lastTweetDate = datetime.strptime(lastTweets[0]["created_at"],"%a %b %d %H:%M:%S +0000 %Y") + timedelta(hours=1)
	timeSinceLastTweet = datetime.today() - lastTweetDate
	delay = int(TIME_BETWEEN_TWEETS - timeSinceLastTweet.total_seconds())
	if delay > 0:
		print("Tweet publication in "+str(delay)+"s")
		sleep(delay)

	word = pick_word()
	tweet = tw.update_status(status="J'aime les "+word.lower())
	register_published(word,tweet["id"])
	print("Tweet published")