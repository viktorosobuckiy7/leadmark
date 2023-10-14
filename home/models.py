from django.db import models
from django.core.validators import RegexValidator
import uuid
import os


class Service(models.Model):
    position = models.SmallIntegerField(unique=True)
    name = models.CharField(unique=True, max_length=30, db_index=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)


class Portfolio(models.Model):
    def get_file_name(self,filename: str):
        ext_file = filename.strip().split(('.'[-1]))
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('portfolio/', new_filename)

    name = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to=get_file_name)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('service',)


class AboutUs(models.Model):

    def get_file_name(self,filename: str):
        ext_file = filename.strip().split(('.'[-1]))
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('about_us/', new_filename)

    title = models.CharField(max_length=30, unique=True)
    subtitle = models.CharField(max_length=30)
    fst_descriptions = models.TextField(max_length=400)
    lg_image = models.ImageField(upload_to=get_file_name)
    sm_image1 = models.ImageField(upload_to=get_file_name)
    sm_image2 = models.ImageField(upload_to=get_file_name)
    lst_descriptions = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.title}'


class Blog(models.Model):

    def get_file_name(self, filename: str):
        ext_file = filename.strip().split(('.'[-1]))
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('blog/', new_filename)

    image = models.ImageField(upload_to=get_file_name)
    title = models.CharField(max_length=20, unique=True)
    subtitle = models.CharField(max_length=30, blank=True)
    small_text = models.CharField(max_length=20)
    date = models.DateField(blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('date',)


class UserReservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=50)
    massage = models.TextField(max_length=700)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}, {self.massage[:50]} '

    class Meta:
        ordering = ('subject', '-is_processed')

