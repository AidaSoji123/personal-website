from django.urls import path
from . import views

app_name = 'myself'
urlpatterns =  [path('home/',views.home,name = 'home'),
                path('about/',views.about,name ='about'),
                path('contact/',views.contact,name ='contact'),
                path('submit_data/',views.submited_data,name='submit_data')
               ]



