from twython import Twython
from settings import *

tw = Twython(APP_KEY, APP_SECRET)
auth = tw.get_authentication_tokens()

OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

print("Please authorize bot on "+auth['auth_url'])
OAUTH_PIN = input("PIN code : ")

tw = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
auth = tw.get_authentication_tokens(OAUTH_PIN)

OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

with open("creadentials.txt","w") as creds:
	creds.write(OAUTH_TOKEN+"\n"+OAUTH_TOKEN_SECRET)

tw.update_status(status="Hello, world !")
print("Méfais accomplis...")