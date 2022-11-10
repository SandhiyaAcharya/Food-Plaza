from django.contrib import admin
from django.urls import path
from food import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('addfood/',views.addfood),
   path('menu/',views.menu,name="menu"),
   path('update/<int:id>',views.update),
   path('delete/<int:id>',views.delete),
   path('addcustomer/',views.addcustomer),
   path('customer/',views.customer),
   path('updatecust/<int:custid>',views.updatecust),
   path('deletecust/<int:custid>',views.deletecust),
   path('login',views.login),
   path('doLogin',views.doLogin),
   path('addtocart/',views.addtocart),
   path('showcart/',views.showcart),
   path('updatequantity/',views.updatequantity),
   path('deletecart/<int:id>',views.deletecart),
   path('order/',views.order),
   path('changepass/', views.changepass),
   path('logout/',views.logout),
   path('graphs/',views.graphs),
   path('graphone/', views.graphone),
   path('graphtwo/', views.graphtwo),
   path('graphthree/', views.graphthree),
   path('graphfour/', views.graphfour),
   path('myorders/',views.myorders),
   path('',views.home)
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
