import pandas as pd
#import re

data=pd.read_csv('before_preprocessed_data/new_seg_movie_dataset.csv')

content_data=data[data['Summary or not']==0]
content_data=content_data[['Movie_name','content']]

# csv to json
df= content_data
df.rename(columns={"content":"src", "Movie_name":"tgt"}, inplace=True)
df=df[["src", "tgt"]]
df = df.dropna().reset_index(drop=True)

df["src"] = df["src"].str.replace(pat=r'([A-Z]{2,})[ \n][(]([a-z]{2,})[)]\n([A-Z])', repl=r'\1 : \3', regex=True)
df["src"] = df["src"].str.replace(pat=r'([A-Z]{2,})\n([A-Z])', repl=r'\1 : \2', regex=True)
df["src"] = df["src"].str.replace(pat='\n\n', repl=' ', regex=False)
df["src"] = df["src"].str.replace(pat='\n', repl=' ', regex=False)
df["src"] = df["src"].str.replace(pat=r'''[^A-Za-z0-9\n:'".?!\(\) ]''', repl=r'', regex=True)
df["src"] = df["src"].str.replace(pat='\\n', repl='', regex=False)
df["src"] = df["src"].str.replace(pat="\'", repl="'", regex=False)
df["src"] = df["src"].str.replace(pat='\"', repl='"', regex=False)
df["src"] = df["src"].str.replace(pat=r'([ \t\r\n\v\f]{1,})', repl=r' ', regex=True)

df.to_json ("data/train_practice.json")