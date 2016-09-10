from django.contrib import admin

# import Models
from .models import UserInfo, BoardGroup, Board, Post, AttachFile, AttachImage

#UserInfo
admin.site.register(UserInfo)

#Boards
admin.site.register(BoardGroup)
admin.site.register(Board)
admin.site.register(Post)
admin.site.register(AttachFile)
admin.site.register(AttachImage)