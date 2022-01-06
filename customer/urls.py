from django.urls import path
from customer import views
urlpatterns=[
path("home",views.CustomerHome.as_view(),name="customerhome")
]