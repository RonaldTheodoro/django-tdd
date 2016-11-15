from django.shortcuts import render
from django.shortcuts import redirect
from .models import Item


def home_page(request):
    """Home page"""
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    return render(request, 'index.html', {'items': Item.objects.all()})
