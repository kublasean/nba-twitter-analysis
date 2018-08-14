# get_verts.py
# kublasean 
# 8 - 14 - 2018
# APPENDS a .csv of twitter ids from names to search for
import twitter
import csv
import sys
import pickle

# returns twitter user obj after searching for str name
def getUserFromName(name, api):
    user_list = api.GetUsersSearch(term=name, page=1, count=3)
    if user_list:
        user = user_list[0]
        if user.verified:
            return user
    return None

# argv = [ get_verts.py | infile.csv | outfile.csv ]
def main():
    players = []
    teams = []
    users = {}
    debug = True

    # put api creds here
    api = twitter.Api(consumer_key="",
                  consumer_secret="",
                  access_token_key="",
                  access_token_secret="")
    api.sleep_on_rate_limit = True
    
    if not api:
        print("invalid credentials")
        return -1

    if len(sys.argv) != 3:
        print("usage: python script.py infile.csv outfile.csv")
        return -1
    
    # read list of nba player names from file
    # expects player name as first field in each row
    with open(sys.argv[1], 'r') as infile:
        reader = csv.reader(infile, delimiter=',')
        for row in reader:
            players.append(row[0])
            if (len(row) >= 2):
                teams.append(row[1]) # optional add other attribs here
    if debug:
        output = "read " + repr(len(players)) + " player names from file"
        print(output)
    
    # open output file
    outfile = open(sys.argv[2], 'a+')
    
    # get V and V-attributes (id, name, scrn_name)
    # writes lines as discovered for fear of Exceptions
    counter = 0
    for player in players:
        output = repr(counter) + ", " + player + ": "
        try:
            user = getUserFromName(player, api)
        except Exception as e:
            print(e)
            dump = open('user_dump', "w+")
            pickle.dump(users, dump) #dump users found so far
            dump.close()
            outfile.close()
            return -1
        if user:
            fileoutput = repr(user.id) + ",none," + user.screen_name + "," + teams[counter] + "\n"
            users[repr(user.id)] = user
            output += user.name
            outfile.write(fileoutput)
        if debug:
            print(output)
        counter += 1

    output = "pulled " + repr(len(users)) + " nba twitter users"
    if debug:
        print(output)
    outfile.close()
    return 0
    
if __name__ == "__main__":
    main()
