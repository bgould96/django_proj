from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Camp)
admin.site.register(User)
admin.site.register(Group)
admin.site.register(Bot)
admin.site.register(Message)
admin.site.register(Favorite)
admin.site.register(Access_Token)