from django.urls import path, include
from .views import HomePageView

app_name='portfolio'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepages'),
]