import tweepy
import config.config_twitter as ct
client=tweepy.Client(bearer_token=ct.BEARER_TOKEN)

query='covid -is:retweet'

response=client.search_recent_tweets(query=query,max_results=90)
res=[]
f2=open('/Users/jianxiaoyang/Documents/EC601 software/google nlp api/env/test/data.txt','a',encoding='UTF-8')
for data in response.data:
    res.append(data.text)
    print(data.text)
    f2.write(data.text)
print(res)
f2.close()


