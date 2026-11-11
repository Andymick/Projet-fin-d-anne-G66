from django.shortcuts import render

# Create your views here.
def inscription(request):
    return render(request, 'pages/inscription.html')

def connexion(request):
    return render(request, 'pages/connexion.html')