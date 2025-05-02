from django.db import models
from django.contrib.auth.hashers import make_password,check_password

# Create your models here.
class Insert(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    is_user = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    
  
    def create_user(self,username,email,password):
        self.username = username
        self.email = email
        self.password = make_password(password)
       
    def __str__(self):
        return self.username  
    
class Update(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()

    def update_user(self,username,email):
        self.username = username
        self.email = email
        
    def __str__(self):
        return self.username
    
    
    
class Delete(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def delete_user(self,username,email,password):
        self.username = username
        self.email = email
        self.password = make_password(password)
        
    def __str__(self):
        return self.username  
        
    
    