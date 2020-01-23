from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].validators = [validate_email]
        self.fields['username'].help_text = 'Enter Email Format.'
        self.fields['username'].label = 'email'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = user.username
        if commit:
            user.save()
        return user

    '''
    # 각 필드에 대한 validators, clean_필드명, clean
    def clean_username(self):
        value = self.cleaned_data.get('username')
        if value:
            validate_email(value)  # 자체적으로 유효성 검사
        return value
    '''
