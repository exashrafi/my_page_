from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        response = make_response(redirect(url_for('welcome')))
        response.set_cookie('name', name)
        response.set_cookie('email', email)
        return response
    return render_template('index.html')


@app.route('/welcome')
def welcome():
    name = request.cookies.get('name')
    if not name:
        return redirect(url_for('welcome'))
    return render_template('welcome.html', name=name)


@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('welcome')))
    response.delete_cookie('name')
    response.delete_cookie('email')
    return response


if __name__ == '__main__':
    app.run(debug=True)
