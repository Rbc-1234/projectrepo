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

class EditProduct(View):
    def get(self,request, id):
        stu =Product.objects.get(id=id)
        fm = AddForm(instance=stu)
        return render(request, 'core/edit-product.html', {'form':fm})
    def post(self, request, id):
        stu = Product.objects.get(id=id)
        fm = AddForm(request.POST, instance=stu)
        if fm.is_valid():
            fm.save()
        return redirect('/')