from django.contrib import admin
from .models import ASIN,ASIN_Instance,ASIN_task,Book,Lead,ASIN_Search_task

# Register your models here.
admin.site.register(ASIN)
admin.site.register(ASIN_Instance)
admin.site.register(ASIN_task)
admin.site.register(Book)
admin.site.register(Lead)
admin.site.register(ASIN_Search_task)



