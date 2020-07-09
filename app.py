from flask import Flask, render_template, redirect

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

@app.route('/resume')
def resume():
    return redirect('./static/resume.pdf')
    # https://stackoverflow.com/questions/18281433/flask-handling-a-pdf-as-its-own-page
    
if __name__ == '__main__':
    app.debug = True
    app.run()
