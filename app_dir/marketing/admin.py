from django.contrib import admin

from .models import MarketingPreference


class MarketingPreferenceAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'subscribed', 'updated_at']
    readonly_fields = ['mailchimp_msg', 'mailchimp_subscribed', 'created_at', 'updated_at']

    class Meta:
        model = MarketingPreference
        fields = [
            'user',
            'subscribed',
            'mailchimp_msg',
            'mailchimp_subscribed',
            'created_at',
            'updated_at'
        ]


admin.site.register(MarketingPreference, MarketingPreferenceAdmin)
