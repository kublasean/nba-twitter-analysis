# nba-twitter-analysis
## Making graphs of player-player connections on twitter

![Warriors Twitter Graph](https://imgur.com/a/JYZr0yG "GSW Graph")

#### Requires:
  * python
  * python-twitter
  * python-igraph
  * jupyter
   
#### Usage:
First, in both <b>get_verts.py</b> and <b>get_edges.py</b> you'll need to put in your twitter developer credentials. If you don't know what this means, check out this walkthrough.

```python
# returns twitter api
# (this codeblock is in both .py files)
def getAPI():
    api = twitter.Api(consumer_key="",
                  consumer_secret="",
                  access_token_key="",
                  access_token_secret="")
    api.sleep_on_rate_limit = True
    return api
```

Run <b>get_verts.py</b> on a set of twitter names to search for these names and output a list of twitter ids. It was written with the intent of running on a list of NBA athletes, but any .csv style file with whatever you want to search for per user as the first column will work (some modification required as noted by comments). Then, to find the all edges between vertices in this set run <b>get_edges.py</b> on the vertex file, which outputs an edgelist file. 

```sh
python get_verts.py names_to_search.csv verts_fname.csv
python get_edges.py verts_fname.csv edges_fname.csv
```

