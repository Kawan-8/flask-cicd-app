from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "🚀 CI/CD with Flask and Docker is working!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
