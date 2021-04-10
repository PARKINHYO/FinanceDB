<h1 align="center">Welcome to 주린이를 위한 정보 모음집👋</h1>
<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/PARKINHYO/FinanceDB" target="_blank">
  </a>
  <a href="https://github.com/PARKINHYO/FinanceDB/blob/master/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-yellow.svg" />
  </a>  
</p>

<p align="center">
<img alt="character" width="600" src="https://user-images.githubusercontent.com/47745785/114260854-46a15880-9a12-11eb-8470-1bc3ac641294.jpg" />

</p>

<p align="center">
증권 서비스를 구현하기 위한 DB 설계와 질의 및 응용 프로그램을 구현합니다. 
</p>

## 📚 Requirement

### 회사 테이블

* 회사는 ISIN(국제증권식별번호), 회사이름, 시가총액, 시가총액의 순위를 저장합니다.
* ISIN은 Primary Key, 회사이름은 Candidate Key입니다. 
* 시가총액은 ?조 ?억원 단위로 입력합니다. 
* 회사와 시세는 '주식가격'이라는 1:N의 관계를 가집니다. 


### 시세 테이블

* 시세는 MPNO, 날짜, 종가, 전일비, 고가, 저가, 거래량, INO를 저장합니다. 
* MPNO는 Primary Key이고, 자동생성됩니다. 
* INO는 회사의 ISIN 어트리뷰트의 외래키입니다. 
* 시세와 회사는 '주식가격'이라는 N:1의 관계를 가집니다. 

### 코스피 테이블 
* 코스피는 날짜, 체결가, 전일비, 등락률을 저장합니다. 
* 날짜는 Primary Key입니다. 
* 증권시장에 상장된 모든 상장기업을 기준으로 테이블을 정의합니다. 

## 📁 ERD

<p align="center">
<img alt="character" width="800" src="https://user-images.githubusercontent.com/47745785/114264707-6abb6480-9a27-11eb-905a-7a92abd164ad.png" />
</p>

## 💻 Test

### 회사와 코스피 삽입

<p align="center">
<img alt="character" width="1000" src="https://user-images.githubusercontent.com/47745785/114269392-c1359c80-9a41-11eb-96ff-31e5a9f1e1b7.png" />
</p>

<p align="center">
<img alt="character" width="1200" src="https://user-images.githubusercontent.com/47745785/114269409-d90d2080-9a41-11eb-8814-bd01023564c4.png" />
</p>

<br>


### 시세 삭제

<p align="center">
<img alt="character" width="800" src="https://user-images.githubusercontent.com/47745785/114269552-ccd59300-9a42-11eb-843f-db5907852417.png" />
</p>

<br>

### 회사, 시세, 코스피 수정

<p align="center">
<img alt="character" width="1500" src="https://user-images.githubusercontent.com/47745785/114269597-fb536e00-9a42-11eb-9d9e-eec5aa9a72b0.png" />
</p>

<br>

### 조회 기능

* 회사들의 시세들 중 최고와 최저 시세를 조회

<p align="center">
<img alt="character" width="700" src="https://user-images.githubusercontent.com/47745785/114269678-55543380-9a43-11eb-9cd3-865b4c8e5ee4.png" />
</p>

* 두 회사의 시세정보 비교

<p align="center">
<img alt="character" width="800" src="https://user-images.githubusercontent.com/47745785/114269723-7e74c400-9a43-11eb-858b-68dc1af217e5.png" />
</p>

* 회사별로 종가의 평균과 최대 종가 조회

<p align="center">
<img alt="character" width="800" src="https://user-images.githubusercontent.com/47745785/114269785-ba0f8e00-9a43-11eb-822b-c364e83e7fc0.png" />
</p>

* 날짜별 코스피 조회, 최대 및 최저 코스피 조회

<p align="center">
<img alt="character" width="800" src="https://user-images.githubusercontent.com/47745785/114269887-4e79f080-9a44-11eb-86f3-b03d2d4313cd.png" />
</p>

## 🖋 Author

👤 **박인효**

* Mail: [inhyopark122@gmail.com](mailto:inhyopark122@gmail.com)
* GitHub: [@PARKINHYO](https://github.com/PARKINHYO)

👤 **이진재**

* Mail: [leejinjae7@gmail.com](mailto:leejinjae7@gmail.com)
* GitHub: [@loftmain](https://github.com/loftmain)

## 📝 License

Copyright © 2021 [박인효](https://github.com/parkinhyo).<br/>
This project is [MIT](https://github.com/PARKINHYO/FinanceDB/blob/master/LICENSE) licensed.
***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_