import os
from django.core.files.storage import FileSystemStorage
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


# Create your models here.
class tb_news(models.Model): # database เพิ่มข่าวสาร
    news_title = models.CharField(max_length=300)
    #news_detail = models.TextField()
    news_detail = RichTextField(blank=True,null=True)
    news_photo = models.ImageField(upload_to='photo',default='')
    news_author = models.CharField(max_length=20,blank=True,null=True)
    news_date = models.DateTimeField(auto_now=True,blank=False)

    def __str__(self):
        return self.news_title