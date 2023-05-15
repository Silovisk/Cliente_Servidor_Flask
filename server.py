from flask import Flask, request

app = Flask(__name__)

@app.route('/screenshot', methods=['POST'])
def receive_screenshot():
    screenshot = request.files['screenshot']
    screenshot.save('screenshot.png')
    return 'Screenshot received successfully!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
