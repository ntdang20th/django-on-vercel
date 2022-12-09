from django.urls import path, include
from .views import FollowUpView, ResponesData, LocationFollowUpView
urlpatterns = [
    path('', FollowUpView.as_view(), name='flup'),
    path('', LocationFollowUpView.as_view(), name='loca_flup'),
    path('post/', ResponesData),
]
