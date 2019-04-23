from django.db import models

from app_dir.billing.models import BillingProfile

ADDRESS_TYPES = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping'),
)


class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=120, choices=ADDRESS_TYPES)
    address_line_1 = models.CharField(max_length=120)
    address_line_2 = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120, default='United States of America')
    state = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.billing_profile)

    def get_address(self):
        return f"" \
            f"{self.address_line_1}" \
            f"{self.address_line_2}" \
            f"{self.city}" \
            f"{self.state}, " \
            f"{self.postal_code}" \
            f"{self.country}"
