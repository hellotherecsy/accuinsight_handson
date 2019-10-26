
> 목차
> ---
> 1. [분석 요건에 대한 정의](scenario_2.md#분석-요건에-대한-정의)
>    1. 실제 공유오피스 분석 화면
> 1. [데이터 준비](scenario_2.md#데이터-준비)
>    1. Dataset 1: 좌석 예약 데이터
>    1. Dataset 2: 좌석 메타 데이터
> 1. [데이터 처리 (Batch Pipeline)](scenario_2.md#데이터-처리-batch-pipeline)
>     1. [데이터파일 2개 조인하여 ETL작업 수행하기](scenario_2.md#데이터파일-2개-조인하여-etl작업-수행하기)
>         1. [생성 메뉴로 이동](scenario_2.md#생성-메뉴로-이동)
>         1. [데이터 로딩](scenario_2.md#데이터-로딩)
>         1. [필요한 컬럼 선택](scenario_2.md#필요한-컬럼-선택)
>         1. [데이터 정제](scenario_2.md#데이터-정제)
>         1. [통계](scenario_2.md#통계)
>         1. [join key 생성](scenario_2.md#join-key-생성)
>         1. [2개파일 조인](scenario_2.md#2개파일-조인)
>         1. [새로운 column 생성](scenario_2.md#새로운-column-생성)
>         1. [불필요한 column 삭제](scenario_2.md#불필요한-column-삭제)
>         1. [null값 제거](scenario_2.md#null값-제거)
>         1. [컬럼명 변경](scenario_2.md#컬럼명-변경)
>         1. [ICOS에 저장](scenario_2.md#ICOS에-저장)
>         1. [저장 및 실행](scenario_2.md#저장-및-실행)
>     1. [워크플로우 상태 확인](scenario_2.md#워크플로우-상태-확인)
>     1. [실행결과 확인](scenario_2.md#실행결과-확인)
> 1. [데이터 시각화 (Data Insight)](scenario_2.md#데이터-시각화-data-insight)
>     1. [데이터 셋 준비](scenario_2.md#데이터-셋-준비)
>         1. [데이터 셋 추가](scenario_2.md#데이터-셋-추가)
>     1. [차트 작성](scenario_2.md#차트-작성)
>         1. [분석 작업 관리](scenario_2.md#분석-작업-관리)
>     1. [DASHBOARD](scenario_2.md#DASHBOARD)

<br/><br/>

# 분석 요건에 대한 정의

> 약 25개의 SK 관계사들의 건물별 좌석 유형별 구성원 속성을 분석한다.

# 실제 공유오피스 분석 화면

- 좌석유형별 주 이용 나이


![ex_screenshot](./img/scenario2.png)

<br/><br/>


## 데이터 준비
ICOS에 업로드된 데이터를 사용합니다.  
스토리지 : IBMOSC1146611-6  
버킷 : handson-bucket  

(1) Dataset 1 : 좌석 예약 데이터

| column명 | column 설명 | Value Example |
|---|:---:|---:|
| `bldg` | 빌딩명 | SKC 본사, 서린 빌딩, ... |
| `desk_type` | 좌석 유형 | 일반좌석, 스탠딩좌석, ... |
| `desk_id` | 각 좌석의 ID | 3a27b3bf-d8de-11e8-975a-0a9726611f46 |
| `dt` | 예약 날짜 | 20190803 |
| `com` | 회사명 | SK C&C, SK이노베이션, … |
| `age` | 나이대 | 20대,30대,... |

 
(2) Dataset 2 : 좌석 메타 데이터

| column명 | column 설명 | Value Example |
|---|:---:|---:|
| `bldg` | 빌딩명 | SKC 본사, 서린 빌딩, ... |
| `desk_type` | 좌석 유형 | 일반좌석, 스탠딩좌석, ... |
| `occupied` | 고정좌석 여부 | N, Y |
| `desk_id` | 각 좌석의 ID | 3a27b3bf-d8de-11e8-975a-0a9726611f46 |
| `dt` | 예약 날짜 | 20190803 |

## 데이터 처리

<br/>

### 데이터파일 2개 조인하여 ETL작업 수행하기

<br/>

> ETL flow 구성내용 : ICOS에서 파일 불러오기 → 데이터 정제 → 통계 → join key 생성 → 2개 파일 join → 새로운 column 생성 → 불필요한 column 삭제 → null값 제거→ column명 rename → ICOS에 저장  

<br/>

#### 생성 메뉴로 이동

<br/>

![ex_screenshot](./img/BP_start.png)

<br/>

#### 데이터 로딩

<br/>

![ex_screenshot](./img/DataLoading_1027.png)

<br/>

데이터 불러오기 그룹에서 ICOS 불러오기 노드를 캔버스 영역에 drag & drop하여 node 생성  
우측 property 패널  
- **file** : 불러오려는 ICOS 파일의 경로 지정
    - 좌석 예약 데이터의 경로 : IBMOSC1146611-6 스토리지에서 handson-bucket/DI/Dataset/desk_resv
    - 좌석 메타 데이터의 경로 : IBMOSC1146611-6 스토리지에서 handson-bucket/DI/Dataset/desk_info
- **option** : 데이터에 header가 없는 경우 false로 변경
- **schema** : `자동 파싱 열기` 클릭  

<br/>

schema - `자동 파싱 열기` - sample data 탭에서 데이터 샘플을 확인
schema - `자동 파싱 열기` - column info 탭에서 컬럼명 변경

> 좌석 예약 데이터 : bldg, desk_type, desk_id, dt, com, age

`확인` 클릭 

     Note : 우측 property 패널 - schema 에서 직접 컬럼명 변경 가능

<br/>

동일한 방법으로 좌석 메타 데이터도 불러오기 & 컬럼명 변경  
> 좌석 메타 데이터 : bldg, desk_type, occupied, desk_id, dt  

<br/>

#### 데이터 정제

<br/>

![ex_screenshot](./img/s2_distinct_filter.png)

<br/>

`distinct` 노드 drag & drop하여 좌석 예약 데이터에서 중복 예약 제거<br/>
좌석 예약 데이터의 `select` 노드에서 `distinct` 노드로 연결<br/><br/>
`filter` 노드 drag & drop하여 좌석 메타 데이터에서 고정 좌석 제외<br/>
좌석 메타 데이터의 `select` 노드에서 `filter` 노드로 연결<br/>
우측 property 패널  
- **col** : occupied
- **filterOption** : =:equal
- **filterValue** : 'N'  

<br/>

#### 통계

![ex_screenshot](./img/s2_agg.png)

`agg` 노드 drag & drop하여 좌석 예약 데이터에서 빌딩별 좌석유형별 회사별 나이대별 예약좌석수 계산<br/>
`distinct` 노드에서 `agg` 노드로 연결<br/>
우측 property 패널<br/>
- **aggcol** : bldg, desk_type, dt, com, age<br/>
- **target** : func count, col desk_id<br/>

<br/>

**agg** 노드 drag & drop하여 좌석 메타 데이터에서 빌딩별 좌석유형별 전체좌석수 계산<br/>
`filter` 노드에서 `agg` 노드로 연결<br/>
우측 property 패널<br/>
- **aggcol** : bldg, desk_type, dt<br/>
- **target** : func count, col desk_id<br/>

<br/>

#### join key 생성

![ex_screenshot](./img/s2_aql.png)

`SQL` 노드 drag & drop하여 좌석 예약 데이터에서 join key 생성  
좌석 예약 데이터의 `agg` 노드에서 `SQL` 노드로 연결<br/>
우측 property 패널  
- **query**  

```SQL
select bldg,desk_type,dt,com,age,countdesk_id as resv, concat(bldg,'_',desk_type,'_',dt) as key  
from default;  
```

- **overwriteSchema** 체크 (SQL 결과로 변경된 데이터 적용)  

<br/>

`SQL` 노드 drag & drop하여 좌석 메타 데이터에서 join key 생성  
좌석  데이터의 `agg` 노드에서 `SQL` 노드로 연결<br/>
우측 property 패널  
- **query**  

```SQL
select countdesk_id as total, concat(bldg,'_',desk_type,'_',dt) as key  
from default;
```

- **overwriteSchema** 체크 (SQL 결과로 변경된 데이터 적용)  

<br/>

#### 2개파일 조인

![ex_screenshot](./img/s2_join.png)

좌측의 `데이터 처리하기` 패널에서 `dataJoin` 노드 우측 캔버스에 drag & drop하여 생성  
`SQL` 노드 두개를 `dataJoin` 노드로 연결<br/>
우측 property패널  
- **col1** : 좌석 예약 데이터의 key 선택  
- **col2** : 좌석 메타 데이터의 key 선택  
- **how** : right_outer 선택 (col1,col2 순서가 바뀐 경우 left_outer 선택)  

#### 새로운 column 생성

![ex_screenshot](./img/s2_withColumn.png)

`withColumn` 노드 drag & drop하여 좌석이용률 계산  
`dataJoin` 노드에서 `withColumn` 노드로 연결<br/>
우측 property 패널  
- **selectType** : column
- **col1** : resv_dt_~
- **operator** : /
- **col2** : total_dt_~
- **newColumn** : ratio  

<br/> 

#### 불필요한 column 삭제

![ex_screenshot](./img/s2_drop.png)

`drop` 노드 drag & drop하여 불필요한 데이터 삭제  
`withColumn` 노드에서 `drop` 노드로 연결<br/>
우측 property 패널  
- **col** checkbox에서 아래 4가지 column 체크
    - 좌석 예약 데이터의 resv_df_~
    - 좌석 예약 데이터의 key_df_~
    - 좌석 메타 데이터의 total_df_~
    - 좌석 메타 데이터의 key_df_~  

#### null값 제거

![ex_screenshot](./img/s2_filter.png)

`filter` 노드 drag & drop하여 회사명이 '\N'이면 삭제 
`drop` 노드에서 `filter` 노드로 연결<br/>
우측 property 패널  
- **col** : com_df_~
- **filterOption** : !=:not equal
- **filterValue** : '\N'  

<br/>

필터 추가 & **filterOperator**는 **OR**로 설정  
- **col** : age_df_~
- **filterOption** : !=:not equal
- **filterValue** : ‘\N’  

<br/>

#### 컬럼명 변경

![ex_screenshot](./img/s2_withColumnRenamed.png)

`withColumnRenamed` 노드 drag&drop하여 생성  
`filter` 노드에서 `withColumnRenamed` 노드로 연결<br/>
우측 property 패널  
- `전체 컬럼 불러오기` 아이콘을 통해 자동 파싱  

<br/>

#### ICOS에 저장

![ex_screenshot](./img/s2_export.png)

좌측 `데이터 내보내기` 클릭  
`ICOS 내보내기` 노드 drag & drop 하여 생성  
`withColumnRenamed` 노드에서 `ICOS 내보내기` 노드로 연결  

<br/>

우측 property 패널  
- **path**의 browse 아이콘을 클릭하여 열리는 팝업에서 저장할 디렉토리 위치 선택 후 확인 클릭 (ex. ~/DI/results)  
- **folder**에 생성할 디렉토리명 입력 (ex. edu01_scenario2)  

<br/>

#### 저장 및 실행
  
캔버스 상단에 워크플로우 이름 입력 (ex. 회의실 일평균 좌석이용률)

<br/>

캔버스에서 **ETL** 클릭 후 **appName** 입력 (ex. scenario1)

![ex_screenshot](./img/s2_final.png)

`저장` 클릭<br/>
`실행` 클릭  

<br/>

#### 워크플로우 상태 확인

![ex_screenshot](./img/s2_stateCheck.png)

`워크플로우 관리` 화면으로 이동하여 상태 확인<br/>
이미 성공으로 종료되었거나 오류가 발생하여 종료된 경우 INACTIVE 상태<br/>
상세정보 컬럼의 `인스턴스 목록` 아이콘 클릭하면 이전 실행 이력 관리 가능<br/>

<br/>

#### 실행결과 확인

![ex_screenshot](./img/s2_resultCheck.png)

`브라우저` 탭 > `ICOS` 메뉴로 이동<br/>
지정했던 ICOS directory 위치로 이동하여 내보내기로 생성한 디렉토리 하단의 part-00000-~파일 클릭<br/>
우측 상단의 `다운로드` 버튼 클릭하여 파일내용 확인<br/>

<br/><br/>

## 데이터 시각화 (Data Insight)

<br/>

### 데이터 준비

#### 데이터 셋 추가
`데이터 셋 관리` 페이지에서 `데이터 셋 추가`를 클릭하면 추가 페이지로 이동합니다.<br/>

<br/>

![ex_screenshot](./img/addDataset.png)

<br/>

DataInsight 분석 및 시각화를 위해 MariaDB, ICOS, HIVE 등 다양한 종류의 데이터 셋을 추가할 수 있습니다.<br/>
지원하는 Data Source 타입<br/>
① 로컬 파일 : csv 타입 등 로컬에 있는 파일을 업로드<br/>
② MariaDB : MariaDB 테이블 연동하여 데이터 업로드<br/>
③ AWS RDS: AWS RDS 테이블 연동하여 데이터 업로드<br/>
④ HIVE : 하둡 클러스터의 데이터를 hive를 통하여 업로드<br/>
⑤ ICOS : IBM 오브젝트 스토리지의 파일을 업로드<br/>
⑥ MySQL : MySQL 테이블을 연동하여 데이터 업로드<br/>

<br/>

> 위에서 Batch Pipeline을 통해 실행한 결과 파일을 사용합니다.<br/>
> 스토리지 : IBMOSC1146611-6<br/>
> 버킷 : handson-bucket<br/>

`데이터 셋 추가` 클릭 후 `ICOS` 선택<br/>
1단계_ICOS선택<br/>
2단계_Bucket선택<br/>
`스키마 편집` 클릭<br/>

<br/>

![ex_screenshot](./img/s2_schema.png)

<br/>

`수정` 클릭하여 그룹 설정 및 데이터 셋 이름 변경<br/>
- part-00000-~ -> 좌석유형별 주 이용 나이<br/>


각 컬럼의 `필드명 변경`을 통해 컬럼명 변경<br/>
- **bldg** -> 건물명<br/>
- **desk_type** -> 좌석유형<br/>
- **dt** -> 날짜<br/>
- **com** -> 회사명<br/>
- **age** -> 나이대<br/>
- **ratio** -> 좌석이용률<br/>

`저장` 클릭<br/>
_새로운 분석 작업 페이지로 이동 하겠습니까?_ 라는 팝업이 뜨면 `이동`하거나 `아니요`하고 다음 단계<br/>

<br/>

### 차트 작성

<br/>

#### 분석 작업 관리
`분석 작업 관리` 페이지에서 `분석 작업 생성`을 클릭하면 추가 페이지로 이동합니다.<br/>
차트 작성할 데이터 셋 `적용`<br/>

![ex_screenshot](./img/s2_selectDataset.png)

<br/>

`분석 작업 생성` 팝업이 뜨면 **그룹** 지정 및 **분석 작업 제목** 입력<br/>
`저장` 클릭<br/>

<br/>

필터 추가<br/>
- **건물명** = 서린 빌딩<br/>
- **회사명** = SK트레이딩인터내셔널 **or** SK이노베이션 **or** SK에너지 **or** SKC (<U>회사명 필터 카테고리 내</U>에서 추가)<br/>
- **날짜** = 20190820<br/>
- **나이대** = 30대<br/>

<br/>

`차트 생성` 버튼 클릭<br/>
  
![ex_screenshot](./img/makeChart.png)

`파이 차트` 선택  
- **Grouping** : 좌석유형<br/>
- **Value** : 좌석이용률<br/>
- **Flag** : SUM<br/>
  
![ex_screenshot](./img/s2_makeChart.png)
    
`저장` 클릭<br/>

<br/>

### Go Editor

에디터를 통해 분석 차트의 외관 수정이 가능합니다.<br/>
차트 색, 배경 색, 투명도 등을 변경하여 차트를 보기 좋게 디자인 할 수 있습니다.<br/>

<br/>

    소수점 2째 자리까지 : Number formatting에서 Precision을 2로 변경
    애니메이션 삭제 : Miscellaneous에서 Start duration을 0으로 변경
    Label 위치 변경 : Legend에서 Align 콤보박스 선택
    Label의 Column 개수 증가 : Legend에서 Max columns 개수 지정
    타이틀 설정 : Title에서 Text에 ‘30대의 좌석유형별 이용현황’ 입력

<br/>
