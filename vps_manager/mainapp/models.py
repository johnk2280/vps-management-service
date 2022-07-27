import uuid

from django.db import models


class VPS(models.Model):
    STARTED = 'started'
    BLOCKED = 'blocked'
    STOPPED = 'stopped'

    STATUS_CHOICES = (
        (STARTED, 'STARTED'),
        (BLOCKED, 'BLOCKED'),
        (STOPPED, 'STOPPED'),
    )

    uid = models.PositiveIntegerField(
        verbose_name='UID',
        primary_key=True,
    )
    cpu = models.PositiveSmallIntegerField(
        verbose_name='CPU cores count',
        null=False,
        blank=False,
    )
    ram = models.PositiveIntegerField(
        verbose_name='RAM volume',
        null=False,
        blank=False,
    )
    hdd = models.PositiveIntegerField(
        verbose_name='HDD volume',
        null=False,
        blank=False,
    )
    status = models.CharField(
        verbose_name='VPS status',
        max_length=7,
        choices=STATUS_CHOICES,
        default=STOPPED,
    )
    created_at = models.DateTimeField(
        verbose_name='Created at',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='Updated at',
        auto_now=True,
    )

    class Meta:
        db_table = 'vps'
        ordering = ('-created_at',)
        verbose_name = 'vps object'
        verbose_name_plural = 'vps objects'

    def __str__(self):
        return self.uid
