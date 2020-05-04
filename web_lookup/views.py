from django.shortcuts import render



# Create your views here.

def home(request):
    import json
    import requests


    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=31D104DF-478D-48E1-8026-9D87A197B82A")


        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error ....."

        return render(request, 'home.html', {'api': api})

    else:


        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=31D104DF-478D-48E1-8026-9D87A197B82A")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error ....."

        return render(request, 'home.html', {'api':api})

def about(request):
     return render(request, 'about.html', {})

