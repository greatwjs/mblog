from django.contrib import admin
from .models import Post,User
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','pub_date')

class UserAdmin(admin.ModelAdmin):
    list_User=('name','password')
admin.site.register(Post,PostAdmin)
admin.site.register(User,UserAdmin)
