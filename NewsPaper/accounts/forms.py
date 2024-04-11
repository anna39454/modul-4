from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from allauth.account.forms import SignupForm #Добавление в группы при регистрации
from django.contrib.auth.models import Group

from django.core.mail import send_mail #Для отправки письма новому пользователю.

#форма с помощью которой мы будем создавать нового пользователя.
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

class CustomSignupForm(SignupForm): # добавлением пользователя в группу
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name="authors")
        user.groups.add(common_users)
        return user


class CustomSignupForm(SignupForm):
    #Функция send_mail позволяет отправить письмо указанному получателю в recipient_list.
    # В поле subject мы передаём тему письма, а в message — текстовое сообщение.
    def save(self, request):
        user = super().save(request)

        send_mail(
            subject='Добро пожаловать в наш новостной сайт!',
            message=f'{user.username}, вы успешно зарегистрировались!',
            from_email=None,  # будет использовано значение DEFAULT_FROM_EMAIL
            recipient_list=[user.email],
        )
        return user