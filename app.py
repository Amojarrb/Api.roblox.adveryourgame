from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'Roblox User Info API. Use /userinfo?userid=<UserID> to get user info.'

@app.route('/userinfo', methods=['GET'])
def userinfo():
    user_id = request.args.get('userid')
    if not user_id:
        return jsonify({'error': 'User ID not provided'}), 400

    url = f'https://users.roblox.com/v1/users/{user_id}'
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch user info'}), response.status_code

    user_info = response.json()

    # Renderiza el template HTML con la información del usuario
    return render_template('userinfo.html', user_info=user_info)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
