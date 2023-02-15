from django.contrib import admin
from .models import blog_model, blog_category_model, blog_tags, blog_comments
# Register your models here.


admin.site.register(blog_model)
admin.site.register(blog_category_model)
admin.site.register(blog_tags)
admin.site.register(blog_comments)