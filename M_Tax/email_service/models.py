from django.db import models

class Mail(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    
    # The email field will not be unique, allowing the same email to be used multiple times.
    email = models.EmailField(max_length=254, default='abxc@gmail.com')

    slug = models.SlugField(max_length=250, unique=True)

    mobile = models.CharField(max_length=16, blank=True, help_text='Enter your mobile number')  # Mobile is optional

    message = models.TextField(default="this is simple message")  # Default message text
    
    # Optional image field if you want to allow users to upload images.
    # image = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'E-mails'

    def __str__(self):
        return self.name