from flask import Flask, jsonify
import requests

app4 = Flask(__name__)

# URLs base de cada servicio:
SERVICIO1_URL = "http://localhost:5000"  # Servicio de geo
SERVICIO2_URL = "http://localhost:5001"  # Servicio de meteo
SERVICIO3_URL = "http://localhost:5002"  # Servicio de demo

@app4.route('/<int:municipioid>/<path:params>', methods=['GET'])
def get_combined(municipioid, params):
    # Separa todos los parámetros que vienen en la URL
    param_list = params.split('/')
    result = {}

    # Itera sobre cada parámetro y llama al servicio correspondiente
    for param in param_list:
        if param == "geo":
            try:
                geo_resp = requests.get(f"{SERVICIO1_URL}/{municipioid}/geo")
                if geo_resp.status_code == 200:
                    result["geo"] = geo_resp.json()
                else:
                    result["geo"] = {"error": "Error al obtener datos geo"}
            except Exception as e:
                result["geo"] = {"error": str(e)}
        elif param == "meteo":
            try:
                meteo_resp = requests.get(f"{SERVICIO2_URL}/{municipioid}/meteo")
                if meteo_resp.status_code == 200:
                    result["meteo"] = meteo_resp.json()
                else:
                    result["meteo"] = {"error": "Error al obtener datos meteo"}
            except Exception as e:
                result["meteo"] = {"error": str(e)}
        elif param == "demo":
            try:
                demo_resp = requests.get(f"{SERVICIO3_URL}/{municipioid}/demo")
                if demo_resp.status_code == 200:
                    result["demo"] = demo_resp.json()
                else:
                    result["demo"] = {"error": "Error al obtener datos demo"}
            except Exception as e:
                result["demo"] = {"error": str(e)}
        else:
            # Si se pasa un parámetro no reconocido, lo anotamos
            result[param] = {"error": "Parámetro no reconocido"}

    if not result:
        return jsonify({"error": "No se proporcionaron parámetros válidos"}), 400

    return jsonify(result), 200

if __name__ == '__main__':
    app4.run(port=5003, debug=True)
