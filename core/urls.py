from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('industries/', views.IndustryListView.as_view())
]