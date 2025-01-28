from django.shortcuts import render
import requests

def home(request):
    return render(request, 'home.html')

def get_data(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = response.json()
    return render(request, 'get_data.html', {'data': data})

def post_data(request):
    if request.method == 'POST':
        response = requests.post('https://jsonplaceholder.typicode.com/posts', data=request.POST)
        return render(request, 'post_data.html', {'response': response.json()})
    return render(request, 'post_data.html')

def json_data(request):
    # Пример отправки и получения JSON
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = response.json()
    return render(request, 'json_data.html', {'data': data})

def api(request):
    # Простой API
    if request.method == 'GET':
        return JsonResponse({'message': 'Hello, World!'})
