from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def inscription(request):
    erreur = None
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password != password2:
            erreur = "Les mots de passe ne sont pas identiques."
        
        elif User.objects.filter(username=username).exists():
            erreur = "Ce nom d'utilisateur existe déjà."
        
        else:
            User.objects.create_user(username=username, password=password)
            return redirect("connexion")
    return render(request, "pages/inscription.html", {"erreur": erreur})

def connexion(request):
    erreur = None
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("accueil")
        erreur = "Nom ou mot de passe incorrect."
    
    return render(request, "pages/connexion.html", {"erreur": erreur})

def accueil(request):

    if request.user.is_authenticated:
        return HttpResponse("Bonjour " + request.user.username)
    return redirect("connexion")