from django.contrib import admin
from blog.models import Post,Category
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Comment
# Register your models here.


#@admin.register(Post) 
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    list_display = ('title','author', 'counted_views', 'status', 'published_date', 'created_date')
    list_filter = ('status','author') #we use comma to indicate that its a tupple
    ordering = ('-created_date',) # "-" doing the reverse order
    search_fields = ('title', 'content')
    summernote_fields = ('content',)
# instead of line 6 we can use the line below:

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    list_display = ('name','posts' ,'approved','created_date')
    list_filter = ('posts','approved')
    search_fields = ['name', 'posts']
    

admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
admin.site.register(Post,PostAdmin)
