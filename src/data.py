import sys
import pandas as pd

# allow for command line specification of rows
if (len(sys.argv) > 1):
    num_rows = int(sys.argv[1])
else:
    num_rows = 200

# read in marvel images
m_data = pd.read_csv('../data/scraped/marvel-wikia-data-images.csv', delimiter=',')
marvel_data = m_data['imgurl'].dropna().reset_index(drop=True)

# read in dc images
d_data = pd.read_csv('../data/scraped/dc-wikia-data-images.csv', delimiter=',')
dc_data = d_data['imgurl'].dropna().reset_index(drop=True)

# read in images that have already been used
p_data = pd.read_csv('../data/submitted/mturk_input_200.csv', delimiter=',')
past_data = p_data['image_url'].dropna().reset_index(drop=True)

# merge the data, filter the data, convert to dataframe
data_series = pd.concat([marvel_data, dc_data])
data_series = data_series[~data_series.isin(past_data)].head(num_rows)
data = data_series.to_frame().reset_index(drop=True)

# below is used to get a csv of hero names
# marvel_name_data = m_data[m_data['imgurl'].isin(data_series)]['name']
# dc_name_data = d_data[d_data['imgurl'].isin(data_series)]['name']
# (pd.concat([marvel_name_data, dc_name_data])).to_csv('heroes.csv', index=False)

# read prompt word csv
words = pd.read_csv('../data/promptwords.csv', names=['prompt'])

# pick only words with length 7
long_words = words[words['prompt'].str.len() == 7]

# shuffle the rows
p_words = long_words.sample(frac=1)
prompt_words = p_words.dropna().reset_index(drop=True)

# join and write
joined = data.join(prompt_words.head(num_rows))
final = joined.rename(index=str, columns={'imgurl':'image_url', 'prompt':'prompt'})

# write to csv
final.to_csv('../data/mturk_input_{}.csv'.format(num_rows), index=False)