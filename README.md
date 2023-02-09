## CS 579: Project 1
### Team Members: Kaylee Rosendahl, Santosh Mummidi 

*Due 2/13/23*

To run: simply run *plot_graphs.py*. 

Note: The Twitter API is no longer free after 2/9. The code used to crawl the data is included, and we saved this data to a text file for further analysis. 

#### File Breakdown: 
- **auth_keys.txt** - authorization keys for accessing the API.
- **user_crawl.py** - script for crawling user data with the API. Writes data to *users.txt*. Used the library [Tweepy](https://www.tweepy.org/) for accessing the API. 
- **users.txt** - saved user data.
- **plot_graphs.py** - plots and saves the visual graph of our network. Also calculates, plots, and saves the network measurement distributions. All are done using the Python package  [Networkx](https://networkx.org/) and library [matplotlib](https://matplotlib.org/).
