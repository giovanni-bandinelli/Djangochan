from django.contrib import admin

from django.contrib import admin
from core.models import *

class BoardAdmin(admin.ModelAdmin):
    pass

admin.site.register(Board, BoardAdmin)

class ThreadAdmin(admin.ModelAdmin):
    pass

admin.site.register(Thread, ThreadAdmin)

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)