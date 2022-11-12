# # MovING_sum (The CreativeSumm 2022 Shared Task: A Two-Stage Summarization Model using Scene Attributes)
**Members: EunChong Kim, TaeWoo Yoo, GunHee Cho, SuYoung Bae, Yun-Gyung Cheong**
Department of Artificial Intelligence, Sungkyunkwan University, South Korea  
Paper: [https://aclanthology.org/2022.creativesumm-1.8](https://aclanthology.org/2022.creativesumm-1.8)

## Task Abstraction: 
MovING 팀은 CreativeSumm Workshop task 4개 중에서 **summarization of movie scripts** 에 참가했습니다.  
워크샵에서 제공한 Scriptbase 데이터셋을 사용해서 요약 성능을 높이는 Task로  abstractive와 extractive summarization 방법을 결합한 Two-Stage Summarization Model 을 제안했고, script에서 중요한 Scene 을 더 잘 추출하기 위해 Topic modeling 방법을 적용했습니다.  
저희 팀의 모델을 사용해서 평가한 결과 Baseline 결과보다 ROUGE, BERTScore에서 높은 요약 성능을 보였고, 해당 CreativeSumm Workshop task Leaderboard 에서 **2등**을 달성해 Coling 워크샵 논문 투고 및 발표를 진행했습니다.  

COLING 2022 (2022.10.12~10.17) [Link](https://coling2022.org/)  
CreativeSumm Workshop: [Link](https://creativesumm.github.io/sharedtask)  
Scriptbase [Paper](https://aclanthology.org/N15-1113/)   [Github](https://github.com/EdinburghNLP/scriptbase)

## Paper Abstraction: 
In this paper, we describe our work for the CreativeSumm 2022 Shared Task, Automatic Summarization for Creative Writing. The task is to summarize movie scripts, which is challenging due to their long length and complex format. To tackle this problem, we present a two-stage summarization approach using both the abstractive and an extractive summarization methods. In addition, we preprocess the script to enhance summarization performance. The results of our experiment demonstrate that the presented approach outperforms baseline models in terms of standard summarization evaluation metrics.  

저희 팀이 도전한 워크샵 주제는 영화 시나리오를 요약하는 작업이었습니다. 영화 시나리오는 다른 데이터셋과는 달리 길고 복잡한 형식으로 이루어져 있어 전처리 과정이 어렵습니다. 저희 팀은 영화 시나리오를 잘 요약하기 위해 abstractive 방식과 extractive 방식 모두 사용해서 두 단계로 이루어진 summarization framework 를 제안했습니다. 게다가 요약 성능을 향상시키기 위해 scene 을 main character 빈도에 따라 재구성하고, 각 scene 에 등장하는 키워드를 추출해 이를 이용하는 과정을 추가했습니다. 저희 팀이 제안한 framework 를 통해 추출한 요약 성능은 기존 baseline 모델보다 더 우수한 성능을 보이는 것을 관찰할 수 있었습니다.  



## Our model : Two-Stage Summarization Approach
### Using both the abstractive and extractive summarization method
1. similar scenes merge based on character information
2. abstractive summarization for each scene.
3. extractive summarization + topic modeling: selecting salient scenes

![enter image description here](https://github.com/BaeSuyoung/MovING_sum/blob/main/image/pic1.png)


### Framework
저희 팀의 모델 프레임워크는 다음과 같습니다. 우선 scriptbase 각 영화별로 scene 에서 주인공을 추출한 후, 주인공 별로 scene 을 다시 merge 해서 scene segmentation 을 진행합니다.  
다시 재구성한 scene 을 각각 **DialogueLM** 모델에 넣어 scene abstractive summary 를 생성하고, **LDA** topic model 을 사용해서 각 영화에서 중요한 topic 단어 10개를 추출한 후, 각 scene 에서 영화의 topic이 몇 개가 등장하는 지를 summary 옆에 추가합니다.  
마지막으로 summary 를 모두 합쳐서 **BertSum** 모델에 넣어 extractive summary 를 구성해 이를 final summary 로 정의합니다.  

![enter image description here](https://github.com/BaeSuyoung/MovING_sum/blob/main/image/pic2.png)


## Evaluation Result
저희 모델은 ROUGE, BERTScore 점수가 baseline 모델 점수보다 좋은 점수를 기록했습니다. 
![enter image description here](https://github.com/BaeSuyoung/MovING_sum/blob/main/image/pic3.png)


## Conclusion

