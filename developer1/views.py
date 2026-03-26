from django.shortcuts import render


def hoja_de_vida(request):
    return render(request, 'developer1/index.html')
