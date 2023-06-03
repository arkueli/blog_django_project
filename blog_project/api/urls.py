from . import views
from rest_framework import routers
from django.urls import path, include
from .views import UserCreateView, StoryListView, StoryDetailView, CommentListView, CommentCreateView

router = routers.DefaultRouter()

urlpatterns = [
    path('api/', include(router.urls))
]















