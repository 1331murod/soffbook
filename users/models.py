from django.db import models
from django.contrib.auth.models import User,AbstractUser, UserManager
from django.core.validators import RegexValidator
from rest_framework_simplejwt.tokens import RefreshToken

class TestManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)



class TestUser(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username = None
    phone_number = models.CharField(max_length=50,
                                     validators=[RegexValidator(r'^\+998\d{9}$')])
    profile_picture = models.ImageField(upload_to="poster/", null=True, blank=True)
    email = models.EmailField(unique=True, verbose_name='Email')
    def __str__(self):
        return f"{self.first_name} - {self.phone_number}"
    

    def get_token(self):
        refresh = RefreshToken.for_user(self)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data

    objects = TestManager()