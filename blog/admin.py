from django.contrib import admin
from blog.models import Post, Tags, Classify

# Register your models here.
class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'author', 'createTime', 'changeTime', 'classify', 'tag', 'content']

class TagsAdmin(admin.ModelAdmin):
  list_display = ['tag']

class ClassifyAdmin(admin.ModelAdmin):
  list_display = ['classify']

admin.site.register(Post, PostAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Classify, ClassifyAdmin)