from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from app_dir.marketing.utils import Mailchimp

User = settings.AUTH_USER_MODEL


class MarketingPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=True)
    mailchimp_subscribed = models.NullBooleanField(blank=True)
    mailchimp_msg = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=MarketingPreference)
def marketing_pref_create_receiver(sender, instance, created, *args, **kwargs):
    if created:
        status_code, response_data = Mailchimp().subscribe(instance.user.email)
        print(status_code, response_data)


@receiver(pre_save, sender=MarketingPreference)
def marketing_pref_update_receiver(sender, instance, *args, **kwargs):
    if instance.subscribed != instance.mailchimp_subscribed:
        if instance.subscribed:
            # subscribing user
            status_code, response_data = Mailchimp().add_email(instance.user.email)
            if response_data['title'] == 'Member Exists':
                status_code, response_data = Mailchimp().subscribe(instance.user.email)
        else:
            # unsubscribe user
            status_code, response_data = Mailchimp().unsubscribe(instance.user.email)

        if response_data['status'] == 'subscribed':
            instance.subscribed = True
            instance.mailchimp_subscribed = True
            instance.mailchimp_msg = response_data
        else:
            instance.subscribed = False
            instance.mailchimp_subscribed = False
            instance.mailchimp_msg = response_data


@receiver(post_save, sender=User)
def make_marketing_pref_receiver(sender, instance, created, *args, **kwargs):
    if created:
        MarketingPreference.objects.get_or_create(user=instance)
