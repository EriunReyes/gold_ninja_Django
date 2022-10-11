from django.shortcuts import render, HttpResponse, redirect
import random
# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0

    if 'chances' not in request.session:
        request.session['chances'] = 5

    if 'found' not in request.session:
        request.session['found'] = random.randint(1, 100)

    if request.session['chances'] < 0:
        del request.session['chances']

    if 'almost' not in request.session:
        request.session['almost'] = request.session['found'] + 5

    if 'almost1' not in request.session:
        request.session['almost1'] = request.session['found'] - 5
    return render(request, 'index.html')

def money(request):
    try:
        if request.POST['place'] == 'farm':
            request.session['gold'] += random.randint(20, 40)
            request.session['chances'] -= 1
        if request.POST['place'] == 'cave':
            request.session['gold'] += random.randint(5, 15)
            request.session['chances'] -= 1
        if request.POST['place'] == 'house':
            request.session['gold'] += random.randint(1, 5)
            request.session['chances'] -= 1
        if request.POST['place'] == 'casino':
            request.session['gold'] -= random.randint(0, 50)
            request.session['chances'] -= 1
        print(request.session['almost'])
        # request.session['almost'] = request.session['found'] + 5
        # request.session['almost1'] = request.session['found'] - 5
        print('session is working :)')
    except:
        print("session is not working :(")
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')