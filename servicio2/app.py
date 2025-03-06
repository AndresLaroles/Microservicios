from flask import Flask, jsonify
import requests

app2 = Flask(__name__)

BASE_URL = 'https://www.el-tiempo.net/api/json/v2/provincias/'

@app2.route('/<int:municipioid>/meteo', methods=['GET'])
def get_meteo(municipioid):
    try:
        # Definir el ID de la provincia y municipio
        provincia_id = "18"
        municipio_id = municipioid  # Utilizamos el municipioid pasado en la URL

        # Construir la URL completa
        url = f'{BASE_URL}{provincia_id}/municipios/{municipio_id}'

        # Hacer la solicitud a la API
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            # Imprimir los datos completos para depuración
            print("Datos completos de la respuesta:", data)

            # Extraemos los datos meteorológicos de acuerdo con la estructura del JSON
            meteo_data = {
                'temperatura_max': data.get('temperaturas', {}).get('max', 'No disponible'),
                'temperatura_min': data.get('temperaturas', {}).get('min', 'No disponible'),
                'humedad': data.get('humedad', 'No disponible'),
                'viento': data.get('viento', 'No disponible'),
                'precipitacion': data.get('precipitacion', 'No disponible'),
                'lluvia': data.get('lluvia', 'No disponible')
            }

            return jsonify(meteo_data), 200
        else:
            print(f"Error al obtener datos: {response.status_code}")
            print(response.text)
            return jsonify({'error': 'No se pudo obtener los datos del tiempo'}), 500

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Error al conectarse a la API: {str(e)}'}), 500

if __name__ == '__main__':
    app2.run(port=5001)
