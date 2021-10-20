from django.shortcuts import render, redirect
import random

def index(request):
    return render (request, "index.html")

def process_money(request):
    name=request.POST
    if name == 'farm':
        gold=random.randint(10, 20)
        context= {
            'gold':gold
        }
    return render (request, 'index.html', context)