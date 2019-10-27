import os
from multiprocessing import Process
from dotenv import load_dotenv
import praw
import asyncio


async def subscribe(message, subreddit_name):
    redd = reddit_class(message, subreddit_name)
    await message.channel.send('Subscribed to %s' % subreddit_name)
    await redd.get_new_posts()



class reddit_class():


    def __init__(self, message, subreddit_name):
        load_dotenv('../.env')
        CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
        USER_AGENT = os.getenv('REDDIT_USER_AGENT')
        SECRET = os.getenv('REDDIT_SECRET')

        self.message = message
        self.subreddit_name = subreddit_name

        self.reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=SECRET, user_agent=USER_AGENT)

    

    async def get_new_posts(self):

        new_post = None

        while True:
            query = self.reddit.subreddit(self.subreddit_name).new(limit=1)

            for post in query:

                if new_post == None or post.id != new_post.id :
                    new_post = post
                    self.post_msg = new_post.title
                    print(new_post.title)

                    msg = 'https://reddit.com' + new_post.permalink
                    await self.message.channel.send(msg)

            await asyncio.sleep(5.0)