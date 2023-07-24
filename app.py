
import os
import sqlite3
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

DB_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'example.db')

def create_table():
    # SQLite 데이터베이스 연결
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # 데이터베이스에 테이블 생성
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    # 변경사항 저장 및 연결 종료
    conn.commit()
    conn.close()


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    diary = data.get('diary')

    if not name or not email or not diary:
        return jsonify({'message': 'Name, email, and diary are required.'}), 400

    # SQLite 데이터베이스 연결
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # 새로운 사용자 추가
    cursor.execute('INSERT INTO users (name, email, diary) VALUES (?, ?, ?)', (name, email, diary))

    # 변경사항 저장 및 연결 종료
    conn.commit()
    conn.close()

    return jsonify({'message': 'User added successfully.'})


@app.route('/show_users')
def show_users():
    # SQLite 데이터베이스 연결
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # 사용자 정보 조회
    cursor.execute('SELECT name, email, diary FROM users')
    users = cursor.fetchall()

    # 연결 종료
    conn.close()

    # 템플릿을 사용하여 사용자 정보를 테이블로 렌더링
    return jsonify({'users': users})


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/<username>', methods=['GET'])
def hello_world(username):
    
    return '내 이름은 '+username+' 입니다.'


@app.route('/Lee/fee')
def hello_world_():
    return 'hello_asdasd'