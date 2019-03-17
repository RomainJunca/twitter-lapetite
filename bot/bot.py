from authentication import get_authenticated_twitter
from publisher import publish_tweet
import time

tw = get_authenticated_twitter()

while True:
	publish_tweet(tw)