from django.shortcuts import render, redirect
from time import localtime, strftime
import random

def index(request):
    context = {
        'date': strftime("%B %d, %Y - %H:%M:%S %p", localtime()),
    }
    return render (request, "index.html", context)

def process_money(request):
    if "get_gold" not in request.session:
        request.session['get_gold']=[]
    if 'farm' in request.POST:
        gold=random.randint(10, 20)
        request.session['get_gold']+=gold
    
    if "get_gold" not in request.session:
        request.session['get_gold']=[]
    if 'cave' in request.POST:
        gold=random.randint(5, 10)
        request.session['get_gold']+=gold
    
    if "get_gold" not in request.session:
        request.session['get_gold']=[]
    if 'house' in request.POST:
        gold=random.randint(2, 5)
        request.session['get_gold']+=gold
    
    if "get_gold" not in request.session:
        request.session['get_gold']=[]
    if 'casino' in request.POST:
        gold=random.randint(-50, 50)
        request.session['get_gold']+=gold
    
    return redirect('/')