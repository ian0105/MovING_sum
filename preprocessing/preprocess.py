from .movie_class import Movie
import pandas as pd
import re
import os


def make_dataset(path):
    # movie scirpt -> pd format dataset
    pd_movie = pd.DataFrame(columns=['Movie_name','Scene_number','Summary or not','content'])
    filenames = os.listdir(path)
    for filename in filenames:
        try:
            movie = Movie(filename,path)
        except:
            continue
#    print(movie.moviename)
        for i, scene in enumerate(movie.scenes):
            if len(str(scene))>5:
                pd_movie = pd_movie.append({'Movie_name':movie.moviename,'Scene_number':i,'Summary or not':0,'content':scene},ignore_index=True)
        pd_movie = pd_movie.append({'Movie_name':movie.moviename,'Scene_number':-1,'Summary or not':1,'content':movie.summary},ignore_index=True)  
    print('영화 수: ', df.shape[0])
    pd_movie.to_csv("moviescript_dataset.csv")

def dialogue_extraction():
    df = pd.read_csv('script_dataset.csv',index_col=0)
    contents = []
    texts = []
    for text in df['content']:
        content = []
        index = []
        text = re.sub(r'\([^)]*\)', '', text)
        dialogues = re.findall(r'[A-Z]+\n(.+?)\n', text)
        dialogues += re.findall(r'[A-Z]+\n\n(.+?)\n', text)
        text = text.split('\n')
        text = [n for n in text if n]
        dialogue = ''
        for dia in dialogues:
            for i, t in enumerate(text):
                if t == dia:              
                    char = text[i-1]
                    if not char.isupper():
                        char = None        
                    else:
                        index.append(i-1)
                        index.append(i)
                    break
            if char:
            dialogue += char + '\n' + dia + '\n' 
        #print(index)
        for i, t in enumerate(text):
            if i in index:
                text[i] = text[i] 
            else:
            
                if i == 0:
                    text[i] = '(' + text[i]
                if i == len(text)-1:
                    text[i] = text[i] + ')'
                if i-1 in index:
                    text[i] = '(' + text[i]
                if i+1 in index:
                    text[i] = text[i] + ')'
        text = '\n'.join(text)
        texts.append(text)
        contents.append(dialogue)
    for i, content in enumerate(df['content']):
        if i not in summary_index:
            df['content'][i] = texts[i]
        else:
            df['content'][i] = df_summary['content'][i]
    df.to_csv('대화평서문분리.csv')

def find_character_name(text):
    character_list = []
    text = text.split('\n')
    for t in text:
        if t.strip().isupper():
            #t = re.sub(r'\([^)]*', '', t).strip()
            #t = re.sub(r'\n[^)]*', '', t).strip()
            character_list.append(t)
        
    return list(set(character_list))
 
def continue_or_not(char_list,characters1,characters2):
    if set(char_list) & set(characters1) == set(char_list) & set(characters2):
        return 1
    elif len(set(char_list) & set(characters1) & set(characters2))>=1:
        return 1
    return 0
    
def scene_segmentation():
    df = pd.read_csv('대화평서문분리.csv') 
    summary = df[df['Summary or not'] == 1]
    A = df[df['Summary or not'] == 1].index
    df.drop(A,axis='index',inplace=True)
    df = df.dropna()
    seg_movie = pd.DataFrame(columns=['Movie_name','Scene_number','scene_summary','movie_summary'])
    stoplist = ['Superman II', 'Ted (film)']
    for num, name in enumerate(set(df2['Movie_name'])):
        if name in stoplist:
            continue
        movie_characters = df[df['Movie_name']==name]['Character_list'].values
        movie_contents = df2[df2['Movie_name']==name]['scene_summary'].values
        scenes_len = len(movie_characters)
        char = []
        for characters in movie_characters:
            for c in characters:
                char.append(c)
        num_occur = Counter(char)
        main_characters_list = num_occur.most_common(10)
        main_character =[]
        c = 0
        for character, count in main_characters_list:
            c += count
            main_character.append(character)
            if c > scenes_len:
                break
        ans = []
        for i in range(scenes_len):
      #  print(i)
            if i == 0:
                continue
            character1 = movie_characters[i-1]
            character2 = movie_characters[i]
      #  print(continue_or_not(main_character,character1,character2))
            ans.append(continue_or_not(main_character,character1,character2))
    
        scene_numbers = [0]
        scenes = movie_contents[0]
    #print(len(ans),len(movie_contents))
        for i, an in enumerate(ans):
            if an == 1: 
                scene_numbers.append(i+1)
                scenes += movie_contents[i+1]
            else:
                seg_movie = seg_movie.append({'Movie_name':name,'Scene_number':scene_numbers,'scene_summary':scenes,'movie_summary':summary[summary['Movie_name']==name]['content'].values[0]},ignore_index=True)
                scene_numbers = [i+1]
                scenes = movie_contents[i+1]
#    seg_movie = seg_movie.append({'Movie_name':name,'Scene_number':scene_numbers,'scene_summary':scenes,'movie_summary':summary[summary['Movie_name']==name]['content'].values[0]},ignore_index=True)
    seg_movie.to_csv("after_seg_movie_dataset.csv")

def main(args):
    make_dataset(args.data_path)
    dialogue_extraction()
   


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Preprocess movie scripts'
    )

    parser.add_argument('--data_path', default='../data/scriptbase/',
        help='Path to the long dialogue data', type=str)

    args = parser.parse_args()
    main(args)
