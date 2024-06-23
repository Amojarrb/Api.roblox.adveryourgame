import requests

def main():
    url = "https://games.roblox.com/v2/users/123456789/games?accessFilter=2&limit=10&sortOrder=Asc"

    try:
        # Realizar la solicitud HTTP GET
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            print(f"Contenido de la URL {url}:")
            print(response.json())  # Mostrar el contenido como JSON
        else:
            print(f"Error al solicitar la URL {url}. Código de estado: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud HTTP: {e}")

if __name__ == "__main__":
    main()
