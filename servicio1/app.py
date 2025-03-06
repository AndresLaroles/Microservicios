from flask import Flask, jsonify
import json

app1 = Flask(__name__)

with open("municipio.json", "r", encoding="utf-8") as file:
    municipio_data = json.load(file)

@app1.route('/<int:municipioid>/geo', methods=['GET'])
def get_geo(municipioid):

    if municipio_data.get("municipioid") == municipioid:
        return jsonify(municipio_data), 200
    else:
        return jsonify({"error": "Municipio no encontrado"}), 404

if __name__ == '__main__':
    app1.run(port=5000, debug=True)
