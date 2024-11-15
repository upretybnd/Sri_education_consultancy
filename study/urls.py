from django.urls import path
from . import views

urlpatterns = [
    path('usa/', views.study_in_us, name='usa'),
    path('austrilia/', views.study_in_austrilia, name='austrilia'),
    path('canada/', views.study_in_canada, name='canada'),
    path('japan/', views.study_in_japan, name='japan'),
    path('korea/', views.study_in_korea, name='korea'),
    path('europe/', views.study_in_europe, name='europe'),
]