
'''
urlpatterns = [
    url(r'^api/tutorials$', views.tutorial_list),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/tutorials/published$', views.tutorial_list_published)
]
'''
from django.urls import path


from django.urls import path,include

from .views import TutorialAPIView
from tutorials.views import TutorialAPIView
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('tutorialapi/',TutorialAPIView.as_view(),name='tutorial'),

]
