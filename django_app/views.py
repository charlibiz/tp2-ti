from django.http import response
from django.shortcuts import render, redirect
import requests
from datetime import date

# Create your views here.
user_key = "721aebe0-0232-4326-9e21-1967ad98fff1"
today = date.today()

def home(request):
    return render(request, "django_app/home.html")

def users(request):
    if request.method == "POST":
        label = request.POST.get("input")
        categorieId = request.POST.get("categorieid")
        return render(request, "django_app/users.html")

    else:
        response = requests.get("https://airbnb-clone-rest-api.herokuapp.com/api/${user_key}/get")
        if response.status_code == 200:
            _users = response.json()
            return render(request, "django_app/users.html", {"users": _users})
        else:
            return render(request, "django_app/users.html")

def members(request):
    if request.method == "POST":
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        address = request.POST.get("address")
        city = request.POST.get("city")
        phone = request.POST.get("phone")
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        password = request.POST.get("password")
        login = request.POST.get("login")

        user = {
            "id": "",
            "statut": "1",
            "employee": "0",
            "gender": gender,
            "email": email,
            "address": address,
            "town": city,
            "user_mobile": phone,
            "login": login,
            "country_code": "CA",
            "lastname": lastName,
            "firstname": firstName,
            "date_creation": today,
            "note_private": password
            }
        req = requests.post("http://34.95.8.244/api/index.php/users?DOLAPIKEY="+ dolapikey, user)
        if req.status_code == 200:
            return render(request, "django_app/members.html", {"success":1, "id":req.json()})
        else: 
            return render(request, "django_app/members.html", {"success":0})
    return render(request, "django_app/members.html")


def order(request):
    if request.method == "POST":
        id = request.POST.get("orderid")
        if id:
            response = requests.get("http://34.95.8.244/api/index.php/products/"+ id +"?DOLAPIKEY="+ dolapikey)
            if response.status_code == 200:
                data = response.json()
                return render(request, "django_app/order.html", {"item": data, "modal": 1})
            else:
                data = {"introuvable"}
                return render(request, "django_app/order.html", {"item": data, "modal": 0})
        else:
            response = requests.get("http://34.95.8.244/api/index.php/products?DOLAPIKEY=" + dolapikey)
            data = response.json()
            return redirect("/users")
    
    else:
        response = requests.get("http://34.95.8.244/api/index.php/products?DOLAPIKEY=" + dolapikey)
        data = response.json()
        return redirect("/users")

def purchase(request):
        return redirect("/users")

