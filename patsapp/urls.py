from django.urls import path
from patsapp import views
urlpatterns=[
    path('',views.home,name='my_index'),
    path('',views.about,name='my_about'),
    path('',views.contact,name='my_contact'),

]