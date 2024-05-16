from flask import Flask, render_template, request, jsonify
import requests
import nbformat
import subprocess

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
        # html에서 데이터 전달받기
        post_data = request.json


        # review데이터 메모장에 적기
        with open('review.txt','w',encoding='utf-8') as f:
            f.write(post_data['data'])
        
        # 파이썬 파일 실행하기
        result = subprocess.run(['python', 'predict.py'], stdout=subprocess.PIPE, check=True)

        # 별점 데이터 메모장에서 읽어오기
        with open('rating.txt','r',encoding='utf-8') as f:
            rating = f.read()

        # 클라이언트에게 응답
        response_data = {'rating':rating}
        return jsonify(response_data)

    return render_template('movie1.html')

#movie2 html
@app.route("/movie2.html", methods=['GET','POST'])
def movie2():
    if request.method == 'POST':
        # html에서 데이터 전달받기
        post_data = request.json


        # review데이터 메모장에 적기
        with open('review.txt','w',encoding='utf-8') as f:
            f.write(post_data['data'])
        
        # 파이썬 파일 실행하기
        result = subprocess.run(['python', 'predict.py'], stdout=subprocess.PIPE, check=True)

        # 별점 데이터 메모장에서 읽어오기
        with open('rating.txt','r',encoding='utf-8') as f:
            rating = f.read()

        # 클라이언트에게 응답
        response_data = {'rating':rating}
        return jsonify(response_data)

    return render_template('movie2.html')

#movie3 html
@app.route("/movie3.html", methods=['GET','POST'])
def movie3():
    if request.method == 'POST':
        # html에서 데이터 전달받기
        post_data = request.json


        # review데이터 메모장에 적기
        with open('review.txt','w',encoding='utf-8') as f:
            f.write(post_data['data'])
        
        # 파이썬 파일 실행하기
        result = subprocess.run(['python', 'predict.py'], stdout=subprocess.PIPE, check=True)

        # 별점 데이터 메모장에서 읽어오기
        with open('rating.txt','r',encoding='utf-8') as f:
            rating = f.read()

        # 클라이언트에게 응답
        response_data = {'rating':rating}
        return jsonify(response_data)

    return render_template('movie3.html')

#movie4 html
@app.route("/movie4.html", methods=['GET','POST'])
def movie4():
    if request.method == 'POST':
        # html에서 데이터 전달받기
        post_data = request.json


        # review데이터 메모장에 적기
        with open('review.txt','w',encoding='utf-8') as f:
            f.write(post_data['data'])
        
        # 파이썬 파일 실행하기
        result = subprocess.run(['python', 'predict.py'], stdout=subprocess.PIPE, check=True)

        # 별점 데이터 메모장에서 읽어오기
        with open('rating.txt','r',encoding='utf-8') as f:
            rating = f.read()

        # 클라이언트에게 응답
        response_data = {'rating':rating}
        return jsonify(response_data)

    return render_template('movie4.html')

#movie5 html
@app.route("/movie5.html", methods=['GET','POST'])
def movie5():
    if request.method == 'POST':
        # html에서 데이터 전달받기
        post_data = request.json


        # review데이터 메모장에 적기
        with open('review.txt','w',encoding='utf-8') as f:
            f.write(post_data['data'])
        
        # 파이썬 파일 실행하기
        result = subprocess.run(['python', 'predict.py'], stdout=subprocess.PIPE, check=True)

        # 별점 데이터 메모장에서 읽어오기
        with open('rating.txt','r',encoding='utf-8') as f:
            rating = f.read()

        # 클라이언트에게 응답
        response_data = {'rating':rating}
        return jsonify(response_data)

    return render_template('movie5.html')

# if __name__ == '__main__':
#     app.run(debug=True)
