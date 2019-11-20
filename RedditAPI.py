import praw
import pandas as pd
import datetime as dt


#Praw = Python Reddit APi Wrapper

reddit = praw.Reddit(client_id='r0XibIX-xKzIFQ', \
                     client_secret='zXLm-tDUZBinKtWYB4LJ3GYEuVk', \
                     user_agent='RedditAPI', \
                     username='raulb1030', \
                     password='BeerOpener2291!')
#subreddit variables

subreddit = reddit.subreddit('Soccer')

top_subreddit = subreddit.top()

top_subreddit = subreddit.top(limit=500)

for submission in subreddit.top(limit=1):
    print(submission.title, submission.id)

topics_dict = { "title":[], \
                "score":[], \
                "id":[], "url":[], \
                "comms_num": [], \
                "created": [], \
                "body":[]}

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)

def get_date(created):
    return dt.datetime.fromtimestamp(created)
_timestamp = topics_data["created"].apply(get_date)
topics_data = topics_data.assign(_timestamp = _timestamp)

topics_data.to_csv('FILENAME.csv', index=False)