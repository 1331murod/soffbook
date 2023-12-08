from django.db import models
from django.core.validators import RegexValidator




class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50,
                                     validators=[RegexValidator(r'^\+998\d{9}$')])
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to="poster/", null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} - {self.phone_number}"

class Ganre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category (models.Model):
     title = models.CharField(max_length=50)

     def __str__(self):
        return self.title

class Period(models.Model):
     name = models.CharField(max_length=50)
     
     def __str__(self):
        return self.name

class Authors(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Avtorning to'liq ismi")
    image = models.ImageField(upload_to="images/", verbose_name="Avtor rasmi")
    bio = models.TextField(verbose_name="Author haqida ma'lumot")
    country = models.CharField(max_length=200, verbose_name="Mamlakati")
    birth_date = models.PositiveIntegerField(verbose_name="Tug'ulgan sanasi")
    death_date =  models.PositiveIntegerField(verbose_name="Vafot etgan sanasi")
    order = models.IntegerField(default=1)
    period = models.ForeignKey(Period,on_delete=models.PROTECT,related_name='period')

    class Meta:
        ordering = ('order', )

    def __str__(self):
        return self.full_name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to="images/", verbose_name="Kitob muqovasi")
    pages = models.IntegerField(verbose_name="Varoqlar soni")
    published = models.PositiveIntegerField(verbose_name="Nashr qilingan sanasi")
    price = models.PositiveIntegerField(verbose_name="kitob narxi")
    ganre = models.ForeignKey(Ganre,on_delete=models.PROTECT,related_name='kitobning_ganri')
    description = models.TextField()
    author = models.ForeignKey(Authors, on_delete=models.PROTECT, related_name='author_books')
    order = models.IntegerField(default=1)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True, related_name='category_books')
    
    class Meta:
        ordering = ('order', )

    def __str__(self):
        return str(self.title)




