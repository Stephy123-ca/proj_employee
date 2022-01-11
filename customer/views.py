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


class CustomerRegistration(TemplateView):
    template_name = "cust_reg.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        user_form=UserRegistrationForm()
        profile_form=UserProfileForm()
        context["user_form"]=user_form
        context["profile_form"]=profile_form
        return context
    def post(self,request,*args,**kwargs):
        u_form=UserRegistrationForm(request.POST)
        p_form=UserProfileForm(request.POST)
        if u_form.is_valid() & p_form.is_valid():
            user=u_form.save()
            profile=p_form.save(commit=False)
            profile.user=user
            profile.save()
            return redirect("signin")
        else:
            u_form = UserRegistrationForm(request.POST)
            p_form = UserProfileForm(request.POST)
            context={}
            context["user_form"] = u_form
            context["profile_form"] = p_form
            return render(request,"cust_reg.html",context)




