# import Django modules
from django.db import models
from django.conf import settings

# import Python modules
from datetime import date, datetime

# Custom User Model for Email User
User = settings.AUTH_USER_MODEL


# Abstract Class
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class UserDoingModel(TimeStampModel):
    user = models.OneToOneField(User)

    class Meta:
        abstract=True


# Basic UserInfo
class UserInfo(UserDoingModel):
    student_num = models.CharField(max_length=9, default='0')
    is_student = models.BooleanField(default=False) #if True: 재학생
    is_testtaker = models.BooleanField(default=False) #if True: 임고생

    @property
    def default_grade(self):
        this_year = int(date.today().strftime('%Y'))
        if (int(date.today().strftime('%m')) > 10):
            winter_season = 1
        else:
            winter_season = 0
        if int(self.student_num) > (this_year-3-winter_season)*10000:
            return 4
        elif int(self.student_num) > (this_year-2-winter_season)*10000:
            return 3
        elif int(self.student_num) > (this_year-1-winter_season)*10000:
            return 2
        elif int(self.student_num) > (this_year-0-winter_season)*10000:
            return 1
        return 0

    def __str__(self):
        return self.user.email


# Basic Board
class Board(TimeStampModel):
    name = models.CharField(max_length=100)
    lock_to_studnet = models.BooleanField(default=True) #재학생 게시판
    lock_to_testtakcer = models.BooleanField(default=False) #임고생 게시판

    def __str__(self):
        return self.name


class Post(UserDoingModel):
    board = models.ForeignKey(Board)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class AttachFile(UserDoingModel):
    post = models.ForeignKey(Post)
    file = models.FileField()

    def __str__(self):
        return self.file.name


class AttachImage(UserDoingModel):
    post = models.ForeignKey(Post)
    image = models.ImageField()

    def __str__(self):
        return self.image.name