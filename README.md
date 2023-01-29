담당자 : 김태훈 (thkim@mnc.ai)


# 2021 NIPA 인공지능 놀이터

### Task19
[미들AI/정형] 전력 설비 이상 탐지


## 상세 설명

### 과제 설명

전력 설비 에너지 패턴 및 고장 분석 센서 데이터를 통한 이상 탐지 과제

- 추진 배경
  - 에너지 데이터 기반 AI 학습용 데이터 및 모델 구축을 통한 인공지능 기술개발, 인공지능 응용서비스/제품 개발 촉진
- 활용 가능 서비스
  - 에너지 효율 분석
  - 설비 이상 감지
  - 설비별 에너지 절감률 분석
  - 전력 피크 관리 서비스
  - 에너지 요금 합리화 등의 AI 응용 서비스 개발

### 채점 방식

**Macro F1-Score**

Macro F1 = 1/6 * sum( F1 )  
  
F1-score: Pricision과 Recall의 조화평균  
F1 = (2 * Recall * Precision ) / ( Precision + Recall )

- Recall[재현율/민감도] : ( TP ) / ( TP + FN )
- Precision[정밀도] : ( TP ) / ( TP + FP )
  - TP : True로 예측하고 실제 값도 True
  - TN : False로 예측하고 실제 값도 False
  - FP : True로 예측하고 실제는 False
  - FN : False로 예측하고 실제는 True



## 데이터

### 데이터 설명

- 입출력
  - Input : 누적전력량, 유효전력평균, 무효전력평균, 주파수, 전류평균, 상전압평균, 선간전압평균, 온도 등 23개 feature
  - Output : '정상' or '비정상'으로 채워진 `label` 컬럼

- 데이터셋 구성 : 약 270MB
  - train: 23개 feature, 1,973,449개 row로 이루어진 csv 파일
  - test: 23개 feature, 292,260 row로 이루어진 csv 파일

### 데이터 링크
- 데이터 다운로드 : [링크](https://aihub.or.kr/problem_contest/nipa-learning-platform)  
- AI hub 참고 데이터 : [전력 설비 에너지 패턴 및 고장 분석 센서](https://aihub.or.kr/aidata/30759)