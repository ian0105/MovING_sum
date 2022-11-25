import pandas as pd

data=pd.read_csv('before_preprocessed_data/new_seg_movie_dataset.csv')
data2=pd.read_csv('/home/inglab/hdd_ext/hdd1/syr/2022_DialogLM/DialogLM-main/DialogLED/Models/practice/generated_predictions.txt', delimiter='\n\n', header=None, skip_blank_lines=False)
data2 = data2.dropna()

summary_data = data[data['Summary or not']==1]
summary_data = summary_data[['Movie_name','content']]
summary_data = summary_data.reset_index(drop=True)

#content_data=data[data['Summary or not']==0]
#content_data=content_data[['Movie_name', 'content']]
content_data=data[['Movie_name', 'content']]
content_data = content_data.dropna()
content_data = content_data.reset_index(drop=True)

a = []
index = 0
for cont in data2.values:
    for i, char in enumerate(cont[0]):
        if char == '&':
            index = i
            break
    a.append(cont[0][i+1:])
data2 = pd.DataFrame(a,columns=['content'])

content_data=data[['Movie_name', 'content']]
content_data = content_data.dropna()
content_data = content_data.reset_index(drop=True)

content_data.loc[:, 'content'] = data2.loc[:, 'content']
content_data = pd.merge(content_data, summary_data, on='Movie_name')
content_data.rename(columns={"content_x":"scene_summary", "content_y":"movie_summary"}, inplace=True)

content_data.to_csv (r"/home/inglab/hdd_ext/hdd1/syr/2022_DialogLM/DialogLM-main/DialogLED/final_output/final_scene_summary_practice.csv")