from django.contrib import admin

# Register your models here.
from .models import Topic , Group , Post

admin.site.register(Topic)
admin.site.register(Group)
admin.site.register(Post)
# admin.site.register(Profile)