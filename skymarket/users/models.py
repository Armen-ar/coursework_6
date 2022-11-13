from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager, UserRoles
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser):
    first_name = models.CharField(verbose_name="Имя.", max_length=50, help_text="Введите имя.")
    last_name = models.CharField(verbose_name="Фамилия.", max_length=100, help_text="Введите фамилию.")
    phone = PhoneNumberField(verbose_name="Телефон.", max_length=20, help_text="Введите номер телефона.")
    email = models.EmailField(verbose_name="Логин.", unique=True,
                              help_text="Не более 150 символов, только буквы, цифры и @/./+/-/_ @/./+/-/_.", )
    role = models.CharField(verbose_name="Роль.", choices=UserRoles.choices, default=UserRoles.USER, max_length=12)
    image = models.ImageField(verbose_name="Аватарка.", upload_to="media/", null=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    class Meta:
        verbose_name = "Пользователь."
        verbose_name_plural = "Пользователи."

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return f"Уважаемый(ая) {self.first_name} {self.last_name}!"
