from django.contrib import admin

from destinations.models import Destination, Like, Comment


class CommentInLineAdmin(admin.TabularInline):
    model = Comment

class DestinationAdmin(admin.ModelAdmin):
    list_display = ('id', 'destination')
    list_filter = ('destination',)
    inlines = [
        CommentInLineAdmin,
    ]


admin.site.register(Destination, DestinationAdmin)
admin.site.register(Like)
admin.site.register(Comment)
