from django.urls import path
from owner import views
urlpatterns=[
    path("",views.OwnerHome.as_view(),name="ownerindex"),
    path("books/add",views.AddBook.as_view(),name="addbook"),
    path("books/all",views.AllBooks.as_view(),name="listallbooks"),
    path("books/<int:id>",views.BookDetail.as_view(),name="bookdetail"),
    path("books/change/<int:id>",views.BookUpdate.as_view(),name="editbook"),
    path("accounts/signup",views.user_registration,name="registration"),
    path("accounts/signin",views.signin,name="signin"),
    path("accounts/signout",views.signout,name="signout")

]