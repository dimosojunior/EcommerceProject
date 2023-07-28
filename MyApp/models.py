from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django_countries.fields import CountryField
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("Your username is required")
        
        

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,

        )
        user.is_admin=True
        user.is_staff=True
        
        user.is_superuser=True
        user.save(using=self._db)
        return user

    



class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="user name", max_length=100, unique=True)
    middle_name=models.CharField(verbose_name="middle name", max_length=100, unique=False)
    last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    company_name=models.CharField(verbose_name="company name", max_length=100, unique=False)
    phone=models.CharField(verbose_name="phone",default="+255", max_length=13)
    
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username

    


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True







class Category(models.Model):
	#id = models.CharField(max_length=100, primary_key=True)
	CategoryName = models.CharField(max_length=100)
	link = models.CharField(max_length=200)
	description = models.TextField(max_length=500, blank=True, null=True)
	image = models.ImageField(upload_to="CategoryImages/",blank=True, null=True)
	recorded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	updated_at = models.DateTimeField(auto_now = True, blank=True, null=True)

	def __str__(self):
	    return self.CategoryName
	def get_absolute_url(self):
	    return reverse('product_by_category', args=[self.id])
	class Meta:
	    verbose_name_plural = "Categories"




class ProductsCategory(models.Model):
    #id = models.CharField(max_length=100, primary_key=True)
    CategoryName = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to="CategoryImages/",blank=True, null=True)
    recorded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now = True, blank=True, null=True)

    def __str__(self):
        return self.CategoryName
    class Meta:
        verbose_name_plural = "ProductsCategories"







class Products(models.Model):
    #id = models.CharField(max_length=100, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #product_category = models.ForeignKey(ProductsCategory, on_delete=models.CASCADE)
    ProductName = models.CharField(max_length=100)
    ProductPrice = models.IntegerField(blank=True, null=True)
    ProductDiscountPrice = models.IntegerField(blank=True, null=True)
    ProductPackage = models.CharField(max_length=100, blank=True, null=True)
    ProductQuantity = models.IntegerField(blank=True, null=True)
    MemorySize = models.CharField(max_length=100, blank=True, null=True)
    MemoryType = models.CharField(max_length=100, blank=True, null=True)
    AuthorizedDistributers = models.CharField(max_length=100, blank=True, null=True)
    Guarantee = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to="ProductImages/",blank=True, null=True)
    Status_Choices = (
            
            ("New", "New"),
            ("Old", "Old"),
            
            
        )
    ProductStatus = models.CharField(max_length=100, choices=Status_Choices, blank=True, null=True)

    SimilarImage1 = models.ImageField(upload_to="SimilarPartsImages_1/",blank=True, null=True)
    SimilarImage2 = models.ImageField(upload_to="SimilarPartsImages_2/",blank=True, null=True)
    SimilarImage3 = models.ImageField(upload_to="SimilarPartsImages_3/",blank=True, null=True)
    SimilarImage4 = models.ImageField(upload_to="SimilarPartsImages_4/",blank=True, null=True)
    SimilarImage5 = models.ImageField(upload_to="SimilarPartsImages_5/",blank=True, null=True)
    SimilarImage6 = models.ImageField(upload_to="SimilarPartsImages_6/",blank=True, null=True)
    SimilarImage7 = models.ImageField(upload_to="SimilarPartsImages_7/",blank=True, null=True)
    SimilarImage8 = models.ImageField(upload_to="SimilarPartsImages_8/",blank=True, null=True)
    SimilarImage9 = models.ImageField(upload_to="SimilarPartsImages_9/",blank=True, null=True)

    SimilarImage10 = models.ImageField(upload_to="SimilarPartsImages_10/",blank=True, null=True)
    SimilarImage11 = models.ImageField(upload_to="SimilarPartsImages_11/",blank=True, null=True)
    SimilarImage12 = models.ImageField(upload_to="SimilarPartsImages_12/",blank=True, null=True)
    SimilarImage13 = models.ImageField(upload_to="SimilarPartsImages_13/",blank=True, null=True)
    SimilarImage14 = models.ImageField(upload_to="SimilarPartsImages_14/",blank=True, null=True)
    SimilarImage15 = models.ImageField(upload_to="SimilarPartsImages_15/",blank=True, null=True)
    SimilarImage16 = models.ImageField(upload_to="SimilarPartsImages_16/",blank=True, null=True)
    SimilarImage17 = models.ImageField(upload_to="SimilarPartsImages_17/",blank=True, null=True)
    SimilarImage18 = models.ImageField(upload_to="SimilarPartsImages_18/",blank=True, null=True)
    # ZA UMUHIMU ZINAISHIA HAPA


    OS = models.CharField(max_length=100, blank=True, null=True)
    ScreenSize = models.CharField(max_length=100, blank=True, null=True)
    ProcessorType = models.CharField(max_length=100, blank=True, null=True)
    RAM = models.CharField(max_length=100, blank=True, null=True)
    InternalStorage = models.CharField(max_length=100, blank=True, null=True)
    ExternalStorage = models.CharField(max_length=100, blank=True, null=True)
    # ZA UMUHIMU KIDOGO ZINAISHIA HAPA


    SIMType = models.CharField(max_length=100, blank=True, null=True)
    RearCamera = models.CharField(max_length=100, blank=True, null=True)
    FrontCamera = models.CharField(max_length=100, blank=True, null=True)
    Battery = models.CharField(max_length=100, blank=True, null=True)
    

    description = models.TextField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to="ProductImages/",blank=True, null=True)

    D1 = models.CharField(default="Dimoso", max_length=100, blank=True, null=True)
    D2 = models.CharField(default="Shukuru", max_length=100, blank=True, null=True)
    D3 = models.CharField(default="Isaack", max_length=100, blank=True, null=True)
    D4 = models.CharField(default="Junior", max_length=100, blank=True, null=True)
    D5 = models.CharField(default="El Jr", max_length=100, blank=True, null=True)

    D1_place = models.CharField(default="Magomeni", max_length=100, blank=True, null=True)
    D2_place = models.CharField(default="Mbeya", max_length=100, blank=True, null=True)
    D3_place = models.CharField(default="Arusha", max_length=100, blank=True, null=True)
    D4_place = models.CharField(default="Mwanza", max_length=100, blank=True, null=True)
    D5_place = models.CharField(default="Dodoma", max_length=100, blank=True, null=True)
    recorded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now = True, blank=True, null=True)

    ProductArchitecture = models.CharField(max_length=100, blank=True, null=True)

    
    MaxFrequency = models.CharField(max_length=100, blank=True, null=True)
    
    Peripherals = models.CharField(max_length=500, blank=True, null=True)
    MaxSupplyVoltage = models.CharField(max_length=100, blank=True, null=True)
    MinSupplyVoltage = models.CharField(max_length=100, blank=True, null=True)
    



    def __str__(self):
        return self.ProductName
    def get_add_to_cart_url(self):
        return reverse('add_to_cart', kwargs={'pk': self.pk})
    def get_remove_from_cart_url(self):
        return reverse('remove_from_cart', kwargs={'pk': self.pk})

    def get_add_to_cart_url2(self):
        return reverse('add_to_cart2', kwargs={'pk': self.pk})
    def get_remove_from_cart_url2(self):
        return reverse('remove_from_cart2', kwargs={'pk': self.pk})
    
    def get_remove_single_from_cart_url(self):
        return reverse('remove_single_from_cart', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "Products"






class OrderItem(models.Model):
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    O_B = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.ProductName}"
    

    def get_total_item_price(self):
        return self.quantity * self.item.ProductPrice

    def get_total_item_discount_price(self):
        return self.quantity * self.item.ProductDiscountPrice

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_final_price()

    def get_final_price(self):
        if self.item.ProductDiscountPrice:
            return self.get_total_item_discount_price()
        return self.get_total_item_price()
    class Meta:
        verbose_name_plural = "OrderItems"

   


