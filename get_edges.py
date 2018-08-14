# get_edges.py
# kublasean
# 8 - 14 - 2018
# APPENDS to .csv file of edges from verts (id -> id)
# beware of ratelimiting (15 calls per 15min per twit api endpoint)
import twitter
import csv
import sys

# returns twitter api
def getAPI():
    api = twitter.Api(consumer_key="",
                  consumer_secret="",
                  access_token_key="",
                  access_token_secret="")
    api.sleep_on_rate_limit = True
    return api

# argv = [ get_edges.py | infile.csv | outfile.csv ]
def main():
    V = []
    users = {}
    debug = True
    
    api = getAPI()

    if not api:
        print("invalid credentials")
        return -1

    if len(sys.argv) != 3:
        print("usage: python script.py infile.csv outfile.csv")
        return -1
    
    # read list of twitter ids from file
    # expects (id, name, screen_name)
    with open(sys.argv[1], 'r') as infile:
        reader = csv.reader(infile, delimiter=',')
        for row in reader:
            V.append(row[0])
            users[row[0]] = 1
    if debug:
        output = "read " + repr(len(V)) + " twitter ids from file"
        print(output)
    
    # open output file and find edges
    outfile = open(sys.argv[2], 'a+')
    counter = 0
    edge_counter = 0
    for userid in V: #change if you need to restart at particular place
        fr_ids = []
        try:
            fr_ids = api.GetFriendIDs(userid)
        except Exception as e:
            print(e)
        output = repr(counter) + ", " + userid + ": " + repr(len(fr_ids))
        if (debug):
            print(output)
        for friend_id in fr_ids:
            if repr(friend_id) in users:
                fileoutput = userid + "," + repr(friend_id) + "\n"
                outfile.write(fileoutput)
                edge_counter += 1
        counter += 1
    outfile.close()

    output = "found " + repr(edge_counter) + " nba twitter edges"
    if debug:
        print(output)
    return 0
    
if __name__ == "__main__":
    main()
