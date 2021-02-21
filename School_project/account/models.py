# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# from django.utils.translation import gettext_lazy as _
#
#
# # from School_project.school.models import Address,Class
#
# class UserManager(BaseUserManager):
#     def create_user(self,email,username,password,**other_fields):
#         if not email:
#             raise ValueError(_("You must provide email address"))
#         email = self.normalize_email(email)
#         user = self.model(email=email, username=username, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_superuser(self,email,username,password,**other_fields):
#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)
#         other_fields.setdefault('is_active', True)
#         if other_fields.setdefault('is_staff') is not True:
#             raise ValueError("Super user must be is_staff=True")
#         if other_fields.setdefault('is_superuser') is not True:
#             raise ValueError("Super user must be is_superuser=True")
#
#         return self.create_user(email, username, password=password, **other_fields)
#
#
#
#
# class User(AbstractBaseUser,PermissionsMixin):
#     email = models.EmailField(_("Email"),unique=True)
#     username = models.CharField(_("Username"),unique=True,max_length=100)
#     is_active = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     object = UserManager()
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']
#
#     def __str__(self):
#         return self.username
#
#
# class AccountManagerTeacher(BaseUserManager):
#     pass
#
#
# class AccountManagerStudent(BaseUserManager):
#     pass
#
#
# class TeacherUser(User):
#     full_name = models.CharField(max_length=200)
#
#     # address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
#     file = models.FileField()
#     profile_image = models.ImageField()
#     # related_class = models.ManyToManyField(Class)
#     approved = models.BooleanField()
#
#     def __str__(self):
#         return self.full_name
#
# #
# # class Student(User):
# #     full_name = models.CharField(max_length=255, unique=True)
# #     date_of_birth = models.DateField(blank=False)
# #     email_address = models.EmailField(max_length=100)
# #     age = models.IntegerField()
# #     # address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
# #     approved = models.BooleanField()
