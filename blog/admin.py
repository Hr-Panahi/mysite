from django.contrib import admin
from blog.models import Post,Category
# Register your models here.


#@admin.register(Post) 
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    list_display = ('title','author', 'counted_views', 'status', 'published_date', 'created_date')
    list_filter = ('status','author') #we use comma to indicate that its a tupple
    ordering = ('-created_date',) # "-" doing the reverse order
    search_fields = ('title', 'content')
# instead of line 6 we can use the line below:
admin.site.register(Category)
admin.site.register(Post,PostAdmin)