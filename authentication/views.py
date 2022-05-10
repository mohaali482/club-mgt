from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from .forms import UserUpdateForm, SignupForm
from .tokens import account_activation_token

# Create your views here.


def home(request):
    return render(request, 'home.html')


def profile(request):
    context = {'uid': urlsafe_base64_encode(force_bytes(request.user.pk))}
    return render(request, 'profile/profile.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('message.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'forms.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse(
            'Thank you for your email confirmation. Now you can login your account.'
        )

    return HttpResponse('Activation link is invalid!')


class UserUpdateView(UpdateView):
    model = User
    template_name = "profile/update.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy('profile')

    def get_object(self, *args, **kwargs):
        try:
            user = self.request.user
        except User.DoesNotExist:
            user = None

        if user is not None:
            return user
        
        messages.error(self.request, "User not found.")
        return redirect('profile')

class UserDetailView(DetailView):
    model = User
    template_name = "profile/detail.html"
    queryset = User.objects.filter(is_active=True)

    def get_object(self):
        uid64 = self.kwargs.get("id")
        uid = force_str(urlsafe_base64_decode(uid64))
        try:
            user = self.queryset.get(pk=uid)
        except User.DoesNotExist:
            user = None

        if user is not None:
            return user
        
        messages.error(self.request, "User not found.")
        return redirect('profile') # Change to list page.