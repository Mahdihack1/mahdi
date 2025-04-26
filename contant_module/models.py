from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Contact(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='contacts')
    name=models.CharField(max_length=50,verbose_name='')
    phone=models.CharField(max_length=50,verbose_name='')
    email=models.EmailField(max_length=50,null=True,blank=True,verbose_name='')
    address=models.TextField(null=True,blank=True,verbose_name='')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='')

    def __str__(self):
        return f'{self.name} --- {self.phone}'
