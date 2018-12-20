from flask import Flask, render_template, request
from bs4 import BeautifulSoup as bs
from faker import Faker
import random
import csv


app = Flask(__name__)
info = {}
info2 = []
a = open('matchmaker.csv','w',encoding='utf-8')
stack = csv.writer(a)
stack.writerow(['name1','name2'])
a.close()


#'/': 사용자의 이름을 입력 받습니다.
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/pastlife')
def pastlife():
    name = request.args.get('name')
    fake = Faker('ko_KR')
    job = fake.job()
    
    if name in info:
        job = info[name]
        print(info)
    else:
        info[name] = job
        
    return render_template('pastlife.html', name = name, job = job )
    
#'/pastlife' : 사용자의 (랜덤으로 생성된) 직업을 보여준다.

@app.route('/matchmaker')
def matchmaker():
    name1 = request.args.get('name1')
    name2 = request.args.get('name2')
    percent = random.sample(range(1,101),1)
    # random.randint(1,100)
    
    if (name1,name2) in info:
        percent = info[name1,name2]
    else:
        info[name1,name2]=percent
        info2.append((name1,name2))
        f = open('matchmaker.csv','a',encoding='utf-8')
        new = csv.writer(f)
        new.writerow([name1,name2])
        f.close
    
    return render_template('matchmaker.html', name1 = name1, name2 = name2, percent = percent)
    
@app.route('/admin')
def admin():
    
    with open('matchmaker.csv','r',encoding='utf-8') as f:
        stack = csv.reader(f)
        for line in stack:
            print(line)
    
    return render_template('admin.html',info=info,info2=info2)