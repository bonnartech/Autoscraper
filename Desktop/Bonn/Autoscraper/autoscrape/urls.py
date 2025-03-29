from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('scrape/', views.run_scrape, name='scrape'),
    path('export/', views.export_csv, name='export'),
    path('upload/', views.upload_azure, name='upload'),
    path('dynamic_scrape/', views.dynamic_scrape, name='dynamic_scrape'),
]
