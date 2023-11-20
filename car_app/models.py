from django.db import models


# Create your models here.

class reg_seller(models.Model):
    fullname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    profilepic = models.FileField(upload_to='car_app/static')
    companyname = models.CharField(max_length=30)
    companyemail = models.EmailField()
    companyphone = models.IntegerField()
    companyaddress = models.CharField(max_length=50)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.fullname


class upload_product(models.Model):
    choice_1 = [
        ('PETROL', 'petrol'),
        ('DIESEL', 'diesel'),
        ('EV', 'ev')
    ]
    choice_2 = [
        ('1st OWNER', 'owner1'),
        ('2nd OWNER', 'owner2'),
        ('3rd OWNER', 'owner3')
    ]
    choice_3 = [
        ('SEDAN', 'sedan'),
        ('SUV', 'suv'),
        ('HATCHBACK', 'hatchback')
    ]

    image = models.FileField(upload_to='car_app/static')
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    km = models.IntegerField()
    price = models.IntegerField()
    fuel = models.CharField(max_length=30, choices=choice_1)
    owner = models.CharField(max_length=30, choices=choice_2)
    category = models.CharField(max_length=30, choices=choice_3)

    def __str__(self):
        return self.name


class reg_buyer(models.Model):
    choice = [
        ('MALE', 'male'),
        ('FEMALE', 'female'),
        ('OTHER', 'other')
    ]
    fullname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    profilepic = models.FileField(upload_to='car_app/static')
    address = models.CharField(max_length=30)
    email = models.EmailField()
    gender = models.CharField(max_length=30, choices=choice)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.fullname


class wish(models.Model):
    userid = models.IntegerField()
    pro_id = models.IntegerField()
    pro_img = models.FileField()
    pro_name = models.CharField(max_length=30)
    pro_des = models.CharField(max_length=30)
    pro_km = models.IntegerField()
    pro_price = models.IntegerField()
    pro_fuel = models.CharField(max_length=30)
    pro_owner = models.CharField(max_length=30)
    pro_category = models.CharField(max_length=30)

    def __str__(self):
        return self.pro_name


class cart(models.Model):
    userid = models.IntegerField()
    pro_id = models.IntegerField()
    pro_img = models.FileField()
    pro_name = models.CharField(max_length=30)
    pro_des = models.CharField(max_length=30)
    pro_km = models.IntegerField()
    pro_price = models.IntegerField()
    pro_fuel = models.CharField(max_length=30)
    pro_owner = models.CharField(max_length=30)
    pro_category = models.CharField(max_length=30)
    quantity = models.IntegerField()

    def __str__(self):
        return self.pro_name


class delivery_address(models.Model):
    userid = models.IntegerField()
    fullname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    postal = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.fullname


class details_full(models.Model):
    userid = models.IntegerField()
    address = models.CharField(max_length=300)
    product_list = models.CharField(max_length=300)
    total_price = models.IntegerField()
    order_date = models.DateField(auto_now_add=True)
    estimated_date = models.DateField()

    def __str__(self):
        return self.address
