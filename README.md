# nba-twitter-analysis
## Making graphs of player-player connections on twitter

<img src="https://i.imgur.com/rg3jmua.png">

#### Requires:
  * [python](https://www.python.org/)
  * [python-twitter](https://python-twitter.readthedocs.io/en/latest/installation.html)
  * [python-igraph](https://igraph.org/python/)
  * [jupyter](http://jupyter.org/install)
   
#### Usage:
First, in both <b>get_verts.py</b> and <b>get_edges.py</b> you'll need to put in your twitter developer credentials. If you don't know what this means, check out [this walkthrough](https://python-twitter.readthedocs.io/en/latest/getting_started.html).

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

Run <b>get_verts.py</b> on a set of twitter names to search for these names and output a list of verified twitter ids. It was written with the intent of running on a list of NBA athletes, but any .csv style file with whatever you want to search for per user as the first column will work (some modification required as noted by comments). Then, to find the all edges between vertices in this set run <b>get_edges.py</b> on the vertex file, which outputs an edgelist file. 

```sh
python get_verts.py names_to_search.csv verts_fname.csv
python get_edges.py verts_fname.csv edges_fname.csv
```

At this point you could just load your edgelist and vertex file into your favorite graph visualization tool (mine is cytoscape) and go from there - but that would be to easy. The <b>twitter-graph</b> ipython-notebok shows a few examples of how you can programmatically generate some cool graphs and do analysis with the igraph package. 

