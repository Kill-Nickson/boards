from django.contrib import admin

from .models import Board, ListTable, ListTableItem, BoardUser


class ListTableItemInline(admin.TabularInline):
    model = ListTableItem


class BoardUsersInLine(admin.StackedInline):
    model = BoardUser


class ListTableInline2(admin.ModelAdmin):
    inlines = [
        ListTableItemInline,
    ]
    list_display = ('board', 'table_name')


class ListTableInline(admin.TabularInline):
    model = ListTable


class BoardAdmin(admin.ModelAdmin):
    inlines = [
        ListTableInline,
        BoardUsersInLine,
    ]
    list_display = ('board_name', 'owner', 'password')
    filter_horizontal = ('users',)


admin.site.register(ListTable, ListTableInline2)
admin.site.register(Board, BoardAdmin)
