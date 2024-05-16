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

# 토큰화와 전처리
tokenizer = Tokenizer(num_words=10000, oov_token='<OOV>')
tokenizer.fit_on_texts(reviews)

sequences = tokenizer.texts_to_sequences(reviews)
padded_sequences = pad_sequences(sequences, maxlen=50, padding='post', truncating='post')

# 데이터를 훈련 세트와 검증 세트로 나눔
X_train, X_val, y_train, y_val = train_test_split(padded_sequences, labels, test_size=0.2, random_state=42)

# Convert lists to numpy arrays
y_train = np.array(y_train)
y_val = np.array(y_val)

# 모델 생성
model = Sequential()
model.add(Embedding(input_dim=10000, output_dim=500))
model.add(Bidirectional(LSTM(50)))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

# 모델 컴파일 및 학습 (클래스 가중치 추가)
class_weight = {0: 1, 1: len(y_train) / sum(y_train)}
# 모델 컴파일 및 학습 (에포크 수 증가)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=1, batch_size=32, validation_data=(X_val, y_val))

with open("model_tokenizer.pkl", "wb") as f:
    pickle.dump((model, tokenizer), f)






