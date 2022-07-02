from django.contrib import admin
from .models import Post, Links, AboutUs

# Register your models here.
# username: code
# email address admin@mail.com
# password: admincode


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'meta_description', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['disapprove_comments']

    def disapprove_comments(self, request, queryset):
        queryset.update(active = False)
    
admin.site.register(Post, PostAdmin)
admin.site.register(Links)
admin.site.register(AboutUs)