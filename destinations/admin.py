from django.contrib import admin

from destinations.models import Destination, Like, Comment


class LikeInLineAdmin(admin.TabularInline):
    model = Like

class DestinationAdmin(admin.ModelAdmin):
    list_display = ('id', 'destination')
    list_filter = ('destination',)
    inlines = [
        LikeInLineAdmin,
    ]


admin.site.register(Destination, DestinationAdmin)
admin.site.register(Like)
admin.site.register(Comment)
