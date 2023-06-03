from django.urls import include, path  
from django.contrib import admin   # provides the Django admin interface for managing site content.

# used to obtain and refresh 'JWT tokens' for authenticated users.
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import UserCreateView, StoryListView, StoryDetailView, CommentListView, CommentCreateView



# contains a list of URL patterns for our Django application.
urlpatterns = [  
    path('admin/',admin.site.urls),
    path('api/', include('api.urls')),
    path('parsers/', include('parsers.urls')),
    
# This view is responsible for handling requests to obtain an access and refresh token.
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
# responsible for handling requests to refresh an access token.
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
# responsible for handling requests to create a new user (UserCreateView)
    path('api/users/', UserCreateView.as_view(), name='user_create'),
    
# responsible for handling requests to get a list of all stories. (StoryListView)
    path('api/stories/', StoryListView.as_view(), name='story_list'),
    
# responsible for handling requests to get details for a specific story, where <id> is the ID of the story.
    path('api/stories/<int:pk>/', StoryDetailView.as_view(), name='story_detail'),
    
# responsible for handling requests to get a list of all comments. (CommentListView)
    path('api/comments/', CommentListView.as_view(), name='comment_list'),
    
# responsible for handling requests to create a new comment. (CommentCreateView)
    path('api/comments/create/', CommentCreateView.as_view(), name='comment_create'),
]









