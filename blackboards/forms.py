from django import forms

from .models import ListTableItem, ListTable, Board


class TableItemForm(forms.ModelForm):
    class Meta:
        model = ListTableItem
        fields = ['item_name']

        widgets = {'item_name': forms.Textarea(attrs={'class': 'form-control',
                                                      'id': 'item_name', 'style': 'height:100px;'})}


class TableForm(forms.ModelForm):
    class Meta:
        model = ListTable
        fields = ['table_name']

        widgets = {
            'table_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'table_name'}),
        }


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['password']

        widgets = {
            'password': forms.TextInput(attrs={'class': 'form-control', 'id': 'password'}),
        }
