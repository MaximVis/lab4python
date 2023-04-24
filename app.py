from flask import Flask, render_template, request
import math


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/qb', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        num_1 = int(request.form.get('num_1'))
    return render_template('index.html', ans=num_1**3)


@app.route('/bq', methods=['post', 'get'])
def form1():
    if request.method == 'POST':
        num_2 = int(request.form.get('num_2'))
        num_3 = int(request.form.get('num_3'))
    return render_template('index.html', ans1=num_2*num_3)


@app.route('/prizma', methods=['post', 'get'])
def form2():
    if request.method == 'POST':
        num_7 = int(request.form.get('num_7'))
        num_8 = int(request.form.get('num_8'))
    return render_template('index.html', ans3=num_7*num_8)


@app.route('/pyramid', methods=['post', 'get'])
def form3():
    if request.method == 'POST':
        num_9 = int(request.form.get('num_9'))
        num_10 = int(request.form.get('num_10'))
        num_11 = int(request.form.get('num_11'))
    return render_template('index.html', ans4=round(1/3*num_9*num_10, num_11))


@app.route('/cilindr', methods=['post', 'get'])
def form4():
    if request.method == 'POST':
        num_12 = int(request.form.get('num_12'))
        num_13 = int(request.form.get('num_13'))
        num_14 = int(request.form.get('num_14'))
    return render_template('index.html', ans5=round((math.pi*num_13**2)*num_12, num_14))


@app.route('/shar', methods=['post', 'get'])
def form5():
    if request.method == 'POST':
        num_15 = int(request.form.get('num_15'))
        num_16 = int(request.form.get('num_16'))
    return render_template('index.html', ans6=round(4/3*math.pi*num_15**3,num_16))