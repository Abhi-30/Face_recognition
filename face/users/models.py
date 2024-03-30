from django.db import models

# Create your models here.
class User(models.Model):
    user_no = models.IntegerField(default=0)  # Field to store the user number
    image_encoding = models.BinaryField(null=True,blank=True)
    image = models.ImageField(upload_to='user_images/',null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.id:  # Check if the user is being created for the first time
            last_user = User.objects.order_by('-user_no').first()
            if last_user:
                self.user_no = last_user.user_no + 1
            else:
                self.user_no = 1
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"user{self.user_no}"
