from ijosephapp.views import *
from django.urls import include, path
from .views import *
# from django.urls import path

app_name = "ijosephapp"

urlpatterns = [
    path('', home, name='home'),
    path('jobs/', job_list, name='jobs'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register_user, name="register"),
    path('logout/', logout_user, name='logout'),
]