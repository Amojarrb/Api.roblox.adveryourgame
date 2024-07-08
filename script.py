from flask import Flask, request, jsonify

app = Flask(__name__)

# Función para obtener información del usuario de Roblox
def obtener_info_usuario_roblox(username):
    # Simulación de datos (reemplaza con tu lógica real para obtener datos de Roblox)
    # En este caso, se devuelve un objeto JSON simulado
    if username == "usuario_ejemplo":
        return {
            "Username": "usuario_ejemplo",
            "Id": 123456789,
            "Nombre completo": "Usuario de Ejemplo"
        }
    else:
        return {"error": f"No se encontró información para el usuario '{username}'"}

# Ruta para obtener información del usuario de Roblox
@app.route('/api/obtener_info_usuario_roblox', methods=['GET'])
def api_obtener_info_usuario_roblox():
    username = request.args.get('username')
    info_usuario = obtener_info_usuario_roblox(username)
    return jsonify(info_usuario)

if __name__ == '__main__':
    app.run(debug=True)
