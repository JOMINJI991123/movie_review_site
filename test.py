import os
import urllib.request
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Bidirectional, LSTM, Dense, Dropout

    
# 데이터 다운로드 URL
url = "https://github.com/e9t/nsmc/raw/master/ratings_train.txt"


# 데이터 다운로드
download_dir = "naver_movie_reviews"
os.makedirs(download_dir, exist_ok=True)
data_file_path = os.path.join(download_dir, "ratings_train.txt")

urllib.request.urlretrieve(url, data_file_path)

# 데이터 전처리
with open(data_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

reviews = [line.split('\t')[1] for line in lines[1:]]  # 리뷰 텍스트
labels = [int(line.split('\t')[2]) for line in lines[1:]]  # 긍정(1) 또는 부정(0) 레이블

print(len(reviews))