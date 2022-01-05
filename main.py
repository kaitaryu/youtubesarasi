
import os
import shutil
import pandas as pd
from sqlalchemy import create_engine

import utility
import datetime

def load_chrome():
    path_ = os.path.join(os.getenv("HOMEDRIVE"), os.getenv("HOMEPATH"), "AppData",
                        "Local/Google/Chrome/User Data/Default/History")
    cache="data/history_repl"
    shutil.copy(src=path_, dst=cache)
    # chrome
    query_ = "select title,url,last_visit_time from urls"
    cache="data/history_repl"
    df = pd.read_sql_query(query_,
                        create_engine("sqlite:///{}".format(cache)))
    df = df.dropna(subset=['title'])
    df = df.sort_values(['last_visit_time'], ascending=False)
    return df
def get_youtube_Url(df):
    for data in df.itertuples():
        url = data.url
        if "https://www.youtube.com/watch" in url:
            title = data.title
            print(data)
            print(url.split('&')[0])
            return title,url.split('&')[0]
    return "",""

def main():

    try:
        os.makedirs('./data')
    except FileExistsError:
        pass
    df = load_chrome()
    title,url = get_youtube_Url(df)
    url_list = ""
    if os.path.isfile('data/data.txt'):
        with open('data/data.txt') as f:
            url_list = f.read()

    if url != "" and not(url in url_list):
        # # TwitterAPI認証
        api = utility.Get_Api()
        utility.Twwet("私はyoutube晒しBot。こいつが見ている動画を晒します。\n" + title + "\n"+ url +"\n")
        print("ツイートしました")
        url_list = url_list + "," + url
        with open('data/data.txt','w') as f:
            f.write(url_list)
        
        
if __name__ == '__main__':
    main()