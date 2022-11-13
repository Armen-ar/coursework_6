from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


# admin.site.register(UserAdmin)
admin.site.register(User)
