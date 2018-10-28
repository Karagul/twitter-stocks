from searchtweets import ResultStream, gen_rule_payload, load_credentials, collect_results
# premium_search_args = load_credentials("~/.twitter_keys.yaml",
#                                        yaml_key="search_tweets_premium",
#                                        env_overwrite=False)

premium_search_args = load_credentials("/Users/Daniel/OneDrive/Columbia/3rd Semester/Other/twitterStocks/Twitter_Stocks/twitter_keys.yaml",
                                       yaml_key="twitter_keys",
                                       env_overwrite=False)
rule = gen_rule_payload("beyonce", results_per_call=100) # testing with a sandbox account
tweets = collect_results(rule,
                         max_results=100,
                         result_stream_args=premium_search_args)
print(rule)
[print(tweet.all_text) for tweet in tweets[0:10]];