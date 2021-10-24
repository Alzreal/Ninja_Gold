from django.shortcuts import render, redirect
from time import localtime, strftime
import random

def index(request):
    return render (request, "index.html")

def process_money(request):
    if "get_gold" not in request.session:
        request.session['get_gold']=0
        request.session['log']=[]
    else:
        request.session['date']= strftime("%B %d, %Y - %H:%M:%S %p", localtime())
        if 'farm' in request.POST:
            request.session['gold']=random.randint(10, 20)
            request.session['get_gold']+=request.session['gold']
            request.session['log'].append(
                f"Your ninja received {request.session['gold']} gold from the farm on {request.session['date']}"
            )
        if 'cave' in request.POST:
            request.session['gold']=random.randint(5, 10)
            request.session['get_gold']+=request.session['gold']
            request.session['log'].append(
                f"Your ninja received {request.session['gold']} gold from the cave on {request.session['date']}"
            )
        if 'house' in request.POST:
            request.session['gold']=random.randint(2, 5)
            request.session['get_gold']+=request.session['gold']
            request.session['log'].append(
                f"Your ninja received {request.session['gold']} gold from the house on {request.session['date']}"
            )
        if 'casino' in request.POST:
            request.session['gold']=random.randint(-50, 50)
            request.session['get_gold']+=request.session['gold']
            request.session['log'].append(
                f"Your ninja received {request.session['gold']} gold from the farm on {request.session['date']}"
            )

    return redirect('/')

def newgame(request):
    request.session.flush()
    return redirect('/')