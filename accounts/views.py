from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.views.generic import CreateView
from .forms import SignupForm

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user) # 로그인 처리
#             next_url = request.GET.get('next') or 'profile'
#             # Querydict : 같은 Key에 대해 다른 값을 가질 수 있음
#             return redirect(next_url)
#     else:
#         form = SignupForm()
#     return render(request, 'accounts/signup.html', {
#         'form': form,
#     })

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next') or 'profile'
        return resolve_url(next_url)

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())

signup = SignupView.as_view()

# signup = CreateView.as_view(model=User,
#         form_class=SignupForm,
#         success_url=settings.LOGIN_URL,
#         template_name='accounts/signup.html')

@login_required # login 상황 보장
def profile(request):
    # request.user # django.contrib.auth.models.AnonymousUser
    return render(request, 'accounts/profile.html')

