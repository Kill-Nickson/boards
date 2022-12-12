from django.urls import re_path
from users.views import CustomConfirmEmailView


urlpatterns = [
    re_path(
        r"^confirm-email/(?P<key>[-:\w]+)/$",
        CustomConfirmEmailView.as_view(),
        name="account_confirm_email",
    ),
]
