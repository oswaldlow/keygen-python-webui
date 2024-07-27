import base64
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

app = Flask(__name__)
CORS(app)

# 这些答辩，能跑起来就已经赢了，别太在意代码质量.jpg
MagicKey = b"41100c93a65cfb71d5b0672c0d60d7ec"
MagicKey2 = b"70ba69d67bf7e61e17ac565c6093a325"[:16]

def create_cipher(key, iv):
    return Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())

def MagicKeyEncode(data):
    cipher = create_cipher(MagicKey, MagicKey2)
    encryptor = cipher.encryptor()
    return encryptor.update(data) + encryptor.finalize()

@app.route('/encode', methods=['POST'])
def encode():
    json_data = request.json
    json_str = json.dumps(json_data).encode()
    encoded = MagicKeyEncode(json_str)
    return jsonify({"encoded": base64.b64encode(encoded).decode()})

if __name__ == '__main__':
    app.run(debug=True)
