from django.shortcuts import render,redirect
from django.http import HttpResponse
from owner import  forms
from owner.models import  Employees
from django.contrib.auth import authenticate,login,logout
from owner.decorators import signin_required
from django.views.generic import View,ListView,TemplateView,CreateView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from owner.forms import UserRegistrationForm
from owner.decorators import signin_required
from Employee.forms import UserProfileForm
from Employee.models import UserProfile

@method_decorator(signin_required,name="dispatch")
class EmpRegistration(TemplateView):
    template_name = "emp_reg.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        user_form=UserRegistrationForm()
        profile_form=UserProfileForm()
        context["user_form"]=user_form
        context["profile_form"]=profile_form
        return context
    def post(self,request,*args,**kwargs):
        u_form=UserRegistrationForm(request.POST,files=request.FILES)
        p_form=UserProfileForm(request.POST,files=request.FILES)
        if u_form.is_valid() & p_form.is_valid():
            user=u_form.save()
            profile=p_form.save(commit=False)
            profile.user=user
            profile.save()
            return redirect("listallemp")
        else:
            u_form = UserRegistrationForm(request.POST)
            p_form = UserProfileForm(request.POST)
            context={}
            context["user_form"] = u_form
            context["profile_form"] = p_form
            return render(request,"emp_reg.html",context)




# @signin_required
# def owner_home(request):
#
#     return render(request, "owner_home.html")

@method_decorator(signin_required,name="dispatch")
class OwnerHome(TemplateView):
    template_name="owner_home.html"


#
# @signin_required
# def add_book(request,*args,**kwargs):
#     form=forms.BookForm()
#     context={"form":form}
#     if request.method=="POST":
#         form=forms.BookForm(request.POST,files=request.FILES)
#         if form.is_valid():
#             form.save()
#
#             # book=Book(book_name=form.cleaned_data["book_name"],
#             #           author=form.cleaned_data["author"],
#             #           price=form.cleaned_data["price"],
#             #           copies=form.cleaned_data["copies"]
#             #           )
#             # book.save()
#             return  redirect("listallbooks")
#         else:
#             return render(request,"emp_reg.html",{"form":form})
#
#
#     return render(request, "emp_reg.html",context)
@method_decorator(signin_required,name="dispatch")

# class AddBook(CreateView):
#     model=Employees
#     template_name="emp_reg.html"
#     form_class=forms.EmployeeForm
#     success_url = reverse_lazy("listallbooks")
#     # context={}
    # def get(self,request,*args,**kwargs):
    #     form=self.form_class()
    #     self.context["form"]=form
    #     return render(request,self.template_name,self.context)
    #
    # def post(self,request,*args,**kwargs):
    #     form=self.form_class(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("listallbooks")
    #     else:
    #         self.context["form"]=form
    #         return render(request,self.template_name,self.context)


#
# def list_books(request,*args,**kwargs):
#     books=Book.objects.all()
#     context = {"products": books}
#
#     return render(request, "emp_list.html", context)
@method_decorator(signin_required,name="dispatch")
class AllEmp(ListView):
    model=User
    template_name="emp_list.html"
    context_object_name = "employees"



@method_decorator(signin_required,name="dispatch")
class EmpDetail(DetailView):
    model=User
    template_name="Emp_detail.html"
    context_object_name = "employee"
    pk_url_kwarg = "id"

@method_decorator(signin_required,name="dispatch")
class EmpUpdate(UpdateView):
    template_name="edit_emp.html"
    model=User
    pk_url_kwarg = "id"
    success_url = reverse_lazy("listallemp")

    form_class=forms.EmployeeForm


class SignIn(TemplateView):
    template_name = "login.html"
    context = {}

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        form=forms.SigninForm()
        context["form"]=form

        return context
    def post(self,request,*args,**kwargs):
        form=forms.SigninForm(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data["username"]
            pwd=form.cleaned_data["password"]
            user=authenticate(request,username=u_name,password=pwd)
            if user:
                login(request,user)
                if user.is_superuser:
                    return redirect("ownerindex")
                else:
                    return redirect("customerhome")


            else:
                print("invalid")
                self.context["form"]=form
                return render(request,self.template_name,self.context)


#
# def signin(request):
#     form=forms.SigninForm()
#     context={"form":form}
#     if request.method=="POST":
#
#         form=forms.SigninForm(request.POST)
#         if form.is_valid():
#             u_name=form.cleaned_data["username"]
#             pwd=form.cleaned_data["password"]
#             user=authenticate(request,username=u_name,password=pwd)
#             if user:
#                 login(request,user)
#                 return redirect("ownerindex")
#             else:
#                 return render(request, "login.html", context)
#
#     return render(request,"login.html",context)

@signin_required
def signout(requset,*args,**kwargs):
    logout(requset)
    return redirect("signin")


# class Registration(CreateView):
#     template_name = "emp_reg.html"
#     form_class = forms.UserRegistrationForm
#     work_class = forms.UserProfile
#
#     def post(self, request):
#         u_form = UserRegistrationForm(request.POST, files=request.FILES)
#         p_form = UserProfileForm(request.POST, files=request.FILES)
#         if u_form.is_valid() & p_form.is_valid():
#             user = u_form.save()
#             profile = p_form.save(commit=False)
#             profile.user = user
#             profile.save()
#             return redirect("listallemp")


# @method_decorator(signin_required,name="dispatch")
# class Delete_emp(DeleteView):
#     template_name="emp_list.html"
#     model=Employees
#     pk_url_kwarg = "id"
#     success_url = reverse_lazy("listallbooks")
#
#     form_class=forms.EmployeeForm
