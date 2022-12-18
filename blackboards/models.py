import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Manager
from django.urls import reverse


class Board(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    board_name = models.CharField(max_length=100, unique=True, blank=False)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    users = models.ManyToManyField(get_user_model(), related_name="board_users", blank=True)
    password = models.CharField(max_length=50, blank=False)

    objects = Manager()

    def __str__(self):
        return self.board_name

    def get_absolute_url(self):
        return reverse('blackboard_detail', kwargs={'pk': str(self.pk)})


class ListTable(models.Model):
    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        related_name='listtables',
    )
    table_name = models.CharField(max_length=100, blank=False)

    objects = Manager()

    def __str__(self):
        return self.table_name


class ListTableItem(models.Model):
    table = models.ForeignKey(
        ListTable,
        on_delete=models.CASCADE,
        related_name='listtableitems',
    )
    item_name = models.CharField(max_length=100, blank=False)
    completed = models.BooleanField(default=False)

    objects = Manager()

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return self.item_name
