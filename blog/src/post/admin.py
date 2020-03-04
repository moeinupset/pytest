from django.contrib import admin

from post.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'status', 'created_time')
    search_fields = ('title', )
    list_display_links = ('title', 'status')
    readonly_fields = ('status', )
    actions = ('make_publish',)

    def author_name(self, obj):
        return obj.author.user.username

    def save_model(self, request, obj, form, change):
        obj.author = request.user.author
        obj.save()

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ()
        return self.readonly_fields

    def make_publish(self, request, queryset):
        queryset.update(status=Post.PUBLISHED)
        return queryset


admin.site.register(Post, PostAdmin)
