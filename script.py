import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Función para obtener juegos del usuario con ID 1 de Roblox
def obtener_juegos_usuario_roblox():
    url = "https://games.roblox.com/v2/users/1/games?accessFilter=2&limit=10&sortOrder=Asc"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', [])
        else:
            return {"error": f"Error al obtener los juegos. Código de estado: {response.status_code}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Error de conexión: {str(e)}"}

# Ruta para obtener juegos del usuario con ID 1 de Roblox
@app.route('/api/obtener_juegos_usuario_roblox', methods=['GET'])
def api_obtener_juegos_usuario_roblox():
    juegos = obtener_juegos_usuario_roblox()
    return jsonify(juegos)

if __name__ == '__main__':
    app.run(debug=True)
