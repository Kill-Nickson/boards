from django.contrib import admin

from .models import Board, ListTable, ListTableItem


class ListTableItemInline(admin.TabularInline):
    model = ListTableItem


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
    ]
    list_display = ('board_name', 'owner', 'password')
    filter_horizontal = ('users',)


admin.site.register(ListTable, ListTableInline2)
admin.site.register(Board, BoardAdmin)
