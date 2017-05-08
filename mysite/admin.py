from django.contrib import admin
from mysite import models

#show detail item('user', 'name', 'created_at', 'enabled') info at admin page
class PollAdmin(admin.ModelAdmin): 
    list_display = ('name', 'created_at', 'enabled')
    ordering = ('-created_at',)

#show detail item('poll', 'name', 'vote', 'image_url') info at admin page
class PollItemAdmin(admin.ModelAdmin): 
    list_display = ('poll', 'name', 'vote', 'image_url')
    ordering = ('poll',)

admin.site.register(models.Poll, PollAdmin)
admin.site.register(models.PollItem, PollItemAdmin)

"""
class PostAdmin(admin.ModelAdmin):
    list_display=('nickname', 'message', 'enabled', 'pub_time')
    ordering=('-pub_time',)
    
admin.site.register(models.Mood)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.User)

admin.site.register(models.Profile)
admin.site.register(models.Diary)
"""



