from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Nikhil! Flask App Running 🚀"

@app.route('/about')
def about():
    return "This app is for Docker + CI/CD"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)