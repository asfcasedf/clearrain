from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER_CHOICES = [
        ("male", "男"),
        ("female", "女"),
        ("unknown", "未知"),
    ]

    nickname = models.CharField("昵称", max_length=50)
    gender = models.CharField("性别", max_length=10, choices=GENDER_CHOICES, default="unknown")
    grade = models.CharField("年级", max_length=20, blank=True, default="")
    major = models.CharField("专业", max_length=100, blank=True, default="")

    class Meta:
        db_table = "accounts_user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.username}({self.nickname})"
