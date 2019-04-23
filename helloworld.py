from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello world</h1>'


r'''
    动态路由参数：name需要动态输入
'''
    # TODO 书签1
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)
