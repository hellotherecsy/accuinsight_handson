# Batch Pipeline

![](images/bp/01.start.png)

## 소개

Batch Pipeline은 대규모 데이터를 안정적으로 처리하고 Job 스케줄링과 모니터링 기능을 제공하는 솔루션입니다. 복잡한 데이터의 배치 처리를 간단한 Workflow UI로 제공합니다. Drag & Drop으로 설계하는 Workflow, 배치 작업의 통합적인 실행/제어 기능과 직관적인 DashBoard를 제공합니다.

## 제공 기능

Drag & Drop으로 손쉽게 Oozie 기반의 워크플로우를 작성할 수 있다.

1. **컴포넌트 제공 및 스케줄 관리**
   - 다양한 하둡 에코 작업 / 시스템 작업을 컴포넌트 형태로 표현. 시작 시각, 종료 시각, 스케줄 주기 설정 용이.
1. **데이터 조회 및 분석 작업 지원**
   - 워크플로우 작성과 함께 인터렉티브하게 데이터 확인 가능.
1. **변수 처리 지원**
   - 일반/날짜 파라미터, 데이터 셋 등 다양한 동적 변수 지정 가능.
1. **모니터링 제공**
   - 배치 작업 별 상태 및 실행 정보를 직관적인 UI로 제공.
1. **다양한 관리 도구**
   - HDFS, Hive, S3 등 다양한 브라우저와 관리 기능 제공.

## 데모

### 사용 데이터

- **사용자 주문 정보**: 상품을 주문한 사용자 정보. `orders.csv`
- **상품 정보**: 상품의 정보와 상품을 판매하는 쇼핑몰 정보. `goods.csv`

#### 사용자 주문 정보

상품을 주문한 사용자 정보가 담겨 있다.

| user_id | goods_id | age | date |
|---|---|---|---|
| 사용자 고유 식별자 | 주문한 상품의 고유 식별자 | 사용자 나이 | 주문 날짜 |

- 사용자 나이 범위: 15 ~ 45
- 나이가 45인 경우 45세 이상

#### 상품 정보

상품의 정보와 상품을 판매하는 쇼핑몰 정보가 담겨 있다.

| goods_id | category | price | image_type | image_width | image_height | shop_id | name | group | style | timestamp |
|---|---|---|---|---|---|---|---|---|---|---|
| 상품 교유 식별자 | 상품 카테고리 | 상품 가격 | 상품 이미지 확장자 | 상품 이미지 너비 | 상품 이미지 높이 | 쇼핑몰 고유 식별자 | 쇼핑몰 이름 | 쇼핑몰이 등록한 연령대 | 쇼핑몰이 등록한 스타일 | 상품 정보 등록 시간 |

- 상품 카테고리: 상의, 바지, 스커트, 원피스, 비치웨어, 아우터, 악세사리, 슈즈, 가방, 패션소품, 피트니스, 란제리&파자마
- 이미지 확장자: jpg, gif, png
- 쇼핑몰 연령대: 10대, 20대 초반, 20대 중반, 20대 후반, 30대 초반, 30대 중반, 30대 후반
- 쇼핑몰 스타일: 페미닌, 모던시크, 심플베이직, 러블리, 유니크, 미시스타일, 캠퍼스룩, 빈티지, 섹시글램, 스쿨룩, 로맨틱, 오피스룩, 럭셔리, 헐리웃스타일

### 결과 데이터셋

사용자, 주문, 상품, 쇼핑몰 정보를 처리하여 얻고자 하는 데이터 형태는 다음과 같다.

| user_id | age | category | price | group | style | age_group | dates |
|---|---|---|---|---|---|---|---|
| 사용자 고유 식별자 | 사용자 나이 | 상품 카테고리 | 상품 가격 | 쇼핑몰이 등록한 연령대 | 쇼핑몰이 등록한 스타일 | 사용자 연령대 | 주문 날짜 |

### 세션 생성

![](images/bp/30.open.session.png)

1. 세션 관리
   - `상단 메뉴 → 실행 → 세션 관리`
1. 클러스터 세션 생성 버튼 클릭

![](images/bp/31.create.session.png)

1. 생성 버튼 클릭

### 워크플로우 생성

![](images/bp/02.workflow.png)

1. 워크플로우 생성
   - `상단 메뉴 → 워크플로우 → 생성`
1. 워크플로우 정보 입력
   - 그룹: `Tutorial`
   - 이름: `Shopping mall data pipeline`
   - 설명: `Demo using shopping mall data`
1. 클러스터 선택
   - `우측 메뉴 → setting → cluster`: 클러스터 선택. 

