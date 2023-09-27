import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from main.forms import ProductForm
from django.urls import reverse
from main.models import Item
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required(login_url='/login')
def show_main(request):
    products = Item.objects.filter(user=request.user)
    context = {
        'creator': 'Rakha Fadil Atmojo',
        'pbpclass': 'PBP C',
        'npm': '2206082985',
        'name': request.user.username,
        'item': products,
        'total_items': len(products),
        'last_login': request.COOKIES.get('last_login', 'N/A'),
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', current_time)
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_amount_button(request, item_id):
    item = get_object_or_404(Item, pk=item_id) #Mengakses item yang ingin dimodifikasi
    item.user = request.user; 
    if item.amount > 0:
        item.amount += 1
        item.save()
    return redirect('main:show_main')

def reduce_amount_button(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.user = request.user;
    if item.amount > 1:
        item.amount -= 1
        item.save()
    else:
        item.delete();
    return redirect('main:show_main')

def remove_item_button(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.user = request.user;
    item.delete()
    return redirect('main:show_main')