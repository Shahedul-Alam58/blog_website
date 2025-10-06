from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')     # ✅ parentheses (tuple)
    list_filter = ('date_posted',)              # ✅ comma makes it a tuple
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)
