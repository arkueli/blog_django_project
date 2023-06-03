from rest_framework import generics, permissions, status
from rest_framework.response import Response
# These two lines import specific classes from the 'rest_framework_simplejwt' package that are used for authentication 
# and token generation.
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Story, Comment
from .serializers import UserSerializer, StorySerializer, CommentSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  
            refresh = RefreshToken.for_user(user)
            
         
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class StoryListView(generics.ListAPIView):
    serializer_class = StorySerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication)

    def get_queryset(self):  
        queryset = Story.objects.all()
        section = self.request.query_params.get('section', None)
        author = self.request.query_params.get('author', None)

        if section is not None:
            queryset = queryset.filter(section=section)
        if author is not None:
            queryset = queryset.filter(author__username=author)
        return queryset.order_by('-created_at')



class StoryDetailView(generics.RetrieveAPIView):
    queryset = Story.objects.all()  #
    serializer_class = StorySerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)


class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self): 
        queryset = Comment.objects.all() 
        article_id = self.request.query_params.get('article_id', None)
        user_id = self.request.query_params.get('user_id', None)
        date = self.request.query_params.get('date', None)
        
        if article_id is not None:  
            queryset = queryset.filter(story_id=article_id)
            
        if user_id is not None:   
            queryset = queryset.filter(user_id=user_id)
            
        if date is not None:    
            queryset = queryset.filter(created_at__date=date)

        return queryset.order_by('-created_at')



class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)




