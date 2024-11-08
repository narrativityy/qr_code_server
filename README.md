# QR Code Generator API
==========================

A simple API built with Flask that generates QR codes based on input data.

## Endpoints

### `/qr/<data>`

Generate a QR code with the given `data` and return it as an image.

* `data`: The input data to encode in the QR code.

## Usage

1. Clone the repository and install the required dependencies.
2. Run the Flask app using `python server.py`.
3. Send a GET request to `/qr/<data>` to generate a QR code.

Example: `curl http://localhost:5000/qr/https://github.com/your-username/your-repo`

## Notes

* The generated QR codes are saved in the [images/](cci:7://file:///Users/jakecrowley/Desktop/qr_code_server/images:0:0-0:0) directory.
* If a QR code with the same data already exists, the existing one will be returned instead of generating a new one.

[CursorSurroundingLines]
</CursorSurroundingLines>
