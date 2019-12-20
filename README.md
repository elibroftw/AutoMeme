# AutoMeme
Originally created by [Daniel Munch](https://github.com/Dmunch04).

It was not working for me, and I did not like the formatting, so I modified it to my liking.

AutoMeme retrieves memes from a subreddit of your choice and ~posts it on Instagram for you~ sends it to your phone so that you can easily post it onto Instagram.

Basic support for `captions.txt`

I suggest you use this along with [Task Scheduler](https://medium.com/@elijahlopezz/python-and-background-tasks-4f70b4a2efd8).

Autoposting does not work at the moment due to Instagram changing its private API.
# Instructions
1. Install [Python 3.6+](https://www.python.org/downloads/)
2. Make sure Python is on PATH
   1. `py` in your Terminal/CMD should work
3. Clone or Download this repo
4. In a terminal opened in the repo dir, do `pip install -r requirements.txt`
5. Create a `.env` file with the information in config.py
   1. `.env` format:
      ```
      REDDIT_CLIENT_ID=VALUE
      REDDIT_SECRET=VALUE
      REDDIT_USERNAME=VALUE
      REDDIT_PW=VALUE
      IG_USERNAME=VALUE
      IG_PW=VALUE
      SUBREDDIT=VALUE
      SUBREDDIT_SORT=HOT
      PUSHBULLET=VALUE
      ```
   2. Create a reddit app from https://www.reddit.com/prefs/apps
      1. Note down your
   3. Make sure [Pushbullet](https://www.pushbullet.com/) is installed on your phone
      1. Create an Access Token for Pushbullet
6. Create `data/hashtags.txt` with contents
      ```
      #sample
      #hashtags
      ```
7. Run `py get_meme.py` in the terminal
