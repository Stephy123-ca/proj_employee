from django.urls import path
from owner import views
urlpatterns=[
    path("",views.OwnerHome.as_view(),name="ownerindex"),
    # path("add",views.AddBook.as_view(),name="addbook"),
    # path("delete/<int:id>", views.Delete_emp.as_view(), name="Deleteemp"),
    path("all",views.AllBooks.as_view(),name="listallbooks"),
    path("view/<int:id>",views.BookDetail.as_view(),name="bookdetail"),
    path("change/<int:id>",views.BookUpdate.as_view(),name="editbook"),
    path("signup",views.Registration.as_view(),name="registration"),
    path("signin",views.SignIn.as_view(),name="signin"),
    path("accounts/signout",views.signout,name="signout"),
    path("add", views.OwnerRegistration.as_view(), name="ownerreg"),

]