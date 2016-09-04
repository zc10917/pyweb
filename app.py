from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_formweqeq():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signinqewqe():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return render_template('signin.html',username = request.form['username'])
    return '<h3>Bad username or password.</h3>'


if __name__ == '__main__':
    app.run()
