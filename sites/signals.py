from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Site


@receiver(post_save, sender=Site)
def send_email_site(sender, **kwargs):
    pass
