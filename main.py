from flask import Flask, render_template, request
import jyserver.Flask as jsf

app = Flask(__name__)


@jsf.use(app)
class App:
    def __init__(self): 
        self.text = ""
    


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    return text


@app.route('/send')
def send():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)