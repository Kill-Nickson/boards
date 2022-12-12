from allauth.account import app_settings
from allauth.account.adapter import get_adapter
from allauth.account.views import ConfirmEmailView
from django.contrib import messages
from django.shortcuts import redirect


class CustomConfirmEmailView(ConfirmEmailView):

    def post(self, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm(self.request)

        # In the event someone clicks on an email confirmation link
        # for one account while logged into another account,
        # logout of the currently logged in account.
        if (
            self.request.user.is_authenticated
            and self.request.user.pk != confirmation.email_address.user_id
        ):
            self.logout()

        get_adapter(self.request).add_message(
            self.request,
            messages.SUCCESS,
            "account/messages/email_confirmed.txt",
            {"email": confirmation.email_address.email},
        )
        if app_settings.LOGIN_ON_EMAIL_CONFIRMATION:
            resp = self.login_on_confirm(confirmation)
            if resp is not None:
                return resp

        user = confirmation.email_address.user
        user.is_active = True
        user.save()

        redirect_url = self.get_redirect_url()
        if not redirect_url:
            ctx = self.get_context_data()
            return self.render_to_response(ctx)
        return redirect(redirect_url)
