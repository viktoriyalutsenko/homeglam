from django.shortcuts import render

# Create your views here.
def glavnaya(request):
    return render(request, 'glavnaya.html')

def contacts(request):
    return render(request, 'contacts.html')
# Create your views here.
