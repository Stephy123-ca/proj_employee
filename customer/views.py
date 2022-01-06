from django.shortcuts import render,redirect
from django.views.generic import View
from owner.models import Book
class CustomerHome(View):
    model=Book
    template_name="cut_home.html"
    context={}
    def get(self,request,*args,**kwargs):
        books=self.model.objects.all()
        self.context["books"]=books
        return render(request,self.template_name,self.context)