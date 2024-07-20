from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Category,Post

class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','add_date')
    search_fields=('title',)

class PostAdmin(admin.ModelAdmin):
    list_display=('title',)
    search_fields=('title',)
    list_filter=('cat',)
    list_per_page=50


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
