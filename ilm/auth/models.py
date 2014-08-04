from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    """
    Extending django auth system.
    """
    mobile_number = models.CharField(max_length=120, null=True)
    gender = models.CharField(max_length=100, null=True)
    karma = models.CharField(max_length=120, null=True)
    status = models.BooleanField(default=True)

    def full_name(self):
    	"""
    	Returns full name of the user.
    	"""
    	if self.first_name and self.last_name:
    		return "{} {}".format(self.first_name, self.last_name)

    def __unicode__(self):
    	"""
    	Shows the object readable name.
    	"""
    	return self.first_name