import praw
import random
import urllib.request
from PIL import Image
import time
import send_meme
import config


def get_data():
    reddit = praw.Reddit(client_id=config.CLIENT_ID, client_secret=config.PRAW_SECRET, password=config.PRAW_PASSWORD,
                         user_agent=config.PRAW_AGENT, username=config.PRAW_USERNAME)
    memes = reddit.subreddit(config.SUBREDDIT)
    try:
        with open('data/posted_memes.txt', 'r') as f:
            posted_memes = set(f.read().splitlines())
    except FileNotFoundError: posted_memes = set()
    with open('data/captions.txt', 'r', encoding='utf-8') as file: captions = file.readlines()
    with open('data/last_captions.txt', 'r', encoding='utf-8') as file: last_captions = file.readlines()
    return memes, posted_memes, captions, last_captions


def get_image(_memes, posted_memes, captions, l_caps):
    if config.SUBREDDIT_SORT == 'NEW': memes = [meme for meme in _memes.new(limit=15) if meme.id not in posted_memes]
    else: memes = [meme for meme in _memes.hot(limit=15) if meme.id not in posted_memes]

    if not memes:
        print('No memes found...')
        return False

    try:
        meme = next((meme for meme in memes if 'redd' in meme.url and not meme.is_self))
    except StopIteration:
        print('No valid meme found')
        return False
    # Maybe use not is_video as well
    try:
        urllib.request.urlretrieve(meme.url, 'data/meme.jpg')
        media_path = 'data/meme.jpg'
    except:
        urllib.request.urlretrieve(meme.url, 'data/meme.mp4')
        media_path = 'data/meme.mp4'
        return False

    if media_path == 'data/meme.jpg':
        img = Image.open('data/meme.jpg').convert('RGB')
        img.resize(config.Size, Image.ANTIALIAS)
        img.save('data/meme.jpg')

    if config.auto_caption: caption = get_caption(captions, l_caps)
    else: caption = f'"{meme.title}" - u/{meme.author}'

    posted_memes.add(meme.id)
    with open('data/posted_memes.txt', 'w') as file:
        file.writelines([meme_id + '\n' for meme_id in posted_memes])
    return send_meme.Upload(caption, media_path)


def get_caption(captions, last_captions):
    for caption in captions:
        if not caption in last_captions:
            with open('data/last_captions.txt', 'r', encoding='utf-8') as file:
                lasts = file.readlines()

            lasts[0] = lasts[1]
            lasts[1] = str(caption)

            with open('data/last_captions.txt', 'w', encoding='utf-8') as file:
                file.writelines(lasts)
            return caption

if __name__ == '__main__': get_image(*get_data())
