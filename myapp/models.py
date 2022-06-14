from django.db import models

# Create your models here.
STATE_CHOICE = (
    ('pradesh1','pradesh1'),
    ('pradesh2','pradesh2'),
    ('pradesh3','pradesh3'),
    ('pradesh4','pradesh4'),
    ('pradesh5','pradesh5'),
    ('pradesh6','pradesh6'),
    ('pradesh7','pradesh7'),
)

class Resume(models.Model):
    name = models.CharField(max_length=154)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=15)
    locality = models.CharField(max_length=154)
    city = models.CharField(max_length=154)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=154)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=154)
    profile_image = models.ImageField(upload_to='profileimg', blank=True)
    my_file = models.FileField(upload_to='doc', blank=True)

    def __str__(self):
        return self.email

