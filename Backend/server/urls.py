from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.log,name="login"),
    path("register",views.register,name="register"),
    path("home/",views.homepage,name="home"),
    path("bookapp/<int:pid>",views.doctors,name="bookapp"),
    path("appoint/<int:pid>/<int:did>",views.appointment,name="appoint"),
    path("viewapps/<int:pid>",views.viewappointments,name="viewapps"),
    path("admlogin/",views.admlog,name="admlogin"),
    path("addoc/",views.addoc,name="addoc"),
    path("storedoc",views.storedoc,name="storedoc"),
    path("getdoc/",views.getdoc,name="getdoc"),
    path("admhome/",views.admhome,name="admhome"),
    path("admapps/",views.adminappointments,name="admapps"),
    path("doclogin/",views.doclog,name="doclogin"),
    path("dochome/",views.dochome,name="dochome"),
    path("addrecord",views.addrecord,name="addrecord"),
    path('medrecords/', views.medrecord_list, name='medrecords'),
    path("patmedrec/<int:pid>",views.patmed,name="patmedrec"),
]
