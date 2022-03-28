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


#ListView rednder list all objects
#TemplateView
#DetailView
#UpdateView
#DeleteView

# Create your views here.

# books = [
#     {"id": 1, "book_name": "randamoozham", "author": "mt", "price": 450, "copies": 50,
#      "image": "https://upload.wikimedia.org/wikipedia/en/a/af/Randamoozham_30th_edition_cover.jpg"},
#     {"id": 2, "book_name": "halfgf", "author": "chethan", "price": 500, "copies": 45,
#      "image": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTHSXYG7XIi8PEuu8zqes8MWFgmKtRiv0gjmJJN402siII5uXE6"},
#     {"id": 3, "book_name": "alchmist", "author": "paulo", "price": 550, "copies": 50,
#      "image": "https://upload.wikimedia.org/wikipedia/en/a/af/Randamoozham_30th_edition_cover.jpg"},
#     {"id": 4, "book_name": "indhuleka", "author": "chandhu", "price": 650, "copies": 20,
#      "image": "https://upload.wikimedia.org/wikipedia/en/a/af/Randamoozham_30th_edition_cover.jpg"},
#     {"id": 5, "book_name": "harry", "author": "jkr", "price": 650, "copies": 20,
#      "image": "https://i.guim.co.uk/img/media/1d4b16d4c6703e9bec9174f1cadc278026de0647/0_75_1280_768/master/1280.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=d036928c5974e9e8bfd87be5dcf37dd7"
# },
#
#
# ]
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
        u_form=UserRegistrationForm(request.POST)
        p_form=UserProfileForm(request.POST)
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
    model=UserProfile
    template_name="emp_list.html"
    context_object_name = "products"



@method_decorator(signin_required,name="dispatch")
class EmpDetail(DetailView):
    model=UserProfile
    template_name="Emp_detail.html"
    context_object_name = "employee"
    pk_url_kwarg = "id"

@method_decorator(signin_required,name="dispatch")
class EmpUpdate(UpdateView):
    template_name="edit_emp.html"
    model=UserProfile
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


class Registration(CreateView):
    template_name = "emp_reg.html"
    form_class = forms.UserRegistrationForm
    work_class = forms.UserProfile

    def post(self, request):
        u_form = UserRegistrationForm(request.POST, files=request.FILES)
        p_form = UserProfileForm(request.POST, files=request.FILES)
        if u_form.is_valid() & p_form.is_valid():
            user = u_form.save()
            profile = p_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect("listallemp")


# @method_decorator(signin_required,name="dispatch")
# class Delete_emp(DeleteView):
#     template_name="emp_list.html"
#     model=Employees
#     pk_url_kwarg = "id"
#     success_url = reverse_lazy("listallbooks")
#
#     form_class=forms.EmployeeForm
