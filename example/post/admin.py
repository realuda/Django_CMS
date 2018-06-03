from django.contrib import admin
from post.models import Category, Post, Comment

class PostAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super(PostAdmin, self).get_urls()
        post_urls = [
            url(r'^status/$', self.admin_site.admin_view(self.post_status_view))
        ]
        return post_urls + urls

    def post_status_view(self, request):
        context = dict(
            self.admin_site.each_context(requst),
            posts=Post.objects.all(),
            key1=value1,
            key2=value2,
        )
        return TemplateResponse(request, "admin/post_status.html", context)

    form = myPostAdminForm
    list_per_page = 10
    list_display = ( 'id', 'title', 'member', 'is_deleted', 'created_at', )
    list_editable = ('is_deleted', )
    list_filter = ('member__permission', 'category__name', 'is_deleted', )
    fields = ('member', 'category', 'title', )

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

# Register your models here.
