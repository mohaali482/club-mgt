from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import DetailView, UpdateView, ListView, DeleteView

from .forms import SignupForm, UserUpdateForm
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
    except(TypeError, ValueError, OverflowError):
        uid = -1
    user = get_object_or_404(User, pk=uid)

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

    def get_object(self, queryset=None):
        if not self.request.user.is_anonymous:
            user = self.request.user
        else:
            user = None

        if user is not None:
            return user
        raise Http404


class UserDetailView(DetailView):
    model = User
    template_name = "profile/detail.html"
    queryset = User.objects.filter(is_active=True)

    def get_object(self, queryset=None):
        uid64 = self.kwargs.get("id")
        uid = force_str(urlsafe_base64_decode(uid64))
        user = get_object_or_404(self.queryset, pk=uid)

        return user


class UserListView(ListView):
    model = User
    template_name = "list.html"
    paginate_by = 10
    queryset = User.objects.filter(is_active=True)


class UserDeleteView(DeleteView):
    model = User
    template_name = "delete.html"
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        if not self.request.user.is_anonymous:
            return self.request.user

        raise Http404
