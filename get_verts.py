# get_verts.py
# kublasean 
# 8 - 14 - 2018
# writes a .csv of twitter ids from a .csv of names to search for
import twitter
from auth import getAPI
import csv
import sys
import string 

# returns twitter user obj after searching for str name
def getUserFromName(name, api):
    user_list = api.GetUsersSearch(term=name, page=1, count=3)
    if user_list:
        user = user_list[0]
        if user.verified:
            return user
    return None

# from https://stackoverflow.com/questions/92438/stripping-non-printable-characters-from-a-string-in-python
def cleanUserName(name):
    return ''.join(list(filter(lambda x: x in string.printable, name)))

# get V and V-attributes (id, name, scrn_name,...)
# from searching for names in fname
def getVerts(fname, debug=True, api=getAPI()):
    fileoutput = ""
    queries = []
    numusers = 0

    with open(fname, 'r') as infile:
        reader = csv.reader(infile, delimiter=',')
        for row in reader:
            queries.append(row)
    if debug:
        output = "read " + repr(len(queries)) + " names to search from file"
        print(output)
    
    for i in range(len(queries)):
        output = repr(i) + ", " + queries[i][0] + ": "
        try:
            user = getUserFromName(queries[i][0], api)
        except Exception as e:
            print(output, end='')
            print(e)
            continue
        if user:
            fileoutput += ','.join([repr(user.id),queries[i][0],user.screen_name])
            for attribute in queries[i][1:]:
                fileoutput += ','+attribute
            output += cleanUserName(user.name)
            fileoutput+="\n"
            numusers += 1
        if debug:
            print(output)

    output = "pulled "+repr(numusers)+" verified twitter-ids from "+repr(len(queries))+" queries."
    if debug:
        print(output)
    return fileoutput

# argv = [ get_verts.py | infile.csv | outfile.csv ]    
if __name__ == "__main__":
    api = getAPI()
    output = ""
    usage = "usage:\npython get_verts.py search [infile.csv] [outfile.csv]\n"
    usage +="python get_verts.py followers [screen name] [outfile.csv]\n"
    usage +="python get_verts.py following [screen name] [outfile.csv]\n"

    if len(sys.argv) != 4:
        print(usage)
        quit()

    if sys.argv[1] == "search":
        output = getVerts(sys.argv[2], api=api)
    elif sys.argv[1] == "followers":
        followers = api.GetFollowers(screen_name=sys.argv[2])
        for follower in followers:
            try:
                output += repr(follower.id)+','+cleanUserName(follower.name)+','+follower.screen_name+'\n'
            except Exception as e:
                print(e)
                continue
    elif sys.argv[1] == "following":
        friends = api.GetFriends(screen_name=sys.argv[2])
        for friend in friends:
            try:
                output += repr(friend.id)+','+cleanUserName(friend.name)+','+friend.screen_name+'\n'
            except Exception as e:
                print(e)
                continue
    else:
        quit()

    print(output)
    #f = open(args[1], "w")
    #f.write(output)
    #f.close()

