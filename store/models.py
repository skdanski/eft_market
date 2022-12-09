from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Product(models.Model):
    DRAFT = 'draft'
    WAITING_APPROVAL = 'waitingapproval'
    ACTIVE = 'active'
    DELETED = 'deleted'
    CLOSED = 'closed'
    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (WAITING_APPROVAL, 'Waiting Approval'),
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted'),
        (CLOSED, 'Bid Closed'),
    )

    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)
    trade_location = models.CharField(max_length=255)
    phone_num = models.CharField(max_length=20)

    price = models.IntegerField()
    currentPrice = models.IntegerField()
    suggestedPrice = models.IntegerField()

    image = models.ImageField(upload_to='uploads/product_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(blank=True, default=timezone.now)



    def __str__(self):
        return self.title

    def get_display_price(self):
        return self.price / 100

    def get_current_price(self):
        return self.currentPrice / 100
    