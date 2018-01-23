from django.contrib import admin
from blog.models import Post, Tag, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'author', 'createTime', 'changeTime', 'category', 'tags', 'content']

  def tags(self, obj):
    return "\n".join(obj.tag)

class TagAdmin(admin.ModelAdmin):
  list_display = ['tag']

class CategoryAdmin(admin.ModelAdmin):
  list_display = ['category']

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)