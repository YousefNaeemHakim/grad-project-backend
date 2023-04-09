from django.contrib import admin
from base.models import Summary, Category, Subscription
from community.models import Profile, Group, Post, Comment
from devroad.models import Roadmap, RoadmapStep
# Register your models here.

admin.site.site_header = "iRead Admin Panel"
admin.site.site_title = "iRead"

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'phone', 'birthdate', 'id')


class SummaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'id')
    list_display_links = ('author',)
    list_editable = ('title',)
    list_filter = ('categories', 'created_at')
    search_fields = ('title', 'categories')

    def combineTitleAndAuthor(self, obj):
        return "{} by {}".format(obj.title, obj.author)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'group', 'created_at', 'id')
    list_display_links = ('author', 'group')
    list_filter = ('group', 'created_at')
    search_fields = ('group', 'author')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'post', 'author', 'created_at', 'id')
    list_display_links = ('post', 'author')
    list_filter = ('created_at',)

class RoadmapAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'steps', 'id')
    list_filter = ('title',)
    search_fields = ('title',)

class RoadmapStepAdmin(admin.ModelAdmin):
    list_display = ('title', 'roadmap', 'created_at', 'updated_at')
    list_display_links = ('roadmap',)
    list_editable = ('title',)
    list_filter = ('roadmap', 'created_at', 'updated_at')
    search_fields = ('title', 'roadmap')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Summary, SummaryAdmin)
admin.site.register(Category)
admin.site.register(Subscription)
admin.site.register(Roadmap, RoadmapAdmin)
admin.site.register(RoadmapStep, RoadmapStepAdmin)