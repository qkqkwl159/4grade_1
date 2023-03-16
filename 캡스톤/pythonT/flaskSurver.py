from flask import Flask

app = Flask(__name__)

user =  '''{
    "id":1,
    "user":"qkqkwl159",
    "pwd":"12345",
    "email":"qkqkwl159@naver.com"
    }
    '''
@app.route('/')
def home():
    return 'This is home!'
@app.route('/user')
def Udata():
    return user


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
