from flask import Flask, render_template, request, jsonify
import requests
import subprocess
import pymysql
import os

#MySQL connection
try:
    db = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='movie_site', charset='utf8')
    print("successful connection")
except pymysql.MySQLError as e:
    print(f"failed connection {e}")

app = Flask(__name__)

# 영화 이미지 갯수
movie_images_path = "static/images"
files = os.listdir(movie_images_path)
movie_images_count = len(files)

#main html
@app.route("/", methods=['GET','POST'])
def index():
    cursor = db.cursor(pymysql.cursors.DictCursor)  # 결과를 딕셔너리 형태로 받기
    cursor.execute("SELECT * FROM movies")  # movies 테이블에서 모든 영화 데이터 가져오기
    movies = cursor.fetchall()  # 데이터 가져오기
    cursor.close()
    
    return render_template('main.html', movies=movies)  # movies 데이터를 템플릿에 전달


#main html
@app.route("/main.html", methods=['GET','POST'])
def main():
    cursor = db.cursor(pymysql.cursors.DictCursor)  # 결과를 딕셔너리 형태로 받기
    cursor.execute("SELECT * FROM movies")  # movies 테이블에서 모든 영화 데이터 가져오기
    movies = cursor.fetchall()  # 데이터 가져오기
    cursor.close()
    
    return render_template('main.html', movies=movies)  # movies 데이터를 템플릿에 전달


#detail html
@app.route("/movie<movie_id>.html", methods=['GET','POST'])
def detail(movie_id):
    if request.method == 'POST':
        return handle_review_request(movie_id) 
    
    cursor = db.cursor(pymysql.cursors.DictCursor)  # 결과를 딕셔너리 형태로 받기
    cursor.execute(f"SELECT * FROM movies WHERE id={movie_id}")  # movies 테이블에서 모든 영화 데이터 가져오기
    movie_info = cursor.fetchone()  # 데이터 가져오기
    cursor.close()
    
    return render_template(f'detail.html', movie_info = movie_info)




#전체리뷰 로드해오기
@app.route("/get_reviews/<movie_id>", methods=['GET'])
def get_reviews(movie_id):
    # 데이터베이스에서 모든 리뷰 가져오기
    cursor = db.cursor()
    sql = f"SELECT comment_star, comment_review FROM comment WHERE movie_num = {movie_id}"
    cursor.execute(sql)
    datas = cursor.fetchall()
    cursor.close()

    # 클라이언트에게 데이터 응답하기
    return [{'star':data[0],'review':data[1]} for data in datas]

# 데이터베이스에 리뷰데이터 저장
def save_review(movie_id ,review_text):
    cursor = db.cursor()
    sql = f"INSERT INTO comment (movie_num, comment_review, comment_star) VALUES (%s,%s,%s);"
    print(movie_id)
    cursor.execute(sql,(movie_id,review_text,0))
    db.commit()
    cursor.close()

# 데이터베이스에서 별점데이터 읽어오기
def get_star(page_num):
    cursor = db.cursor()
    sql = f"SELECT comment_star FROM comment ORDER BY id DESC LIMIT 1;"
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    return result[0]

# 자동 별점 예측 전체 코드
def handle_review_request(movie_id):
        print(movie_id)
        # html에서 데이터 전달받기
        post_data = request.json

        #데이터베이스에 리뷰데이터 저장
        save_review(movie_id,post_data['data'])

        # 리뷰데이터 별점 예측 실행
        result = subprocess.run(['C:\\Users\\UserK\\Desktop\\deeplearning_project\\movie_review_site\\venvmovie\\Scripts\\python.exe', 'predict.py',str(movie_id)], stdout=subprocess.PIPE, check=True)

        # 데이터베이스에서 별점데이터 읽어오기
        star = get_star(movie_id)

        # 클라이언트에게 응답
        response_data = {'star':star}
        return jsonify(response_data)

