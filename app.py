from flask import Flask, render_template, request
import socket

app = Flask(__name__)

def detect_spam(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(('192.168.60.246', 8889))  # Replace '192.168.x.x' with the server's local IP
        client.send(message.encode())
        response = client.recv(1024).decode()
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_spam', methods=['POST'])
def check_spam():
    message = request.form['message']
    response = detect_spam(message)
    return render_template('result.html', message=message, response=response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
