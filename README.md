# News Article Crawling & News Chatbot


## Short Description
- Scrapy를 이용하여 네이버 뉴스 기사를 카테고리별로 크롤링하며, crontab을 통해 크롤링 자동화를 구축한다.
- 크롤링한 데이터는 중복기사 제거 후 MongoDB에 저장되며, Discord 챗봇과 연동시켜 챗봇을 통해 원하는 뉴스 기사 또는 워드클라우드 이미지를 받아볼 수 있다.


## Built With
- [서기현](https://github.com/seogihyun): 
- [유승균]():
- [이기중]():
- [김종찬]():


## Getting Started

You will require Python 3 and the following libraries


## Installation

    - pip install -U scikit-learn

    - pip install Scrapy

    - pip install -U discord.py
    
    - pip install pymongo
    
    - pip install -U nltk
    
    - pip install asyncio
    
    - pip install wordcloud
    
    - pip install konlpy


### Prerequisites

* import requests
* import scrapy
* import pandas as pd
* import pymongo
* import discord
* import asyncio
* import nltk
* from wordcloud import WordCloud
* from scrapy.http import TextResponse
* from sklearn.feature_extraction.text import TfidfVectorizer
* from sklearn.feature_extraction.text import CountVectorizer
* from sklearn.metrics.pairwise import linear_kernel
* from IPython.display import Image 
* from discord.ext import commands


### Dataset

* 네이버 뉴스기사 2년치 크롤링 데이터

      - 카테고리 : IT, 생활문화, 경제, 사회
      
      - 기간 : 2019.01.01 ~ 2020.11.29   
      
* 2020.11.30 ~ 2020.12.04 - 데이터 용량 과부하로 인한 수집 불가, 추후 다른 PC로 대체

* 네이버 뉴스기사 daily 크롤링 데이터

      - 카테고리 : IT, 생활문화, 경제, 사회
      
      - 기간 : 2020.12.05 ~ 2020.12.10(프로젝트 종료)


## Crawling Project Progress

* 1. 데이터 수집 : 네이버 뉴스기사 크롤링(scrapy)  +  중복 기사 제거(Cosine Similarity)  +  daily 크롤링 자동화(crontab)
* 2. 데이터 저장 및 관리 : .csv 저장(2년치 크롤링 데이터)  +  MongoDB 저장(daily 크롤링)
* 3. 챗봇 개발 : 자연어처리(Mecab)  +  Stop word  +  WordCloud 


## Project Result




### 느낌점 & 추후 연구 및 연구방향

* 느낀점 

      - 각 사이트마다 다양한 방식으로 크롤링을 하면서 크롤링 방식마다 크고 작은 속도차이를 경험해볼 수 있었음.
      - 챗봇을 만들게 되면서 아직 배우지 않았던 내용들을 스스로 학습하며 임무를 완수하는 재미가 있었음.
      - 다양한 변수들로 인해 계획했던 것보다 시간이 오래걸려 시간 조절이 어려웠음.
      - 계획을 세울 때 좀 더 세분화하여 작업 소요시간 파악과 체계적인 계획수립으로 효율적인 시간활용이 되야할 것 같음

* 추후 연구 및 연구 방향 

      - 자연어처리에서 불용성단어 리스트는 주기적으로 업데이트가 필요하며, 불용어단어 처리 시 처리 기준을 명확히 할 필요가 있음
      - 코사인 유사도를 이용한 효율적인 중복 기사 제거에 대해 추가적인 연구가 필요함.
      - 개인 맞춤형 추천 알고리즘에 대한 연구도 추후 진행할 예정임.
      - 크롤링한 데이터 저장 시 메모리 경량화 방법에 대한 연구가 필요함.


### License

* MIT License
