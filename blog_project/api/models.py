from django.db import models


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager




class UserManager(BaseUserManager): 
    
    def create_user(self, username, password): 
       
       
        user = self.model(username=username)
        user.set_password(password)   
        user.save(using=self._db) 
        return user   
    

    def create_superuser(self, username, password):
        
        
        user = self.create_user(username, password)
        
        user.is_admin = True
        user.save(using=self._db) 
        return user 


class User(AbstractBaseUser):
    
 
    username = models.CharField(max_length = 50, unique = True)
   
    is_active = models.BooleanField(default = True) 
    
    is_admin = models.BooleanField(default=False)

    objects = UserManager()  

    
    USERNAME_FIELD = 'username'
  
    def __str__(self):
        return self.username

    
    def has_perm(self, perm, obj = None):
        return True

   
    def has_module_perms(self, app_label):
        return True

    
    @property
    # If "is_admin" is True, then "is_staff" is also True, which means that the user is a staff member.
    def is_staff(self):  
        return self.is_admin


class Story(models.Model):

    title = models.CharField(max_length=200)

    slug = models.SlugField(max_length=1000, null=True, blank=True)   
   
    content = models.TextField()
    
    
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    
    section = models.CharField(max_length=50)
    

    created_at = models.DateTimeField(auto_now_add = True)
 
    
   
    def __str__(self):
        return self.title


class Comment(models.Model):
    

    user = models.ForeignKey(User, on_delete = models.CASCADE) 
    story = models.ForeignKey(Story, on_delete = models.CASCADE)
    
 
    content = models.TextField()
    
   
    created_at = models.DateTimeField(auto_now_add = True)
    
    # Returns the comment's content.
    def __str__(self):
        return self.content






