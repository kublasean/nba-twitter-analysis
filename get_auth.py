# returns twitter api
def getAPI():
    api = twitter.Api(consumer_key="",
                  consumer_secret="",
                  access_token_key="",
                  access_token_secret="")
    api.sleep_on_rate_limit = True
    return api