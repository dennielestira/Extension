from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Document

@receiver(pre_save, sender=Document)
def set_uploaded_by_name(sender, instance, **kwargs):
    if instance.uploaded_by and not instance.uploaded_by_name:
        instance.uploaded_by_name = instance.uploaded_by.get_full_name() or instance.uploaded_by.username
    if instance.recommended_by and not instance.recommended_by_name:
        instance.recommended_by_name = instance.recommended_by.get_full_name() or instance.recommended_by.username
    if instance.approved_by and not instance.approved_by_name:
        instance.approved_by_name = instance.approved_by.get_full_name() or instance.approved_by.username
