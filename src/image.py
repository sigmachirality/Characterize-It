import re, mimetypes, urllib, sys
import pandas as pd

# read sys args
if (len(sys.argv) > 1):
    num_rows = int(sys.argv[1])
else:
    num_rows = 800

# read in marvel images
m_data = pd.read_csv(
    '../data/scraped/marvel-wikia-data-images.csv', delimiter=',')
marvel_data = m_data[['page_id', 'imgurl']].dropna().reset_index(drop=True)

# read in dc images
d_data = pd.read_csv('../data/scraped/dc-wikia-data-images.csv', delimiter=',')
dc_data = d_data[['page_id', 'imgurl']].dropna().reset_index(drop=True)

# define downloader function
root = '../data/images/'
def download_file(url, path):
    print(path)
    try:
        urllib.request.urlretrieve(url, path + '.png')
    except:
        print("Exception occured - " + path)

# download images
for _, row in marvel_data.head(num_rows).iterrows():
    url = row['imgurl']
    path = root + 'm' + str(row['page_id'])
    download_file(url, path)

for _, row in dc_data.head(num_rows).iterrows():
    url = row['imgurl']
    path = root + 'd' + str(row['page_id'])
    download_file(url, path)
