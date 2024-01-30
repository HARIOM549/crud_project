from django.urls import path
from .views import *


urlpatterns = [

    path("",home,name='home'),
    # path("",base,name='base'),
    path("Signup/",Signup,name='Signup'),
    path("Login/",Login,name='Login'),
    path("about/",about,name='about'),
    path("Contact/",Contact,name='Contact'),
    path("savedata/",savedata,name='savedata'),
    path("Logindata/",Logindata,name='Logindata'),
    path("delete/<int:pk>",delete,name='delete'),
    path("query/",query,name='query'),
    path('showdata/<str:pk>',showdata,name='showdata'),
    path('edit/<int:pk>',edit,name='edit'),
    path('update/<int:pk>',update,name='update')


]