### ETL 추가

#### 노드 추가

![](images/bp/03.etl.png)

1. `좌측 메뉴 → 데이터 불러오기 → ICOS 불러오기`
   - 캔버스로 **드래그앤드롭**하여 노드를 추가한다.
1. ETL 설정
   - 생성된 **ETL 글씨를 클릭하고** 우측 메뉴에서 변수를 설정한다.
   - `우측 메뉴 → property → appName`: 앱 이름 설정. (예: `batchApp`)

#### 데이터 불러오기 설정

![](images/bp/04.file.select.png)

ICOS 불러오기 노드를 클릭하고 우측 메뉴에서 변수를 설정한다.

- Node description: `주문 정보 불러오기`.
- file: 폴더 아이콘 버튼 클릭한다.

![](images/bp/05.file.browser.png)

스토리지에서 파일을 선택한다.

- 스토리지: `IBMOSC1146611-6`
- Bucket: `handson-bucket`
- 경로: `/BP/Shop/orders.csv`

#### 데이터 자동 파싱

![](images/bp/06.auto.parse.png)

- schema: 자동 파싱 열기 버튼을 클릭한다.

![](images/bp/09.parse.data.png)

파싱이 완료되면 워크플로우를 **저장**한다.

### 상품 정보 불러오기 추가

![](images/bp/36.drag.png)

1. `좌측 메뉴 → 데이터 불러오기 → ICOS 불러오기`
   - **ETL 상자 위**로 **드래그앤드롭**하여 노드를 추가한다.

![](images/bp/11.input.data.png)

1. 파일 선택
   - 스토리지: `IBMOSC1146611-6`
   - Bucket: `handson-bucket`
   - 경로: `/BP/Shop/goods.csv`
1. 자동 파싱 확인

![](images/bp/35.second.data.png)

### 결측값 제거

![](images/bp/12.dropna.png)

상품 정보 중에 결측값이 있으면 제거한다.

1. `좌측 메뉴 → 데이터 처리(기본) → dropna`
   - 노드 이름: `결측값 제거`
1. `상품 정보 불러오기` 노드와 연결.
1. `dropna` 노드에서 컬럼을 선택한다.
    - Drop 처리 방법: any

### 데이터 결합

![](images/bp/13.data.join.png)

`주문 정보 불러오기`와 `결측값 제거` 노드를 결합하여 데이터셋을 하나로 만든다.

1. `좌측 메뉴 → 데이터 처리(기본) → dataJoin`
   - 노드 이름: `데이터 결합`
1. `주문 정보 불러오기`와 `결측값 제거`를 `dataJoin` 노드와 연결.
1. `dataJoin` 노드 설정
    - col1: goods_id
    - col2: goods_id
    - how: inner

### 스키마 확인

![](images/bp/34.schema.2.png)

1. `데이터 결합` 노드에서 스키마 버튼 클릭
1. 결합된 데이터셋 정보 확인

두 가지 데이터가 결합되어 컬럼 이름은 `컬럼명`에서 `컬럼명_df_[랜덤값]`으로 바뀐다. 

![](images/bp/34.schema.png)

### 스냅샷 확인

![](images/bp/33.snapshot.2.png)

1. `데이터 결합` 노드에서 스냅샷 버튼 클릭
1. 결합된 데이터셋 확인

두 가지 데이터가 결합되어 컬럼 이름은 `컬럼명`에서 `컬럼명_df_[랜덤값]`으로 바뀐다. 

![](images/bp/33.snapshot.png)

### 컬럼 선택

![](images/bp/14.select.png)

결합한 데이터에서 필요한 컬럼만 선택한다.

1. `좌측 메뉴 → 데이터 처리(기본) → select`
   - 노드 이름: `컬럼 선택`
1. `데이터 결합` 노드와 연결.
1. 컬럼 선택
   - user_id_df_[랜덤값]
   - age_df_[랜덤값]
   - category_df_[랜덤값]
   - price_df_[랜덤값]
   - group_df_[랜덤값]
   - style_df_[랜덤값]
   - dates_df_[랜덤값]

