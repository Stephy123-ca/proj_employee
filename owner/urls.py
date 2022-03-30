from django.urls import path
from owner import views
urlpatterns=[
    path("",views.OwnerHome.as_view(),name="ownerindex"),
    # path("add",views.AddEmp.as_view(),name="addEmp"),
    # path("delete/<int:id>", views.Delete_emp.as_view(), name="Deleteemp"),
    path("list",views.AllEmp.as_view(),name="listallemp"),
    path("view/<int:id>",views.EmpDetail.as_view(),name="Empdetail"),
    path("change/<int:id>",views.EmpUpdate.as_view(),name="editemp"),
    # path("signup",views.Registration.as_view(),name="registration"),

    path("accounts/signout",views.signout,name="signout"),
    path("add", views.EmpRegistration.as_view(), name="ownerreg"),

]