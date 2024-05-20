# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.contrib.auth.models import Group, Permission

# class User(AbstractUser):
#     phone_number = models.CharField(max_length=20, blank=True, null=True)
#     birth_date = models.DateField(blank=True, null=True)

#     class Meta(AbstractUser.Meta):
#         db_table = 'auth_user'
#         swappable = 'AUTH_USER_MODEL' 

#     groups = models.ManyToManyField(Group, related_name='catalog_user_groups')
#     user_permissions = models.ManyToManyField(Permission, related_name='catalog_user_permissions')


#     def __str__(self):
#         return self.username
