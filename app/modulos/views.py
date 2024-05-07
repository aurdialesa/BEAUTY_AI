from django.shortcuts import render

# Create your views here.


def first_view(request):
    return render(request, 'login.html')

def second_view(request):
    return render(request, 'index.html')


def third_view(request):
    return render(request, 'rec_tono_piel.html')


def four_view(request):
    return render(request, 'rec_tip_ceja.html')


def five_view(request):
    return render(request, 'rec_tono_cabello.html')

def six_view(request):
    return render(request, 'cal_sug.html')


