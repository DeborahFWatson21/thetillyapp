# from email.policy import default
# from django.db import models
# from django.contrib.auth.models import User
# import uuid
# import os


# def business_logo_file(instance,filename):
#     """Generate file path for new business logo."""
#     ext = os.path.splitext(filename)[1]
#     filename = f'{uuid.uuid4()}{ext}'

#     return os.path.join('uploads', 'logo', filename) 





# class Profile(models.Model):
#     profile_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#     date_created = models.DateTimeField(auto_now_add=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, black=True)
#     primary_number = models.CharField(max_length=20,null=True, blank=True)
    
#     def __str__(self):
#         return '{} {}'.format(self.user.first_name,self.user.last_name)

# class Business:
#     business_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
