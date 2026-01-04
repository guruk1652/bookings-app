from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('industries/', views.IndustryListView.as_view()),
    path('organizations/', views.OrganizationListAPIView.as_view())
]