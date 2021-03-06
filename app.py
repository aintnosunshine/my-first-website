from flask import Flask, render_template, redirect, url_for, request
from flask_scss import Scss
app = Flask(__name__)
Scss(app, static_dir='my-first-website/static/css', asset_dir='my-first-website/assets/scss')

@app.route('/', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'atlassian' or request.form['password'] != '':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('show_success'))
    return render_template('login.html', error=error)

@app.route('/success')
def show_success():
    return render_template('') #the file was changed
if __name__ == '__main__':
    app.run()

