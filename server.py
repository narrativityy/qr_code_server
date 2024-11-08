from flask import Flask, jsonify, send_file
import qrcode
import os

app = Flask(__name__)

@app.route('/send/<data>')
def home(data):
    """
    Generate a QR code with the given data, save it to images/, and
    send it as a response.
    """
    if not search_files('./images', f'{data}.png'):
        # Generate a QR code
        img = qrcode.make(data)
        # Save the QR code to images/
        img.save(f'./images/{data}.png')
        # Send the QR code as a response
        return send_file(f'./images/{data}.png', mimetype='image/png')

    # If the QR code already exists, just send the existing one
    return send_file(f'./images/{data}.png', mimetype='image/png')

def search_files(directory, filename):
    """
    Check if a file exists in the given directory.

    Args:
        directory (str): The directory path to search in.
        filename (str): The name of the file to search for.

    Returns:
        bool: True if the file is found, False otherwise.
    """
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        # Check if the filename is in the current directory's files
        if filename in files:
            return True
    # Return False if the file was not found in any directory
    return False

if __name__ == '__main__':
    app.run(debug=True)