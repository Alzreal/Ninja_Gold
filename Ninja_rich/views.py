from django.shortcuts import render, redirect
import random

def index(request):
    return render (request, "index.html")

def process_money(request):
    if 'farm' in request.POST:
        gold=random.randint(10, 20)
        context= {
            'gold':gold
        }
    if 'cave' in request.POST:
        gold=random.randint(5, 10)
        context= {
            'gold':gold
        }
    if 'house' in request.POST:
        gold=random.randint(2, 5)
        context= {
            'gold':gold
        }
    if 'casino' in request.POST:
        gold=random.randint(-50, 50)
        context= {
            'gold':gold
        }
    return render (request, 'index.html', context)