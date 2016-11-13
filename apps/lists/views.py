from django.shortcuts import render


def home_page(request):
    """Home page"""
    context = {'new_item_text': request.POST.get('item_text', '')}
    return render(request, 'index.html', context)
