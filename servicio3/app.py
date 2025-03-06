from flask import Flask, jsonify
import json

app3 = Flask(__name__)

with open("municipio.json", "r", encoding="utf-8") as file:
    municipio_data = json.load(file)

@app3.route('/<int:municipioid>/demo', methods=['GET'])
def get_demo(municipioid):

    return jsonify(municipio_data), 200

if __name__ == '__main__':

    app3.run(port=5002, debug=True)
