import tweepy

#Twitter Authentication
auth = tweepy.OAuthHandler("yD0PYw6sHKXcfVblNsifwefP5","B1m4rUxhq64Z6vE2yKSi6PCV4RgDwxq4tvIH1Ll0ZlG5OE07TC")
auth.set_access_token("1521864363820392454-Wkh8cpRgIlFVf61QY1QiJYVGreW9eY","F3TeeDIUAd4avD0lUYCThH8Akp4jo74ZMKkH2Ds7iZhum")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#Search a tweet mentioning @ExactementBot and respond "Exactement !"
for tweet in api.search_tweets (q="@ExactementBot"):
    try:
        api.update_status("@" + tweet.user.screen_name + " Exactement !", in_reply_to_status_id = tweet.id)
        print("Tweet sent")
    except tweepy.TweepError as e:
        print(e.reason)