import json

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Board, ListTable, ListTableItem
from .forms import TableItemForm, TableForm, BoardForm


class BlackboardListView(ListView):
    model = Board
    context_object_name = 'blackboard_list'
    template_name = 'blackboards/blackboards_list.html'

    def get_context_data(self, **kwargs):
        context = super(BlackboardListView, self).get_context_data(**kwargs)
        context['form'] = BoardForm
        return context

    def post(self, request, **kwargs):
        form = BoardForm(request.POST)

        if 'board_name' in request.POST and form.is_valid():
            board_name = request.POST['board_name']
            form_password = form.cleaned_data['password']
            try:
                board = Board.objects.get(board_name=board_name)
            except Board.DoesNotExist:
                print('No such a board!')
            else:
                if form_password == board.password:
                    pk = board.pk
                    url = reverse('blackboard_detail', kwargs={'pk': pk})
                    return HttpResponse(json.dumps(url, ensure_ascii=False),
                                        content_type='application/json')
                else:
                    return HttpResponse(json.dumps('Wrong password!', ensure_ascii=False),
                                        content_type='application/json')
        elif request.POST['password'] == '':
            return HttpResponse(json.dumps('Password field is empty!', ensure_ascii=False),
                                content_type='application/json')


class BlackboardDetailView(DetailView):
    model = Board
    context_object_name = 'blackboard'
    template_name = 'blackboards/blackboards_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BlackboardDetailView, self).get_context_data(**kwargs)
        context['form'] = TableItemForm
        context['form2'] = TableForm
        return context

    def post(self, request, **kwargs):
        form = TableItemForm(request.POST)
        form2 = TableForm(request.POST)

        if 'item_name' in request.POST and form.is_valid():
            if form.is_valid():
                new_task = form.save(commit=False)
                new_task.table = ListTable.objects.get(table_name=request.POST['table'])
                new_task.item_name = form.cleaned_data['item_name']
                form.save()
                return HttpResponse('')
            else:
                response = form.errors
                response = response.as_json()
                return HttpResponse(json.dumps(response, ensure_ascii=False),
                                    content_type='application/json')

        elif 'table_name' in request.POST:
            if form2.is_valid():
                new_group = form2.save(commit=False)
                new_group.board = self.get_object()
                new_group.table_name = form2.cleaned_data['table_name']
                form2.save()
                return HttpResponse('')
            else:
                response = form2.errors
                response = response.as_json()
                return HttpResponse(json.dumps(response, ensure_ascii=False),
                                    content_type='application/json')

        elif 'delete_item_name' in request.POST:
            table_id = request.POST['delete_table_id']
            item_name = request.POST['delete_item_name']
            pk = request.POST['delete_item_name_pk']

            queryset = ListTableItem.objects.filter(table=table_id, item_name=item_name, id=pk).delete()

            if not queryset:
                raise Http404
            return HttpResponse('Item deleted!')

        elif 'update_item_name' in request.POST:
            table_id = request.POST['update_table_id']
            item_name = request.POST['update_item_name']
            pk = request.POST['update_item_name_pk']

            completed_value = ListTableItem.objects.get(table=table_id, item_name=item_name, id=pk)
            if completed_value.completed:
                completed_value.completed = False
            else:
                completed_value.completed = True
            completed_value.save()

            return HttpResponse('Item updated!')

        elif 'delete_table_name' in request.POST:
            board = self.get_object()
            table_name = request.POST['delete_table_name']
            pk = request.POST['delete_table_name_pk']

            queryset = ListTable.objects.filter(board=board, table_name=table_name, id=pk).delete()

            if not queryset:
                raise Http404
            return HttpResponse('Table deleted!')
        else:
            return HttpResponseRedirect(reverse('blackboard_detail', args=(self.get_object().id,)))
