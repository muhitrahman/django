

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SingnUpView.as_view(), name='singup')
]