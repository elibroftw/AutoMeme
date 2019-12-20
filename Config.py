import os
import environs

environs.Env().read_env()

# praw stuff
CLIENT_ID = os.environ['REDDIT_CLIENT_ID']
PRAW_SECRET = os.environ['REDDIT_SECRET']
PRAW_USERNAME = os.environ['REDDIT_USERNAME']
PRAW_PASSWORD = os.environ['REDDIT_PW']
PRAW_AGENT = 'python3'
SUBREDDIT = os.environ['SUBREDDIT']
SUBREDDIT_SORT = os.environ['SUBREDDIT_SORT']  # one of {HOT, NEW}

PUSHBULLET_API_KEY = os.environ['PUSHBULLET']

# IG_Username = os.environ['IG_USERNAME']
# IG_Password = os.environ['IG_PW']

Size = 1080, 1080 # width x height
Interval = 30  # in seconds
auto_caption = False
