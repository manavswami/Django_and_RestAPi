from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from django.db.models.signals import post_save
from django.dispatch import receiver


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self,phone_number , email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not phone_number:
            raise ValueError('The given phone_number must be set')
        email = self.normalize_email(email)
        
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, email, password, **extra_fields)

    def create_superuser(self, phone_number, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_number, email, password, **extra_fields)
















class User(AbstractBaseUser,PermissionsMixin):
    phone_number = PhoneNumberField(_('phone_number'),unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    id = models.AutoField(primary_key=True)
    is_admin = models.BooleanField(default=False)
    
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name','last_name','email']
 
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        swappable = 'AUTH_USER_MODEL'
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name


    def __str__(self):
        return str(self.phone_number)
   

class global_database(models.Model):
    # user=models.OneToOneField(User,on_delete="models.CASCADE")
    user_id=models.IntegerField(null=True,blank=True)
    spam=models.BooleanField(default=False)
    Name=models.CharField(max_length=30,null=False,blank=False)
    Phone_Number= PhoneNumberField('phone_number',unique=True)

    Email_Address=models.EmailField(null=True,blank=True)

    def __str__(self):
        return str(self.Phone_Number)


#automatically create global_database new entry whenn new user is created
@receiver(post_save,sender=User)
def user_is_created(sender, instance, created,**kwargs):
    if created:
        global_database.objects.create(Name=instance.first_name +" "+ instance.last_name,
        Phone_Number=instance.phone_number,Email_Address=instance.email,user_id=instance.id)
  

    else:
        q=global_database.objects.get(user_id=instance.id)

        q.Name=instance.first_name +" "+ instance.last_name
        q.Phone_Number=instance.phone_number
        q.Email_Address=instance.email
        q.user_id=instance.id
        q.save()


