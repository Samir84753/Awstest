from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('blog/msg',views.postmsg),
    path('viewmsg',views.viewmsg,name='msgpage'),
    path('deletemsg/<int:user_id>',views.deletepost),
    path('editpost/<int:user_id>',views.editpost),
    path('update',views.updatepost)
    

]