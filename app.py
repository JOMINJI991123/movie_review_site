from flask import Flask, render_template, request, jsonify
import requests
import subprocess
import pymysql

#MySQL connection
try:
    db = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='movie_site', charset='utf8')
    print("successful connection")
except pymysql.MySQLError as e:
    print(f"failed connection {e}")

app = Flask(__name__)

#main html
@app.route("/", methods=['GET','POST'])
def main1():
    return render_template('main.html')

#main html
@app.route("/main.html", methods=['GET','POST'])
def main2():
    return render_template('main.html')

#movie1 html
@app.route("/movie1.html", methods=['GET','POST'])
def movie1():
    if request.method == 'POST':
        return handle_review_request(1) 
    return render_template('movie1.html')

#movie2 html
@app.route("/movie2.html", methods=['GET','POST'])
def movie2():
    if request.method == 'POST':
        return handle_review_request(2) 
    return render_template('movie2.html')

#movie3 html
@app.route("/movie3.html", methods=['GET','POST'])
def movie3():
    if request.method == 'POST':
        return handle_review_request(3) 

    return render_template('movie3.html')

#movie4 html
@app.route("/movie4.html", methods=['GET','POST'])
def movie4():
    if request.method == 'POST':
        return handle_review_request(4) 

    return render_template('movie4.html')

#movie5 html
@app.route("/movie5.html", methods=['GET','POST'])
def movie5():
    if request.method == 'POST':
        return handle_review_request(5) 

    return render_template('movie5.html')

#전체리뷰 로드해오기
@app.route("/get_reviews/<movie_num>", methods=['GET'])
def get_reviews(movie_num):
    # 데이터베이스에서 모든 리뷰 가져오기
    cursor = db.cursor()
    sql = f"SELECT movie_star, movie_review FROM movie{movie_num}"
    cursor.execute(sql)
    datas = cursor.fetchall()
    cursor.close()

    # 클라이언트에게 데이터 응답하기
    return [{'star':data[0],'review':data[1]} for data in datas]

# 데이터베이스에 리뷰데이터 저장
def save_review(page_num ,review_text):
    cursor = db.cursor()
    sql = f"INSERT INTO movie{page_num} (movie_review, movie_star) VALUES (%s,%s);"
    print(page_num)
    cursor.execute(sql,(review_text,0))
    db.commit()
    cursor.close()

# 데이터베이스에서 별점데이터 읽어오기
def get_star(page_num):
    cursor = db.cursor()
    sql = f"SELECT movie_star FROM movie{page_num} ORDER BY id DESC LIMIT 1;"
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    return result[0]

# 자동 별점 예측 전체 코드
def handle_review_request(page_num):
        print(page_num)
        # html에서 데이터 전달받기
        post_data = request.json

        #데이터베이스에 리뷰데이터 저장
        save_review(page_num,post_data['data'])

        # 리뷰데이터 별점 예측 실행
        result = subprocess.run(['C:\\Users\\UserK\\Desktop\\deeplearning_project\\movie_review_site\\venvmovie\\Scripts\\python.exe', 'predict.py',str(page_num)], stdout=subprocess.PIPE, check=True)

        # 데이터베이스에서 별점데이터 읽어오기
        star = get_star(page_num)

        # 클라이언트에게 응답
        response_data = {'star':star}
        return jsonify(response_data)

