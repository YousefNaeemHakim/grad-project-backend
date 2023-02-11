import datetime
from django.db import models
  
  
# Create your models here.
  
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name



class Book(models.Model):
    name = models.CharField(max_length=60)
    aouthor_name = models.CharField(max_length=60)
    availability = models.BooleanField(default=True)
    publication_date = models.DateField(default=datetime.datetime.today)
    author_summary = models.TextField(blank=True, max_length=120)
    rating = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField( max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.name



class Discount_copon (models.Model):
    name = models.ForeignKey(Book,on_delete=models.CASCADE)
    code = models.IntegerField()
    id = models.IntegerField()
    validate_from = models.DateField()
    validate_to = models.DateField()
    discount = models.IntegerField()

    def __str__(self):
        return self.code



BOOK_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
)


class Buy(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    cupon = models.ForeignKey(Discount_copon,on_delete=models.CASCADE)
    payment_id = models.IntegerField()
    payment_date = models.DateTimeField(default=datetime.datetime.today)
    quantity = models.CharField(
        max_length = 20,
        choices = BOOK_CHOICES,
        default = '1'
        )
  
    def __str__ (self):
        return self.save()         



class refund (models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE) 
    payment_id = models.IntegerField(max_length=10)
    payment_date = models.DateField(default=datetime.datetime.today)
    reason = models.TextField(max_length=120)
    is_accepted = models.BooleanField(default=False)

    def __str__(self) :
        return self.book.name



class rate(models.Model) : 
    book = models.ForeignKey(Book,on_delete=models.CASCADE)  
    def __str__(self) :
        return self.book.name


class add(models.models):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    adding_date = models.DateField(default=datetime.datetime.today)        