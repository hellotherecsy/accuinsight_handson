# 데이터 소개

<https://www.kaggle.com/uciml/sms-spam-collection-dataset>

Kaggle에 등록된 영어 SMS 메시지 데이터

* class : ham/spam (Label)

* sms : 메시지 내용

# RP + ML 데모 시나리오

## 1. ML

### 1. ML 데이터셋 불러오기

![image-20191023192824464](images/image-20191023192824464.png)

DATASET 탭에서 New 버튼 클릭

![image-20191023192916767](images/image-20191023192916767.png)

ICOS 선택 후, 폴더 버튼을 눌러 ICOS File Browser 창을 오픈

IBMO...-6 스토리지 선택, hanson-bucket 선택

RP/sms 폴더 내부에 training 데이터와 test 데이터가 있음

![image-20191023192955526](images/image-20191023192955526.png)

Dataset Name과 Description을 적당히 적어주고,

Header exists는 FALSE로 선택, Delimiter는 | 로 입력 (`Shift + \`, 파이프)

training 데이터와 test 데이터 모두 해준다

![image-20191023193054602](images/image-20191023193054602.png)

원격 클러스터를 선택 후 실행 클릭

![image-20191023195317498](images/image-20191023195317498.png)

데이터셋 등록이 완료되면, 우측 편집 버튼을 클릭해 _c2 column의 타입을 Vector Type으로 바꿔줌

### 2. Pipeline 생성 및 학습

![image-20191023193317461](images/image-20191023193317461.png)

WORKSPACE 탭에서 New 버튼을 클릭해 새 탭 생성

Select Dataset. 우측의 폴더 버튼을 눌러 데이터셋을 가져옴

![image-20191023193344746](images/image-20191023193344746.png)

등록된 training 데이터를 적용

![image-20191023193506795](images/image-20191023193506795.png)

알고리즘은 GBTClassifier를 선택

input 파라미터에서 _c2만 선택되게 수정

![image-20191023193519298](images/image-20191023193519298.png)

label 파라미터는 _c0 선택

![image-20191023193542511](images/image-20191023193542511.png)

validationSetPath 파라미터에는 등록한 test 데이터를 선택

다른 값들은 default 값으로 남겨둠

모든 값을 입력했다면 우측 상단의 Run 버튼 클릭

![image-20191023193707100](images/image-20191023193707100.png)

클러스터를 선택하고, 모델 Name과 Description을 적당히 작성

저장 경로는 HDFS를 선택하고

![image-20191023193646857](images/image-20191023193646857.png)

파일 브라우저에서 tmp 폴더를 선택 (tmp 내부에 새 폴더를 생성하여 선택하여도 무관)

모든 값을 입력했다면 Run 버튼을 클릭하고 학습이 완료될 때까지 기다림

![image-20191023195543568](images/image-20191023195543568.png)

학습이 완료되었다면 우측 상단의 Show results 버튼을 클릭해 학습 및 테스트 결과를 확인할 수 있음

## 2. RP

### 1. 토픽 생성

![image-20191024083606901](images/image-20191024083606901.png)

큐 탭의 토픽 관리 메뉴 클릭

우측 상단의 신규 생성 버튼 클릭

![image-20191024083647899](images/image-20191024083647899.png)

들어오는 메시지를 저장할 토픽과, 스팸 분류 결과를 저장할 토픽 2개를 등록함

토픽명을 적당히 적어주고 저장

![image-20191024083800746](images/image-20191024083800746.png)

정상적으로 2개가 생성되었는지 확인

### 2. 콜렉터 생성 및 실행

![image-20191024083850253](images/image-20191024083850253.png)

콜렉터 탭의 생성 메뉴 클릭하여 콜렉터 생성 페이지 오픈

![image-20191024083946386](images/image-20191024083946386.png)

좌측 Source 탭의 exec-source 버튼을 드래그&드랍하거나 더블클릭하여 exec-source 노드 생성

우측 Command 프로퍼티에 아래 값 입력

`while read line; do echo $line; sleep 1; done < sms.json`

* **주의 : 위 커맨드가 실행되기 위해 콜렉터를 실행하는 클러스터의 네임노드에 파일을 미리 넣어두어야 함 (경로 : `/home/ecouser/sms.json`**

![image-20191024085319197](images/image-20191024085319197.png)

콜렉터가 끝나지 않고 계속 돌게 하고 싶다면, 더보기를 눌러 4.Restart 프로퍼티를 체크해줌

![image-20191024084444061](images/image-20191024084444061.png)

Channel 탭의 memory-channel 노드를 동일한 방식으로 생성한 후 exec-source 노드와 연결

연결은 시작 노드의 테두리를 클릭한 채로 끝 노드의 근처로 마우스를 이동하면 자동으로 연결됨

![image-20191024084655267](images/image-20191024084655267.png)

Sink 탭의 kafka-sink 노드를 생성

![image-20191024084739028](images/image-20191024084739028.png)

kafka-sink 노드가 선택된 상태면 우측 프로퍼티에 kafka-sink의 프로퍼티가 나옴

1.Clustername에서 클러스터를 선택하고, 더보기 버튼을 눌러 4.Kafka.Topic에는 등록했던 메시지를 저장할 토픽 이름을 선택

![image-20191024084939663](images/image-20191024084939663.png)

memory-channel 노드와 kafka-sink 노드를 연결해 줌

우측의 Collector 탭을 클릭하고 콜렉터 Name을 적당히 작성함

그 후 우측 상단의 저장 버튼 클릭

![image-20191024085137448](images/image-20191024085137448.png)

저장 완료가 되었다면 콜렉터 탭의 관리 페이지 오픈

등록한 콜렉터 우측의 기능에서 시작 버튼 클릭

![image-20191024085219453](images/image-20191024085219453.png)

실행할 콜렉터를 선택

![image-20191024085431214](images/image-20191024085431214.png)

콜렉터가 정상적으로 실행되고 있는지 확인하기 위해, 큐 > 토픽 관리에서 토픽 샘플 조회를 할 수 있음

![image-20191024085516428](images/image-20191024085516428.png)

데이터가 큐에 들어가고 있는 것을 확인

### 3. 스트리밍 생성 및 실행

![image-20191024085627544](images/image-20191024085627544.png)

스트리밍 탭의 생성 페이지 오픈

![image-20191024085649670](images/image-20191024085649670.png)

Reader 탭의 kafka 노드 생성

![image-20191024085735126](images/image-20191024085735126.png)

프로퍼티에서 메시지가 등록되고 있는 클러스터와 토픽을 선택

컨슈머 그룹 명은 적당히 입력해줌

![image-20191024085824765](images/image-20191024085824765.png)

데이터 샘플링 우측 새로고침 버튼을 누르면 큐에 등록된 데이터 샘플을 확인할 수 있음

![image-20191024085902624](images/image-20191024085902624.png)

Parser 탭의 json 노드를 생성하고, kafka reader 노드와 연결해줌

![image-20191024090007394](images/image-20191024090007394.png)

테이블 명을 `sms`라고 적어주고, 컬럼 목록의 자동파싱 버튼 클릭

(kafka reader 노드와 연결이 되어있지 않다면 자동파싱이 되지 않으므로 주의한다)

![image-20191024090108587](images/image-20191024090108587.png)

데이터 샘플과 결과를 확인할 수 있음

![image-20191024090138077](images/image-20191024090138077.png)

컬럼 정보와 포맷 데이터를 확인해보고, 정상적으로 처리되었다면 적용 버튼 클릭

![image-20191024090849639](images/image-20191024090849639.png)

Function 탭의 sql 노드를 만들어 json parser 노드와 연결함

Sql에는 `select *, regexp_replace(lcase(*), '([^A-Za-z ])', ' ') from sms` 를 입력해줌

(만약 json parser 노드에서 테이블 명을 다르게 입력했다면, Sql 문의 `from sms`를 `from [입력한 테이블 명]` 으로 바꿔서 입력)

위 Sql문을 통해 원본 텍스트를 소문자화한 후, 알파벳과 공백만 남기는 가공 작업이 진행됨

![image-20191024091107038](images/image-20191024091107038.png)

컬럼 목록의 추가 버튼을 클릭해 컬럼을 2개로 만든 다음, 컬럼 명과 데이터 타입을 지정해 줌

(첫 컬럼은 메시지 원본 텍스트이며, 두번째 컬럼은 가공한 메시지 텍스트)

![image-20191024091332297](images/image-20191024091332297.png)

룰 방식과 ML 방식 두 가지로 스팸 필터링을 진행하기 위해, Fork 탭의 clone 노드를 생성한 후 sql 노드와 연결

#### 1. 룰 방식

![image-20191024091516266](images/image-20191024091516266.png)

룰 방식은 간단하게 스팸 메시지에 자주 등장하는 단어가 메시지에 포함되어 있다면 스팸으로 판별하기로 함

Filter 탭의 StringContain 노드를 생성해 clone 노드와 연결함

![image-20191024091808554](images/image-20191024091808554.png)

컬럼 목록 우측의 추가 버튼을 클릭해 검색 문자를 4개로 만듬

연산 대상 컬럼은 모두 가공된 데이터 컬럼을 선택하고, 검색 문자에 각각 `www, co, uk, prize` 를 입력함

![image-20191024092113485](images/image-20191024092113485.png)

필터링된 메시지를 큐에 저장하기 위해, Writer 탭의 kafka 노드를 생성

클러스터를 지정한 후, 스팸 메시지를 저장하기 위해 미리 생성해 놓은 토픽을 선택

#### 2. ML 방식

메시지 데이터를 ML 파이프라인에 돌리기 위해 vectorize 작업이 필요함

![image-20191024092407100](images/image-20191024092407100.png)

Filter 탭의 vectorize 노드를 생성하고, clone 노드와 연결함

![image-20191024092454476](images/image-20191024092454476.png)

프로퍼티의 변환 대상 컬럼을 가공된 텍스트 컬럼으로 선택해줌

![image-20191024092537083](images/image-20191024092537083.png)

미리 만들어둔 ML 파이프라인을 불러오기 위해, Function 탭의 mlPipelines 노드를 생성하고 vectorize 노드와 연결

![image-20191024092617449](images/image-20191024092617449.png)

모델 경로 선택에서 ML 모델을 저장했던 경로를 선택하고 확인 (모델 폴더명은 `MDL_......` 형태로 되어 있음)

![image-20191024092744606](images/image-20191024092744606.png)

처리 대상 컬럼을 vector 컬럼으로 선택

![image-20191024092941806](images/image-20191024092941806.png)

ML 파이프라인의 예측 결과를 조회하기 위해 Writer 탭의 sparkSQL 노드를 생성, mlPipelines 노드와 연결

![image-20191024093051482](images/image-20191024093051482.png)

테이블 명을 적당히 입력해주고, 데이터 지속 시간을 10000으로 입력

![image-20191024093142342](images/image-20191024093142342.png)

모든 작업이 완료되었다면 상단의 그룹, 이름, 설명을 입력하고 저장 버튼 클릭

![image-20191024093255682](images/image-20191024093255682.png)

스트리밍 탭의 관리 페이지에서 저장된 스트리밍을 확인할 수 있음

![image-20191024093331590](images/image-20191024093331590.png)

우측의 실행 버튼을 클릭하고, 클러스터를 선택하여 실행

![image-20191024093359201](images/image-20191024093359201.png)

스트리밍 이름을 클릭해 상세 페이지로 진입

![image-20191024093442706](images/image-20191024093442706.png)

상세 페이지에서 스트리밍의 현재 상태를 확인할 수 있음

sparkSQL writer 노드의 조회 버튼을 클릭해 ML 모델의 예측 결과를 확인해보자

![image-20191024093545900](images/image-20191024093545900.png)

sql문을 수정해 더 깔끔하게 결과를 확인할 수 있음

![image-20191024093836825](images/image-20191024093836825.png)

차트 뷰에서 X-axis가 prediction인 Pie Chart를 생성해 스팸으로 분류된 메시지의 비율을 확인

![image-20191024093720713](images/image-20191024093720713.png)

`select prediction, text from result where prediction == "spam"`

위 sql문으로 스팸으로 분류된 메시지만 확인하는 것도 가능

![image-20191024093937656](images/image-20191024093937656.png)

룰 방식으로 분류된 메시지를 확인하기 위해, 큐 > 토픽 관리에서 스팸 메시지를 저장하는 토픽의 샘플을 조회
