# -*- coding: utf-8 -*-

# dataset1: Scrape all tweets with keyword "BeijingOlympics"
import snscrape.modules.twitter as sntwitter
import pandas as pd
import warnings
import itertools

def get_first_dataset():
    warnings.filterwarnings('ignore')
    proxy = None
    kw = 'BeijingOlympics'
    start = "2022-02-04"
    end = "2022-02-20"
    item_num=int(10e10)
    query = '"{kw}" until:{end} since:{start}'.format(kw=kw, end=end, start=start)
    print("looking for: ", query)
    scraper = sntwitter.TwitterSearchScraper(query)
    scraper._session.proxies = {'https': proxy, 'http': proxy}
    tmp_res = scraper.get_items()  # qurey
    res_details = itertools.islice(tmp_res, item_num)  # details, maximum 10e10 records
    df = pd.DataFrame(res_details)
    print("records found: ", df.shape[0], query)
    df.to_csv("datasource1.csv", index=None)
    return df

# dataset2: Scrape all tweets with keyword "BoycottBeijingOlympics"
def get_second_dataset():
    warnings.filterwarnings('ignore')
    proxy = None
    kw = 'BoycottBeijingOlympics'
    start = "2022-02-04"
    end = "2022-02-20"
    item_num=int(10e10)
    query = '"{kw}" until:{end} since:{start}'.format(kw=kw, end=end, start=start)
    print("looking for: ", query)
    scraper = sntwitter.TwitterSearchScraper(query)
    scraper._session.proxies = {'https': proxy, 'http': proxy}
    tmp_res = scraper.get_items()  # qurey
    res_details = itertools.islice(tmp_res, item_num)  # details, maximum 10e10 records
    df = pd.DataFrame(res_details)
    print("records found: ", df.shape[0], query)
    df.to_csv("datasource2.csv", index=None)
    return df

# Scrape all comments from Reddit as dataset3
# You need to get your own user agent
import praw
import pandas as pd
def get_third_dataset():
    reddit_read_only = praw.Reddit(client_id="replace your client_id here",     
                                   client_secret="replace your client_secret here", 
                                   user_agent="replace your user_agent here")        
    # URL of the post
    url = "https://www.reddit.com/r/AskAnAmerican/comments/m5yj40/would_you_support_a_boycott_of_the_2022_beijing/"
    # Creating a submission object
    submission = reddit_read_only.submission(url=url)

    from praw.models import MoreComments

    post_comments = []

    for comment in submission.comments:
        if type(comment) == MoreComments:
            continue
        post_comments.append(comment.body)
    #creating a dataframe
    comments_df = pd.DataFrame(post_comments, columns=['comment'])
    comments_df.to_csv('datasource3.csv')
    return comments_df


# analysis content and create wordcloud
from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import matplotlib.pyplot as plt
import csv

def wordcloud_generator(data):
    data_list = []
    for i in data:
        data_list.append(i)
    text = ' '.join(data_list)
    # Generate a word cloud image
    wordcloud = WordCloud().generate(text)
    
    # Setting Stopwords
    gist_file = open("gist_stopwords.txt", "r")
    try:
        content = gist_file.read()
        stopwords = content.split(",")
    finally:
        gist_file.close()
        
    # Display the image
    wordcloud = WordCloud(width=800, height=400,stopwords = stopwords).generate(text)
    plt.figure(figsize=(20,10))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


# execute program in command line
import sys
if __name__ == "__main__":
    l = list(sys.argv)
    d = {"data1":[],"data2":[],"data3":[]}
    dataset = pd.DataFrame(data=d)
    if len(l)==2 and l[1]=='--static':
        data1 = pd.read_csv("datasource1.csv").iloc[:, 2]
        data2 = pd.read_csv("datasource2.csv").iloc[:, 2]
        data3 = pd.read_csv("datasource3.csv").iloc[:, 1]
        dataset["data1"] = data1
        dataset["data2"] = data2
        dataset["data3"] = data3
        print("data is combined, the first five rows are...", dataset[:5])
        print('generating the wordcloud...')
        wordcloud_generator(data1)
        plt.savefig('1.png')
        wordcloud_generator(data2)
        plt.savefig('2.png')
        wordcloud_generator(data3)
        plt.savefig('3.png')
        
    elif len(l)==1:
        dataset1 = get_first_dataset()
        content1 = dataset1['content']
        dataset["data1"] = content1
        dataset2 = get_second_dataset()
        content2 = dataset2['content']
        dataset["data2"] = content2
        dataset3 = get_third_dataset()
        content3 = dataset3['comment']
        dataset["data3"] =content3
        print("all data are scraped, the first five rows are...", dataset[:5])
        wordcloud_generator(content1)
        wordcloud_generator(content2)
        wordcloud_generator(content3)
        
    else:
        print("The arguments do not match the requirements. Please refer README.md for understanding the requirements")

