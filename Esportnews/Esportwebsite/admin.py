from django.contrib import admin
from .models import tb_news
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display =["news_title","news_date"]


admin.site.register(tb_news,NewsAdmin)

