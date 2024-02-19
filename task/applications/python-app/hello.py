from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_tiacloud():
    return 'Hello Tiacloud 2024'

if __name__ == '__main__':
    app.run(debug=True, port=2024)
