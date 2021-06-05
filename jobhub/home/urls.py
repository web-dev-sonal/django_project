from django.urls import path, include
from django.conf.urls import url
from home import views

urlpatterns = [
    url('carpenter/',include('carpenter.urls')),
    url('driver/',include('driver.urls')),
    url('electrician/',include('electrician.urls')),
    url('servant/',include('home_servant.urls')),
    url('painter/',include('painter.urls')),
    url('teacher/',include('teacher.urls')),
    path('about/',views.about),
    path('contact/',views.contact),
    path('Login/',views.Login),
    path('',views.home_page),
]
