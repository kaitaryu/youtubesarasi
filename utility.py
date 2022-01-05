
import key
import tweepy
import re
import json
from requests_oauthlib import OAuth1Session
def Get_Api():
    auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
    auth.set_access_token(key.access_token, key.access_token_secret)
    api = tweepy.API(auth)
    return api

def Twwet(test):
    url_media = "https://upload.twitter.com/1.1/media/upload.json"
    url_text = "https://api.twitter.com/1.1/statuses/update.json"

    # OAuth認証 セッションを開始
    twitter = OAuth1Session(key.consumer_key, key.consumer_secret, key.access_token,  key.access_token_secret)
    # Media ID を付加してテキストを投稿
    params = {'status': test}
    req_media = twitter.post(url_text, params = params)

    # 再びレスポンスを確認
    if req_media.status_code != 200:
        print ("テキストアップデート失敗: %s", req_text.text)
        exit()

    print ("OK")
