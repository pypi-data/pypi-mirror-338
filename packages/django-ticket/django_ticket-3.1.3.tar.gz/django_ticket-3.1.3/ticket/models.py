import datetime
from datetime import timezone
from enum import Enum

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _

User = get_user_model()


class TicketOptions(Enum):
    # status
    PENDING = "pending"
    PENDING_LABEL = _("Pending")
    ANSWERED = "answered"
    ANSWERED_LABEL = _("Answered")
    CLOSED = "closed"
    CLOSED_LABEL = _("Closed")

    # section
    MANAGEMENT = "management"
    MANAGEMENT_LABEL = _("Management")
    FINANCES = "finances"
    FINANCES_LABEL = _("Finances")
    SUPPORT = "support"
    SUPPORT_LABEL = _("Support")

    # priority
    LOW = "low"
    LOW_LABEL = _("Low")
    MEDIUM = "medium"
    MEDIUM_LABEL = _("Medium")
    HIGH = "high"
    HIGH_LABEL = _("High")


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    status = models.CharField(
        max_length=255,
        choices=[
            (TicketOptions.PENDING.value, TicketOptions.PENDING_LABEL.value),
            (TicketOptions.ANSWERED.value, TicketOptions.ANSWERED_LABEL.value),
            (TicketOptions.CLOSED.value, TicketOptions.CLOSED_LABEL.value),
        ],
        default=TicketOptions.PENDING,
    )
    section = models.CharField(
        max_length=128,
        choices=[
            (TicketOptions.MANAGEMENT.value, TicketOptions.MANAGEMENT_LABEL.value),
            (TicketOptions.FINANCES.value, TicketOptions.FINANCES_LABEL.value),
            (TicketOptions.SUPPORT.value, TicketOptions.SUPPORT_LABEL.value),
        ],
        default=TicketOptions.SUPPORT.value,
    )

    priority = models.CharField(
        max_length=128,
        choices=[
            (TicketOptions.LOW.value, TicketOptions.LOW_LABEL.value),
            (TicketOptions.MEDIUM.value, TicketOptions.MEDIUM_LABEL.value),
            (TicketOptions.HIGH_LABEL.value, TicketOptions.HIGH_LABEL.value),
        ],
        default=TicketOptions.LOW.value,
    )
    seen_by_user = models.BooleanField(default=False, verbose_name=_("Seen by user"))
    seen_by_admin = models.BooleanField(default=False, verbose_name=_("Seen by admin"))

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    soft_delete = models.BooleanField(default = False)
    def __str__(self):
        return f"{self.id}:{self.title}"

    class Meta:
        verbose_name = _("Ticket")
        verbose_name_plural = _("Tickets")


class TicketMessage(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    viewed = models.DateTimeField(null=True)
    viewer = models.ForeignKey(User, on_delete=models.CASCADE, null=True , related_name='admin_viewer')
    soft_delete = models.BooleanField(default=False)
    def __str__(self):
        return ""

    class Meta:
        verbose_name = _("Ticket Message")
        verbose_name_plural = _("Ticket Messages")
