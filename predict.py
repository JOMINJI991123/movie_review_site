import urllib.request
import numpy as np
import pickle
import pymysql
import sys
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Bidirectional, LSTM, Dense, Dropout

review_text=""
page_num = 0

# 리뷰데이터 불러오기
def get_review(page_num):
    cursor = db.cursor()
    sql = f"SELECT movie_review, id FROM movie{page_num} ORDER BY id DESC LIMIT 1;"
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    return result[0], result[1]

# 별점데이터 저장하기
def save_star(id,page_num,star):
    cursor = db.cursor()
    sql = f"UPDATE movie{page_num} SET movie_star = %s WHERE id=%s"
    cursor.execute(sql,(star,id))
    db.commit()
    cursor.close()

# 예측 함수 정의
def predict_sentiment(review_text):
    sequence = tokenizer.texts_to_sequences([review_text])
    padded_sequence = pad_sequences(sequence, maxlen=50, padding='post', truncating='post')

    # 예측
    prediction = model.predict(padded_sequence)[0, 0]

    # 별점 예측 (가정: 1~5의 정수)
    rating = round(prediction * 4) + 1

    # 긍정 리뷰를 판단하는 기준을 조정하여 높은 신뢰도 설정
    confidence = prediction if rating >= 4 else 1 - prediction

    return rating, confidence


# 페이지 넘버 인자로 불러오기
page_num = sys.argv[1]

# 모델, 토크나이저 로드해오기
with open("model_tokenizer.pkl", "rb") as f:
    model, tokenizer = pickle.load(f)   

#MySQL connection
try:
    db = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='movie_site', charset='utf8')
    print("successful connection")
except pymysql.MySQLError as e:
    print(f"failed connection {e}")

# 리뷰데이터 조회
review_text, review_id = get_review(page_num)

 # 검증결과
predicted_rating, confidence = predict_sentiment(review_text)

save_star(review_id,page_num,predicted_rating)








