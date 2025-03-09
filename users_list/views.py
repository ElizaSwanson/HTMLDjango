from django.contrib.auth.views import LogoutView
from django.core.mail import send_mail
from django.views.generic import CreateView
from django.urls import reverse_lazy

from users_list.forms import UserRegistrationForm
from users_list.models import Users
from django.conf import settings


class UserCreateView(CreateView):
    model = Users
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users_list:login")

    def form_valid(self, form):
        response = super().form_valid(form)

        send_mail(
            subject="Добро пожаловать!",
            message='Спасибо за регистрацию!',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[form.cleaned_data.get("email")],
            fail_silently=False,
        )

        return response


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('catalog:product_list')
