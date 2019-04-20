from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class BillingProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # customer_id in Stripe or Braintree

    def __str__(self):
        return self.email


# def billing_profile_created_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         print("ACTUAL API REQUEST Send to stripe/braintree")
#         instance.customer_id = newID
#         instance.save()

@receiver(post_save, sender=User)
def user_created_receiver(sender, instance, created, *args, **kwargs):
    if created:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)

