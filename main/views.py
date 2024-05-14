from django.shortcuts import render

# Create your views here.
def glavnaya(request):
    return render(request, 'glavnaya.html')

def catalog(request):
    return render(request, 'catalog.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

# Create your views here.
