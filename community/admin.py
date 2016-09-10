from django.contrib import admin

# import Models
from .models import UserInfo, Board, Post, AttachFile, AttachImage

admin.site.register(UserInfo)
admin.site.register(Board)
admin.site.register(Post)
admin.site.register(AttachFile)
admin.site.register(AttachImage)