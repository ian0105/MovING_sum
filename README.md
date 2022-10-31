# # MovING_sum (The CreativeSumm 2022 Shared Task: A Two-Stage Summarization Model using Scene Attributes)
**Members: EunChong Kim, TaeWoo Yoo, GunHee Cho, SuYoung Bae, Yun-Gyung Cheong**
Department of Artificial Intelligence, Sungkyunkwan University, South Korea  
Paper: [https://aclanthology.org/2022.creativesumm-1.8](https://aclanthology.org/2022.creativesumm-1.8)

## Task Abstraction: 
MovING 팀은 CreativeSumm Workshop task 4개 중에서 **summarization of movie scripts** 에 참가했습니다.  
워크샵에서 제공한 Scriptbase 데이터셋을 사용해서 요약 성능을 높이는 Task로  abstractive와 extractive summarization 방법을 결합한 Two-Stage Summarization Model 을 제안했고, script에서 중요한 Scene 을 더 잘 추출하기 위해 Topic modeling 방법을 적용했습니다.  
저희 팀의 모델을 사용해서 평가한 결과 Baseline 결과보다 ROUGE, BERTScore에서 높은 요약 성능을 보였습니다.

COLING 2022 (2022.10.12~10.17) [Link](https://coling2022.org/)  
CreativeSumm Workshop: [Link](https://creativesumm.github.io/sharedtask)  
Scriptbase [Paper](https://aclanthology.org/N15-1113/)   [Github](https://github.com/EdinburghNLP/scriptbase)

## Paper Abstraction: 
In this paper, we describe our work for the CreativeSumm 2022 Shared Task, Automatic Summarization for Creative Writing. The task is to summarize movie scripts, which is challenging due to their long length and complex format. To tackle this problem, we present a two-stage summarization approach using both the abstractive and an extractive summarization methods. In addition, we preprocess the script to enhance summarization performance. The results of our experiment demonstrate that the presented approach outperforms baseline models in terms of standard summarization evaluation metrics.

## Our model : Two-Stage Summarization Approach
### Using both the abstractive and extractive summarization method
1. similar scenes merge based on character information
2. abstractive summarization for each scene.
3. extractive summarization + topic modeling: selecting salient scenes

![enter image description here](https://github.com/BaeSuyoung/MovING_sum/blob/main/image/pic1.png)


### Framework
![enter image description here](https://github.com/BaeSuyoung/MovING_sum/blob/main/image/pic2.png)


## Evaluation Result

![enter image description here](https://github.com/BaeSuyoung/MovING_sum/blob/main/image/pic3.png)


## Conclusion
