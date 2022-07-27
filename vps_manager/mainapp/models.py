import uuid

from django.db import models


class VPS(models.Model):
    STATUSES = (
        ('started', 'STARTED'),
        ('blocked', 'BLOCKED'),
        ('stopped', 'STOPPED'),
    )

    uid = models.UUIDField(
        verbose_name='UID',
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    cpu = models.SmallIntegerField(
        verbose_name='CPU cores count',
        null=False,
        blank=False,
    )
    ram = models.SmallIntegerField(
        verbose_name='RAM volume',
        null=False,
        blank=False,
    )
    hdd = models.SmallIntegerField(
        verbose_name='HDD volume',
        null=False,
        blank=False,
    )
    status = models.CharField(
        verbose_name='VPS status',
        max_length=7,
        choices=STATUSES,
        default='STOPPED',
    )
    created_at = models.DateTimeField(
        verbose_name='Created at',
        auto_now=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='Updated at',
        auto_now_add=True,
    )
