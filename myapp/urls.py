from django.urls import path, include
from myapp.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

]