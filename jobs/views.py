from django.shortcuts import render

# Create your views here.


def index(request):
    main = 'main'
    return render(request, 'index.html',{'main':main})

def apply(request):
    apply = 'apply'

    return render(request, 'index.html',{'apply':apply})