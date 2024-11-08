from flask import Flask, jsonify, send_file
import qrcode
import os

app = Flask(__name__)

@app.route('/send/<data>')
def home(data):
    if not search_files('./images', f'{data}.png'):
        img = qrcode.make(data)
        img.save(f'./images/{data}.png')
        return send_file(f'./images/{data}.png', mimetype='image/png')

    return send_file(f'./images/{data}.png', mimetype='image/png')

def search_files(directory, filename):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return True
    return False

if __name__ == '__main__':
    app.run(debug=True)