class Order(models.Model):
   # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
   
    ordered = models.BooleanField(default=False)
    O_B = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    address = models.ForeignKey(
        "Address", on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        "Payment", on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        "Coupon", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        # if self.coupon:
        #     total -= self.coupon.amount
        
        
        return total
    class Meta:
        verbose_name_plural = "Orders"



class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=200)
    apartment_address = models.CharField(max_length=200)
    country = CountryField(multiple=False)

    zip = models.CharField(max_length=200)
    save_info = models.BooleanField(default=False)
    default = models.BooleanField(default=False)
    use_default = models.BooleanField(default=False)
    PAYMENT_CHOICES = (
    ('S', 'M-PESA'),
    ('P', 'TIGO PESA'),
    ('H', 'HALO PESA'),
    ('A', 'AIRTEL MONEY'),
)

    payment_option = models.CharField(choices=PAYMENT_CHOICES, max_length=2)

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return self.user.username


class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    charge_id = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name_plural = 'Payments'


class Coupon(models.Model):
    code = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return self.code
    class Meta:
        verbose_name_plural = 'Coupons'









class ContactMe(models.Model):
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(max_length=1000, blank=True, null=True)
    
    username = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default='+255',max_length=13, blank=True, null=True)
    email = models.EmailField(default='@gmail.com', blank=True, null=True)
    place = models.CharField(max_length=200, blank=True, null=True)
    
    send_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    #to_dimoso_email = models.EmailField(default='juniordimoso8@gmail.com', blank=True, null=True)

    def __str__(self):
        return self.username
    class Meta:
        verbose_name_plural = "ContactMe"




class Ask(models.Model):
    username = models.CharField(max_length=200)
    phone = models.CharField(default='+255',max_length=13)
    email = models.EmailField(default='@gmail.com')
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.username
    class Meta:
        verbose_name_plural = "Ask"


class PrivacyPolicy(models.Model):
    #id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)
    
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to="PrivacyPolicy/",blank=True, null=True)
    recorded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now = True, blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "PrivacyPolicy"
