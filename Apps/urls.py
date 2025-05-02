from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('insert/',views.insert,name='insert'),
    path('update/<int:user_id>/',views.update,name='update'),
    path('updated/',views.updated,name='updated'),
    path('delete/<int:user_id>/',views.delete,name='delete'),

    path('display/',views.display,name='display'),
    

]