from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from owner.models import Book
from owner.forms import UserRegistrationForm
from customer.forms import UserProfileForm
class CustomerHome(View):
    model=Book
    template_name="cut_home.html"
    context={}
    def get(self,request,*args,**kwargs):
        books=self.model.objects.all()
        self.context["books"]=books
        return render(request,self.template_name,self.context)


class CustomeRegistration(TemplateView):
    template_name = "cust_reg.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        user_form=UserRegistrationForm()
        profile_form=UserProfileForm()
        context["user_form"]=user_form
        context["profile_form"]=profile_form
        return context

