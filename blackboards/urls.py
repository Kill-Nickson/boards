from django.urls import path

from .views import BlackboardListView, BlackboardDetailView


urlpatterns = [
    path('', BlackboardListView.as_view(), name='blackboard_list'),
    path('<uuid:pk>', BlackboardDetailView.as_view(), name='blackboard_detail'),
]
