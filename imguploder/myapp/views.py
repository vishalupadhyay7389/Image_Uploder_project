from django.shortcuts import render
from .models import Images
from .forms import Imageforms
# Create your views here.

def home(request):
    
    if request.method == "POST":
        form = Imageforms(request.POST , request.FILES)
        if form.is_valid():
            form.save()
    form = Imageforms()
    img = Images.objects.all()
    return render(request , 'myapp/home.html',{'img':img , 'form':form})
