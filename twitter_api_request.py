from searchtweets import ResultStream, gen_rule_payload, load_credentials, collect_results


def removeRetweetsReplies(tweets):
    filteredTweets = []
    for tweet in tweets:
        if tweet.in_reply_to_user_id == None:
            filteredTweets.append(tweet)
    return filteredTweets

premium_search_args = load_credentials("/Users/Daniel/OneDrive/Columbia/3rd Semester/Other/twitterStocks/Twitter_Stocks/twitter_keys.yaml",
                                       yaml_key="twitter_keys",
                                       env_overwrite=False)
rule = gen_rule_payload("from:elonmusk", results_per_call=100) # testing with a sandbox account


rs = ResultStream(rule_payload=rule,
                  max_results=500,
                  max_pages=1,
                  **premium_search_args)
tweets = list(rs.stream())


filteredTweets = removeRetweetsReplies(tweets)

[print(tweet.created_at_datetime) for tweet in filteredTweets];
[print(tweet.all_text, end='\n\n') for tweet in filteredTweets];
print(len(filteredTweets))

