from django.urls import path
from Employee import views
from django.views.generic import TemplateView


urlpatterns=[
    path("",TemplateView.as_view(template_name="cbase.html"),name="cbase"),
    path("home",views.CustomerHome.as_view(),name="customerhome"),
    path("accounts/Employee/signin",views.CustomerRegistration.as_view(),name="custreg"),
    path("",views.Index.as_view(),name="cindex"),
    path("signin",views.SignIn.as_view(),name="signin"),

]