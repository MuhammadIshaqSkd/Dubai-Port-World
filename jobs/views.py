from math import ceil

from django.shortcuts import render
from .models import Ad, Applicant
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
    allProds = []
    catprods = Ad.objects.values('TYPE', 'id')
    cats = {item['TYPE'] for item in catprods}
    for cat in cats:
        prod = Ad.objects.filter(TYPE=cat)
        n = len(prod)
        n = int(n)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, 'n': n, 'apply': apply}

    return render(request, 'index.html', params, )

def applyform(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        address = request.POST.get('address', '')
        applyjob = request.POST.get('applyjob', '')
        country = request.POST.get('country', '')
        city = request.POST.get('city', '')
        email = request.POST.get('email', '')
        cnic = request.POST.get('cnic', '')
        phone = request.POST.get('phone', '')
        zip = request.POST.get('zip', '')
        apy = Applicant(Ap_name=name,adddress=address,country=country, city=city,
                  applyedfor=applyjob,email=email,cnic=cnic,phone=phone,zip=zip, )

        apy.save()
        ch = 'new'
        # print(applyjob)

        return render(request, 'index.html',{'ch':ch})