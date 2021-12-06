from django.contrib import admin
from home.models import Contact,requestblog,Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all":("css/main2.css",)
        }
        js = ("js/blog.js",)

admin.site.register(Contact)
admin.site.register(requestblog)
admin.site.register(Blog,BlogAdmin)