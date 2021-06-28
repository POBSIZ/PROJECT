from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

from profileapp.models import Profile


class UserManager(BaseUserManager):
    # Method Overriding
    def create_user(self, username, password, realname, email, phone, date_of_birth):
        user = self.model(
            username=username,
            realname=realname,
            email=self.normalize_email(email),
            phone=phone,
            date_of_birth=date_of_birth,
            date_joined=timezone.now(),
            is_superuser=0,
            is_staff=0,
            is_active=1,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    # Method Overriding
    def create_superuser(self, username, realname, email, phone, date_of_birth, password):
        user = self.create_user(
            username=username,
            password=password,
            realname=realname,
            email=email,
            phone=phone,
            date_of_birth=date_of_birth,
        )
        user.is_superuser = 1
        user.is_staff = 1

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    password = models.CharField(max_length=128)
    username = models.CharField(unique=True, max_length=150)
    is_superuser = models.IntegerField(blank=True, null=True)
    realname = models.CharField(max_length=128)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=256)
    date_of_birth = models.DateField()
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_staff = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['realname', 'phone', 'email', 'date_of_birth']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        db_table = 'auth_user'
