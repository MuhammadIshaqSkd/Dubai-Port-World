from math import ceil

from django.shortcuts import render
from .models import Ad
# Create your views here.


def index(request):
    main = 'main'
    allProds = []
    catprods = Ad.objects.values('TYPE', 'id')
    cats = {item['TYPE'] for item in catprods}
    for cat in cats:
        prod = Ad.objects.filter(TYPE=cat)
        n = len(prod)
        n = int(n)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, 'n': n,'main':main}

    return render(request, 'index.html',params,)

def apply(request):
    apply = 'apply'

    return render(request, 'index.html',{'apply':apply})