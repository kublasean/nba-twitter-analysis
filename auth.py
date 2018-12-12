import twitter

# returns twitter api
def getAPI():
    api = twitter.Api(consumer_key="ipc5sPpJQNZ1Ko2aSb8rd2TR6",
                  consumer_secret="YGmRt2QjCuma0q3BI3FQVX0elzLXndPq1tDDsYN1u4KnhuFBLk",
                  access_token_key="372058543-HTTmrAWgDUyc3U19GtZLkyy8Cs5gMrKwUCxTeZNC",
                  access_token_secret="56YqXznFOqW0L1CaXkVzZtdnKrXlAFIz61oca0JaYUCMJ")
    api.sleep_on_rate_limit = True
    return api