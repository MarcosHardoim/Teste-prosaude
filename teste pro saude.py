import requests

# Faz a solicitação à API para obter a lista de postagens
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Verifica se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Converte a resposta JSON em um objeto Python
    posts = response.json()

    # Itera sobre as postagens e exibe seus títulos
    for post in posts:
        print(post['title'])
else:
    print('Não foi possível obter as postagens. Código de status:', response.status_code)





