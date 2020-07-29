from django.urls import path
from . import views

urlpatterns = [
    path('', views.myfunctioncall, name="get_hello"),
    path('about', views.myfunctionabout, name="get_about"),
    path('add/<str:a>/<str:b>', views.add, name="concat method"), # Careful about variable a,b
    path('intro/<str:name>/<int:age>', views.intro, name="intro of name and age"),
    path('myfirstpage', views.myfirstpage, name="basic page of html"),
    path('mysecondpage', views.mysecondpage, name="change b_html my ginger code"),
    path('mythirdpage', views.mythirdpage, name="using for loop method"),
    path('myforthpage/<int:num1>/<int:num2>', views.myforthpage, name="If checking greater"),
    path("myimagepage", views.myimagepage, name="load single image"),
    path("myimagepage2", views.myimagepage2, name="load two image"),
    path("myimagepage3", views.myimagepage3, name="load three image"),
    path("myimagepage4", views.myimagepage4, name="load four image"),
    path("myimagepage5/<str:name>", views.myimagepage5, name="load image through if"),
    path("myformpage_GET", views.myformpage_GET, name="myformpage_GET"),
    path("submitform_GET", views.mysubmitform_GET, name="mysubmitform_GET"),
    path("myformpage_POST", views.myformpage_POST, name="myformpage_POST"),
    path("submitform_POST", views.mysubmitform_POST, name="mysubmitform_POST"),
    path("form2", views.form2, name="form2"),
    path('form2_sub', views.form2_sub, name="form2_sub"),
    ]