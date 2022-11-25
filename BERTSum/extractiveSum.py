from summarizer import Summarizer
import csv

def main(args):
    # 데이터셋
    dataset = pd.read_csv(args.data_path)

    # 전체 데이터에서 movie list 추출
    movie_list = []
    d = ''
    for data in tqdm(dataset.iterrows()):
    a = data[1]['Movie_name']
    if a != d:
        movie_list.append(a)
    d = a
    
    # 한 씬에서 하나씩 bertsum해서 합치기
    dum_data_list = []
    summary_list = []
    for idx, movie_name in tqdm(enumerate(movie_list)):
        # 영화 하나 데이터 준비
        oneM_dataset = dataset[dataset['Movie_name']==movie_name]
        oneM_dataset.reset_index(drop=True, inplace=True)

        # th 값 조정해서 중요씬 salient_ratio 이상인걸로 뽑기
        salient_ratio_th = 0.1
        for threshold in range(10, -1, -1):
            salient_ratio = len(oneM_dataset[oneM_dataset['include_topic_num']>=threshold]) / len(oneM_dataset)
            if salient_ratio_th < salient_ratio:
                oneM_dataset_th = oneM_dataset[oneM_dataset['include_topic_num']>=threshold]
                dum_data_list.append([movie_name, threshold, salient_ratio])
                break

        # th로 summary
        summary = ''
        for data in oneM_dataset_th.iterrows():
            summary = summary + ' ' + ''.join(model(data[1]['scene_summary']))
        summary = summary[1:]
    
        # th로 돌린 summary len이 4500이 넘는다면, bertsum (80%)
        if len(summary) > 4500:
            summary = ''.join(model(summary, ratio=4500/len(summary)))

        summary_list.append(summary)

    # summary 저장
    with open(args.summary_path, 'w', newline='') as f:
        write = csv.writer(f)
        write.writerow(summary_list)
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Extractive Summarization'
    )

    parser.add_argument('--data_path', default='../data/scene_summary_merge_topic.csv',
        help='Path to the merge topic csv data', type=str)
    parser.add_argument('--summary_path', default='../data/summary.txt',
        help='Path to the summary text', type=str)

    args = parser.parse_args()
    main(args)
