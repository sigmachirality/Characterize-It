import pandas as pd

# read in marvel images
m_data = pd.read_csv('../data/marvel-wikia-data-images.csv', delimiter=',')
marvel_data = m_data['imgurl'].dropna().reset_index(drop=True)

# read in dc images
d_data = pd.read_csv('../data/dc-wikia-data-images.csv', delimiter=',')
dc_data = d_data['imgurl'].dropna().reset_index(drop=True)

# merge the data
data_series = pd.concat([marvel_data.head(100), dc_data.head(100)])
data = data_series.to_frame().reset_index(drop=True)

# read prompt word csv
words = pd.read_csv('../data/promptwords.csv', names=['prompt'])

# pick only words with length 7
long_words = words[words['prompt'].str.len() == 7]

# shuffle the rows
p_words = long_words.sample(frac=1)
prompt_words = p_words.dropna().reset_index(drop=True)

# join and write
joined = data.join(prompt_words.head(200))
final = joined.rename(index=str, columns={'imgurl':'image_url', 'prompt':'prompt'})

# write to csv
final.to_csv('../data/mturk_input_200.csv', index=False)