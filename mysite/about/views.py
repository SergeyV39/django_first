from django.shortcuts import render


# Create your views here.
def index(request):
    about = 'About us'
    return render(request, 'about/index.html', {'about': about})
