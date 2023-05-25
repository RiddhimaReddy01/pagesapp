from django.contrib import admin
from django.urls import path
from .views import HomePageView,AboutusPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomePageView.as_view(), name='home'),
    path('aboutus/',AboutusPageView.as_view(),name='aboutus')
]
