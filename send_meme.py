import ssl
from instapy_cli import client
from pushbullet import Pushbullet
import config


def Upload(caption, media_path='Data/meme.jpg', media_type='Photo'):
    pb = Pushbullet(config.PUSHBULLET_API_KEY)
    phones = [device for device in pb.devices if device.icon == 'phone']
    with open(media_path, 'rb') as pic: file_data = pb.upload_file(pic, 'picture.jpg')
    for phone in phones:
        # e.g. with a url
        # push = pb.push_file(file_url="https://i.imgur.com/IAYZ20i.jpg", file_name="meme.jpg", file_type="image/jpeg")
        phone.push_file(**file_data)
        phone.push_note(f'r/{config.SUBREDDIT}', caption)
    if phones:
        print(f'Sent the meme, with the caption: {caption}')
        return True
    else:
        print('No phones to send meme to')
        return False
    # with client(config.IG_Username, config.IG_Password) as cli:
    #     cli.upload(media_path, _Caption)


if __name__ == '__main__': Upload('This is a test.')