from django.shortcuts import render

def index(request):
    return render(
        request,
        'pages/index.html'    
    )

def hacker_etico(request):
    return render(
        request,
        'pages/comprar/hacker_etico.html'    
    )
