from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator


STATUS = [
        ("P","Pendente"),
        ("C","Cancelado(a)"),
        ("A","Aprovado(a)")
]

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Trip(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    daily = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    categoryFK = models.ForeignKey(Category, related_name='categoryTrip', on_delete=models.CASCADE)
    createdDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    
class Image(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=500)   
    tripFk = models.ForeignKey(Trip, related_name='tripImage', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    taxId = models.CharField(max_length=30)

    def __str__(self):
        return self.user.email

@receiver(post_save, sender=User)
def create_user_custom(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_custom(sender, instance, created, **kwargs):
    instance.customuser.save()


class Booking(models.Model):
    customUserFK = models.ForeignKey(CustomUser, related_name='customUserBooking', on_delete=models.CASCADE)
    tripFK = models.ForeignKey(Trip, related_name='trip', on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    purchaseValue = models.DecimalField(max_digits=10,decimal_places=2,null=True, blank=True)
    people = models.IntegerField()
    hasPet = models.BooleanField(default=False)
    comment = models.CharField(max_length=400, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    createdDate = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS, default="P")

    def __str__(self):
        return self.tripFK.title
    
    def save(self, *args, **kwargs):
        daily = self.tripFK.daily
        days = abs(self.endDate - self.startDate).days        
        self.purchaseValue = daily * days
        super(Booking, self).save(*args, **kwargs)


class Payment(models.Model):
    PAYMENT_CATEGORIES = [
        ("PIX","PIX"),
        ("BS","BANK SLIP"),
        ("CC","CREDIT CARD"),
        ("CD","DEBT CARD"),
    ]


    data = models.CharField(max_length=1000)
    bookingFK = models.ForeignKey(Booking, related_name='bookingPayment', on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.CharField(max_length=100, choices=PAYMENT_CATEGORIES)
    status = models.CharField(max_length=100, choices=STATUS, default="P")
    createdDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.data
    

class Availability(models.Model):
    tripFK = models.ForeignKey(Trip, related_name="tripAvailability", on_delete=models.CASCADE)
    bookingFK = models.ForeignKey(Booking, related_name="bookingAvailability", on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.tripFK.title + '-' + str(self.date)
