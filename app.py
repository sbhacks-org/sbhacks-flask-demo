from flask import Flask
from flask import render_template, request
from utils import find_zodiac_sign, get_magic_8_ball_response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', base_url=request.url)

@app.route('/zodiac', methods=['GET'])
def zodiac():
    return render_template('zodiac.html')

@app.route('/zodiac_result', methods=['GET', 'POST'])
def zodiac_result():
    day = int(request.form['day'])
    month = int(request.form['month'])
    zodiac_sign = find_zodiac_sign(day, month)

    return render_template('zodiac_result.html', day=day, month=month, zodiac_sign=zodiac_sign)

@app.route('/magic_8_ball', methods=['GET'])
def magic_8_ball():
    return render_template('magic_8_ball.html')

@app.route('/magic_8_ball_result', methods=['GET', 'POST'])
def magic_8_ball_result():
    question = request.form['question']
    magic_8_ball_response = get_magic_8_ball_response()
    return render_template('magic_8_ball_result.html', question=question, magic_8_ball_response=magic_8_ball_response)
