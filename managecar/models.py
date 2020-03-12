from django.db import models
from django.db.models.fields import CharField, DateTimeField
from django.forms.fields import ImageField
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Car(models.Model):

    CATEGORY_CAR = (
        ('SUV','Sport Utility Vehicle'),
        ('PPV', 'Pick-Up Passenger Vehicle'),
        ('MPV','Multi Purpose Vehicle'),
        ('ECO','Eco Car'),
        ('HEV','Hybrid Electric Vehicles'),
        ('EV', 'Electric Vehicles'),
        ('PU', 'Pick-Up Truck'),
        ('VAN', 'Van Car'),
        ('SED', 'Sedan'),
        ('SUP', 'Supercar'),
        ('COP','Coupe')
    )

    # COLOR = (
    #     ('BLUE','น้ำเงิน'),
    #     ('RED','แดง'),
    #     ('PINK','ชมพู'),
    #     ('ORANGE','ส้ม'),
    #     ('BLACK','ดำ'),
    #     ('WHI','ขาว'),
    #     ('SILVER','เงิน'),
    #     ('BRONZ','บรอนซ์'),
    #     ('YELLOW','เหลือง'),
    #     ('Green', 'เขียว')
    # )

    TYPE_GEAR = (
        ('AUTO','เกียร์ธรรมดา'),
        ('MANUAL','เกียร์อัตโนมัติ'),
        ('CBT','เกียร์ CVT'),
        ('DTC','เกียร์กึ่งอัตโนมัติ และ เกียร์คลัตช์คู่ DCT')
    )

    STATUS = (
        ('AVAILABLE','ว่าง'),
        ('NO_AVAILABLE','ไม่ว่าง'),
        ('HIDE','ซ่อน')
    )

    name = models.CharField(max_length=60)
    years = models.CharField(max_length=4)
    color = models.CharField(max_length=20)
    category = models.CharField(max_length=3, choices=CATEGORY_CAR)
    type_gear = models.CharField(max_length=10, choices=TYPE_GEAR)
    number_seat = models.SmallIntegerField()
    number_door = models.SmallIntegerField()
    status = models.CharField(max_length=12, choices=STATUS)
    price = models.FloatField()
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)
    pic_url = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.name + " " + self.years + " ("+ self.status+")"
    

class Promo(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=50)
    promotion_code = models.CharField(max_length=8,unique=True)
    discount_percent = models.FloatField()
    minimum_cost = models.FloatField()
    expire_day = models.DateTimeField()
    is_active = models.BooleanField()

class Rent(models.Model):
    STATUS = (
        ('Picked','รับรถเเล้ว'),
        ('Approved','ยืนยัน'),   
        ('Denied','ปฎิเสษ'),
        ('Returned','คืนเเล้ว'),
        ('Pending','รอการยืนยัน')
    )
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)
    status = models.CharField(max_length=8, choices=STATUS)
    total_price = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    car_id = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    customer_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    promotion = models.ForeignKey(Promo, on_delete=models.DO_NOTHING, null=True)



    
    
    

