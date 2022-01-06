from django.shortcuts import render,redirect
from .models import Product
from django.views import View
from .forms import AddForm
# Create your views here.
class Pr_home(View):
    def get(self,requests):
        mytb=Product.objects.all()
        return render(requests,'core/home.html',{'mytb':mytb})

class Pr_Add(View):
    def get(self,requests):
        myform=AddForm()
        return render(requests,'core/addproduct.html',{'mytb':myform})

    def post(self,requests):
        myform=AddForm(requests.POST)
        if myform.is_valid():
            myform.save()
            return redirect('/')
        else:
            return render(requests,'core/addproduct.html',{'mytb':myform})
