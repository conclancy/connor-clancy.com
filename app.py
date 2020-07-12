from flask import Flask, render_template, redirect, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/style.css')
def style():
    return url_for('static', 'style.css')
    # required for browser to find the css file on the server
    # https://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files

@app.route('/resume')
def resume():
    return redirect('./static/resume.pdf')
    # https://stackoverflow.com/questions/18281433/flask-handling-a-pdf-as-its-own-page

if __name__ == '__main__':
    app.static_folder = 'static'
    app.debug = True
    app.run()
