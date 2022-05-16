# What-do-Twitter-and-Reddit-users-say-about-the-Beijing-Olympics
Introduction:
This project scrapes data from Twitter and Reddit. It also makes word clouds based on the content scraped. It's goal is to see what’s the most frequent keywords about the Beijing Olympics and the negative  “boycottBeijingOlympics”, as well as the difference of discussion between that in Twitter and  Reddit.


1. Installe Requirements
Using the requirements.txt file to install all the packages needed.

2. Get API
To scrape Twitter, you don't need to apply for API.
To scrape Reddit, you need to register the Reddit API. You can start from here:
https://www.reddit.com/wiki/api
First, you need to sign up for the API.
Second, record the client ID, client secret, and user agent.

3. Run the files
There are two modes to run the file.
	
	Mode 1: python final.py --static 

This opens the stored 3 datasets and performs analysis on stored 
data.

	Mode 2: python final.py 

This will scrape data and then perform analysis on the database (most recently scraped data).

4. Save the Wordcloud Graphs
After running the code, there will be three wordclouds appearing one by one. When one graphs appear, you need to save the picture manually and one by one to ensure the program could generate another wordcloud.

