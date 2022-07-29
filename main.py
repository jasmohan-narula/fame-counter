# Import required modules
import requests
import json
from bs4 import BeautifulSoup
from lxml import etree,html
from instaloader import Instaloader, Profile

# Import files
import properties

def get_youtube_subscribers(youtube_channel_name_or_id):
    youtube_url = "https://www.youtube.com/c/" + youtube_channel_name_or_id + "/about"
    
    # Request the page
    youtube_page = requests.get(youtube_url)


    youtube_page_soup = BeautifulSoup(youtube_page.content, "html.parser")

    youtube_page_string=str(youtube_page_soup)
    start = youtube_page_string.find('"subscriberCountText":') + 22
    end = youtube_page_string.find(',"tvBanner":')
    youtube_page_string_parse = youtube_page_string[start:end]

    youtube_subscriber_json = json.loads(youtube_page_string_parse)

    youtube_subscriber_count=youtube_subscriber_json['simpleText']
    youtube_subscriber_count=youtube_subscriber_count.split(" ")[0]
    print("YouTube Subscribers for channel " + youtube_channel_name_or_id +" : " + youtube_subscriber_count)
    
    return youtube_subscriber_count

if(properties.youtube_channel_name_or_id != None):
    get_youtube_subscribers(properties.youtube_channel_name_or_id)


def get_instagram_followers(instagram_handle):
    insta_loader = Instaloader()
    insta_profile = Profile.from_username(insta_loader.context, instagram_handle)

    insta_follower_count = str(insta_profile.followers)

    print("Instgram Followers for @" + instagram_handle + ": " + insta_follower_count)

    return insta_follower_count
    
if(properties.instagram_handle != None):
    get_instagram_followers(properties.instagram_handle)