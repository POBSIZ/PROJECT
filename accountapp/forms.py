from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class AccountUpdateForm(UserCreationForm):
    # class Meta:
    #     model = get_user_model()
    #     fields = ['phone', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        fields['username'].disabled = True