데이터가 결합 노드를 지나면 컬럼 이름은 `컬럼명`에서 `컬럼명_df_[랜덤값]`으로 바뀐다.  
따라서 다음 [컬럼 이름 변경](#컬럼-이름-변경) 노드에서 컬럼 이름을 정리해야 한다.

### 컬럼 이름 변경

![](images/bp/15.rename.png)

컬럼 이름 자동 변경 기능을 사용한다.

1. `좌측 메뉴 → 데이터 처리(기본) → withColumnRenamed`
   - 노드 이름: `컬럼 이름 변경`
1. `컬럼 선택` 노드와 연결.
1. 전체 컬럼 불러오기 버튼 클릭

### 연령대 분류

![](images/bp/16.with.column.png)

사용자 연령 범위(15 ~ 45)를 단위 구간으로 나누어 새로운 컬럼(`age_group`)으로 저장한다.

1. `좌측 메뉴 → 데이터 처리(기본) → withColumn`
   - 노드 이름: `연령대 분류`
1. `컬럼 이름 변경` 노드와 연결.
1. `expression` 설정을 다음과 같이 한다.
   - selectType: `numeric`
   - col: `age`
   - operator: `/`
   - value: `12`
   - newColumn: `age_group`

### 캐스팅

![](images/bp/17.cast.png)

사용자 연령대(`age_group`) 값을 정수로 표현한다.

1. `좌측 메뉴 → 데이터 처리(기본) → cast`
   - 노드 이름: `형 변환`
1. `연령대 분류` 노드와 연결.
1. `subset` 설정을 다음과 같이 한다.
   - col: `age_group`
   - dataType: `IntergerType()`

### 데이터 내보내기

![](images/bp/19.save.data.png)

HDFS에 데이터셋을 저장한다.

1. `좌측 메뉴 → 데이터 내보내기 → HDFS 내보내기`
   - 노드 이름: `데이터 저장`
1. `형 변환` 노드와 연결.
1. path: 폴더 아이콘 버튼 클릭 후 스토리지에서 저장할 위치를 선택한다.
   - 경로: `hdfs://10.x.x.x:8020/tmp`
   - HDFS의 IP 주소는 유동적이다.
1. folder: 새로 생성할 폴더 이름
   - 이름: `bp_shop`

Hadoop으로 처리한 데이터는 자동으로 파일명이 지정된다.  
(예: `part-00000-f57ca98e-3c25-4479-aa8e-334dc6850638-c000.csv`)

**마지막으로 워크플로우를 저장한다.**


### 세션 종료

![](images/bp/37.close.session.png)

만약 클러스터에게 할당된 자원이 적다면, Livy 세션을 종료하여 자원을 확보한다.

### 실행

![](images/bp/20.job.run.png)

워크플로우를 저장하고 실행 버튼을 클릭한다. 워크플로우가 실행되며 노드 색깔이 초록색으로 바뀐다.

### 작업 완료

![](images/bp/21.job.finish.png)

워크플로우 실행이 완료되어 노드 상태가 `실행완료`로 바뀌었다.

### 데이터 확인

![](images/bp/22.browser.png)

HDFS 브라우저에서 생성된 데이터셋을 확인한다.

- 클러스터: `expert01-231710`
- 경로: `/tmp/bp_shop/part-000.csv` (파일 이름은 Hadoop이 자동으로 생성하여 저장한다.)

파일을 더블 클릭하여 샘플 데이터를 미리 보거나 다운로드 버튼을 사용하여 로컬에 저장한다.

![](images/bp/23.dataset.png)

### 작업 실행 상태 확인

실행되고 있는 작업의 상태나 종료된 작업의 기록을 확인할 수 있다.  

#### 워크플로우 목록

![](images/bp/24.workflow.list.png)

1. `상단 메뉴 → 워크플로우 → 관리`
   - 워크플로우 관리 페이지로 들어간다.
1. 생성한 워크플로우의 `인스턴스 목록` 버튼을 클릭한다.

#### 워크플로우 인스턴스 목록

![](images/bp/25.instance.list.png)

실행되고 있는 워크플로우의 상태와 종료된 워크플로우 기록을 확인할 수 있다.  
현재 작업을 멈추거나 지난 작업을 다시 실행할 수 있다.

1. `Job ID` 링크를 눌러 인스턴스 상세 정보 페이지로 들어간다.

#### 워크플로우 인스턴스 흐름

![](images/bp/26.instance.detail.png)

워크플로우 실행 흐름을 확인할 수 있다.  
인스턴스 상태는 **실행 전**, **실행 중**, **실행 완료**, **에러**로 나눠진다.

각 노드를 클릭하면 실행 로그를 확인할 수 있다.  
로그의 종류는 **INFO**, **STD**, **ERR**로 나눠진다.

터미널 접속 없이 웹페이지에서 간단하게 로그를 확인할 수 있다.  
노드별로 로그를 확인이 가능하기 때문에, 에러가 발생한 노드와 원인을 쉽게 파악할 수 있다.

#### 워크플로우 인스턴스 상세

![](images/bp/27.instance.detail.2.png)

`상세` 탭을 클릭하여 인스턴스 정보를 간단히 확인할 수 있다.  
자세한 정보를 보려면 `DHP 콘솔` 링크를 클릭한다.

#### 어플리케이션 상세 정보

![](images/bp/28.dhp.detail.png)

워크플로우 인스턴스 상세 페이지에서 `DHP 콘솔` 링크를 클릭하면, 어플리케이션 작업에 대한 정보를 볼 수 있다.

#### 작업 정보 목록

![](images/bp/29.dhp.list.png)

DHP 클러스터 페이지에서 실행한 작업들의 정보와 클러스터 상태를 확인할 수 있다.

### HIVE 태이블 생성하기
HDFS에 저장된 데이터를 학습/테스트 데이터로 나누기 위하여 HIVE Table을 생성한다.

![](images/bp/30.hive.menu.png)

1. `상단 메뉴 → 브라우저 → HIVE ` 
   - HIVE 브라우저를 선택한다.
1. `좌측 메뉴`에서 이미 생성된 DHP 클러스터를 선택한다.
1. `HIVE 계정 관리`를 선택하고 HIVE 계정을 추가한다.

![](images/bp/31.hive.manageuser.png)

![](images/bp/32.hive.adduser.png)

1. `쿼리` 화면에 아래의 sql을 입력하여 Table을 생성한다. 
- 칼럼 정보(category STRING, price INT, groups STRING, style STRING, age INT, order_date STRING, user_id STRING, age_group INT)를 입력하는 순서는 **실제 저장된 파일의 칼럼 순서와 동일**하게 입력.
   - CREATE EXTERNAL TABLE IF NOT EXISTS shopping_data (`category STRING, price INT, groups STRING, style STRING, age INT, order_date STRING, user_id STRING, age_group INT`) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE LOCATION '`/tmp/bp_shop`' TBLPROPERTIES ("skip.header.line.count"="1")

    생성된 테이블 내용을 확인한다.

![](images/bp/33.hive.createtable.png)

### 데이터 나누기

1. `상단 메뉴 → 워크플로우 → 관리` 화면에서 워크플로우 편집을 선택한다.
1. `좌측 메뉴 → Flow 구성 → hiveToHdfs`
   - **캔버스의 ETL 상자 밖**으로 **드래그앤드롭**하여 트레이닝 셋을 저장할 노드를 추가한다.

![](images/bp/34.hive.trainingset.png)

1. hiveToHdfs 노드의 property를 아래와 같이 설정하고 기존에 생성한 **ETL 캔버스**와 연결한다.
    - Node Description: `트레이닝 셋 저장`
    - cluster: DHP 클러스터 선택
    - user: Hive 브라우저에서 생성한 유저 아이디 입력
    - path: Hive 쿼리 결과를 저장할 폴더 선택 `/tmp/bp_shop/`
    - fileName: Hive 쿼리 결과를 저장할 파일 이름 입력 `traing.csv`
    - header: 데이터에 HEAD 포함하기 위해 `체크`
    - sql: 쿼리 입력
        - `select * from shopping_data where ABS(HASH(order_date))%10 < 8;`

    ![](images/bp/35.hive.trainingset2.png)

1. `좌측 메뉴 → Flow 구성 → hiveToHdfs`
   - **캔버스의 ETL 상자 밖**으로 **드래그앤드롭**하여 테스트 셋을 저장할 노드를 추가한다.
1. hiveToHdfs 노드의 property를 아래와 같이 설정하고 기존에 생성한 **트레이닝 셋 저장 노드**와 연결한다.
    - cluster: DHP 클러스터 선택
    - user: Hive 브라우저에서 생성한 유저 아이디 입력
    - path: Hive 쿼리 결과를 저장할 폴더 선택 `/tmp/bp_shop/`
    - fileName: Hive 쿼리 결과를 저장할 파일 이름 입력 `test.csv`
    - header: 데이터에 HEAD 포함하기 위해 `체크`
    - sql: 쿼리 입력
        - `select * from shopping_data where ABS(HASH(order_date))%10 >= 8;`
    ![](images/bp/36.hive.testset.png)

1. 최종 워크플로우를 저장하고 실행을 누른다.

    ![](images/bp/37.hive.running.png)


### 데이터 확인

![](images/bp/38.hive.datacheck.png)

HDFS 브라우저에서 생성된 트레이닝/테스트 데이터를 확인한다.

- 경로: `/tmp/bp_shop/training.csv`, `/tmp/bp_shop/test.csv`

파일을 더블 클릭하여 샘플 데이터를 미리 보거나 다운로드 버튼을 사용하여 로컬에 저장한다.
