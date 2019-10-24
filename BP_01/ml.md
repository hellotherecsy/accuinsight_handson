# ML Modeler

![](images/ml/01.start.png)

## 소개

ML Modeler는 머신러닝을 코딩없이 사용할 수 있는 웹 기반 분산 병렬 모델링 도구입니다.

## 특징

1. **손쉬운 머신러닝 모델 구축**
   - 시간 및 장소 상관없이 몇 분 안에 모델을 구축. 데이터 형식 제한 웹 서비스로 프로덕션 환경 배포 가능.
1. **M/L 알고리즘 적용 용이성**
   - GUI로 Feature Engineering, 머신러닝 알고리즘 설계 및 분석 용이
1. **간단한 머신러닝 모델 구축 및 대용량 분산처리**
   - Auto Model으로 분류 알고리즘의 매개변수 자동으로 탐색하여 최적의 결과 빠른 도출. SparkML 알고리즘(Transformation, Classification, Regression, Clustering)으로 대용량 분산처리.
1. **분석 모델 관리 편의성**
   - 데이터 셋 / 파이프라인 / 모델 통합 관리. 학습된 모델 저장 및 실 데이터 예측.

## 제공 기능

1. **Workspace Canvas**
   - 머신러닝과 Feature Engineering 조합하여 파이프라인 설계.
1. **Auto Model**
   - 분류 알고리즘의 최적 매개변수 자동 탐색으로 빠른 결과 도출.
1. **데이터 / 모델 / 파이프라인 관리**
   - 데이터 원본 및 알고리즘 적용 가능. 데이터 셋 / 학습 모델 / 파이프라인 저장 관리 기능.

## 데모

사용자가 주문한 상품의 정보로 쇼핑몰 연령대 분류

### 사용 데이터

- BP 결과 데이터

| user_id | age | category | price | group | style | age_group |
|---|---|---|---|---|---|---|
| 사용자 고유 식별자 | 사용자 나이 | 상품 카테고리 | 상품 가격 | 쇼핑몰이 등록한 연령대 | 쇼핑몰이 등록한 스타일 | 사용자 연령대 |

### 데이터셋 불러오기

![](images/ml/02.dataset.png)

ML Modeler를 생성할 때 필요한 데이터셋을 추가한다.

#### 데이터셋 정보 저장

![](images/ml/03.new.dataset.png)

Batch Pipeline에서 만든 데이터를 불러온다.

- HDFS 경로 입력: 
  - 경로: `/tmp/shop/part-000.csv`
- Dataset Name: `Shop Train`
- Header exists: `TRUE`
- Delimiter: `,`
- Description: `훈련 데이터`

### 파이프라인 생성

![](images/ml/05.workspace.png)

Workspace 메뉴에서 파이프라인을 생성한다.

#### 데이터셋 선택

![](images/ml/06.select.dataset.png)

Pipeline에서 등록한 데이터셋을 선택한다.

#### 알고리즘 추가: OneHotEncoder

![](images/ml/07.onehot.png)

`OneHotEncoder를` 추가한다. `group`과 `style` 컬럼에 있는 값들을 0과 1로 이루어진 배열로 변환한다.

  - input: `group, style`
  - output: `group_encoded,style_encoded`
  - dropLast: `true`

#### 알고리즘 추가: RandomForestClassifier

![](images/ml/08.rfc.png)

`RandomForestClassifier를` 추가한다. `age_group`을 기준으로 라벨링을 한다.

  - automodel: `false`
  - input: `category, price, group_encoded, style_encoded`
  - output: `predict_age_group`
  - label: `age_group`
  - splitWeight: `0.7`
  - seed: `2`
  - 나머지 기본 설정 그대로

### 파이프라인 저장

![](images/ml/09.save.pipeline.png)

**Save pipeline** 클릭 후 `shop_pipeline`으로 저장

### 파이프라인 실행

**Run** 버튼을 클릭하여 모델을 생성한다.

#### 클러스터 선택

![](images/ml/10.run.select.cluster.png)

클러스터를 선택한다.

#### 모델 저장 경로 선택

![](images/ml/11.run.select.path.png)

새 폴더를 만들어서 모델 저장 경로를 선택한다.

- 경로: `/tmp/model`

#### 파이프라인 실행

![](images/ml/12.run.png)

파이프라인을 실행한다.

### 결과

![](images/ml/13.result.png)
![](images/ml/14.descript.png)

**Show results** 버튼을 클릭해서 결과를 확인한다. 

### 모델 확인

![](images/ml/15.model.png)
![](images/ml/16.model.predict.png)

Model 메뉴에서 저장한 모델을 확인한다.
### 파이프라인 확인

![](images/ml/17.pipeline.png)

Pipeline 메뉴에서 저장한 파이프라인을 확인한다.

### 훈련 기록 확인

![](images/ml/18.history.png)

Training History 메뉴에서 모델 학습 기록들을 확인한다.