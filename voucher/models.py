from django.db import models
from djmoney.models.fields import MoneyField
from django.template.defaultfilters import slugify
from django.urls import reverse



class MinistryOrAgency(models.Model):
    mda = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True, max_length=255)

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.category)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.mda


class Voucher(models.Model):
    TEAM_TYPE_CHOICES = (
        ('governor', 'Governor'),
        ('budget', 'Budget'),
        ('accoutant_general', 'Accountant General'),
    )


    ministry_or_agency = models.ForeignKey(MinistryOrAgency, on_delete=models.CASCADE)
    voucher_number = models.CharField(max_length=50, unique=True)
    date_on_voucher = models.DateField()
    date_of_voucher_approval = models.DateField()
    approved_by = models.CharField(max_length=50, choices=TEAM_TYPE_CHOICES)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='NGN')
    voucher_code = models.CharField(max_length=50, unique=True)
    upload_voucher = models.FileField(upload_to='media/voucher', blank=False, null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.voucher_number
