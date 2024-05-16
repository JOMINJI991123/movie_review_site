import urllib.request
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Bidirectional, LSTM, Dense, Dropout

input_review=""

try:
    with open("review.txt", 'r', encoding='utf-8') as f:
        input_review = f.read()
    print("파일을 성공적으로 읽었습니다.")
except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다.")
except IOError as e:
    print(f"파일 읽기 중 오류가 발생했습니다: {e}")

# 모델, 토크나이저 로드해오기
with open("model_tokenizer.pkl", "rb") as f:
    model, tokenizer = pickle.load(f)    

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
 
# 결과 출력
predicted_rating, confidence = predict_sentiment(input_review)

with open('rating.txt', 'w', encoding='utf-8') as f:
    f.write(str(predicted_rating))





