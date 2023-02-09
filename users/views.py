from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from users.models import MyUser
from users.forms import UserCreateForm, UserUpdateForm, CustomerUpdateForm, CustomerProfileForm


class MyMixin(LoginRequiredMixin, UserPassesTestMixin):
    """ Mixin for Authentication and User is Admin or not """
    def test_func(self):
        return self.request.user.user_type == 'admin'


# Create your views here.
@login_required()
def home(request):
    """ Home Page """
    admin_count = MyUser.objects.filter(user_type='admin').count()
    customer_count = MyUser.objects.filter(user_type='customer').count()
    context = {
        'a_count': admin_count,
        'c_count': customer_count,
    }
    return render(request, 'users/home.html', context)


class UserRegistrationView(CreateView):
    """ New User Registration """
    model = MyUser
    form_class = UserCreateForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('user_app:home')

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data['password']
        user.set_password(password)
        messages.success(self.request, f"{user.username} is created successfully!")
        user.save()
        return redirect(reverse_lazy('user_app:home'))


class UserListView(MyMixin, ListView):
    """ List of Users for Admin """
    model = MyUser
    template_name = 'users/list.html'
    context_object_name = 'data'


class UserCreateView(MyMixin, CreateView):
    """ Create a new User by Admin """
    model = MyUser
    form_class = UserCreateForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('user_app:list')

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data['password']
        user.set_password(password)
        messages.success(self.request, f"{user.username} is created successfully!")
        user.save()
        return redirect(reverse_lazy('user_app:list'))


class UserUpdateView(MyMixin, UpdateView):
    """ Update a user by Admin """
    model = MyUser
    form_class = UserUpdateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('user_app:list')

    def form_valid(self, form):
        super(UserUpdateView, self).form_valid(form)
        messages.success(self.request, f"user is updated successfully!")
        return redirect(reverse_lazy('user_app:list'))


class UserDeleteView(MyMixin, DeleteView):
    """ Delete a user by Admin """
    model = MyUser
    template_name = 'users/delete.html'
    success_url = reverse_lazy('user_app:list')

    def form_valid(self, form):
        super(UserDeleteView, self).form_valid(form)
        messages.warning(self.request, f"user is deleted successfully!")
        return redirect(reverse_lazy('user_app:list'))


class UserProfile(LoginRequiredMixin, UpdateView):
    """ All User Profile Page """
    def get(self, request, **kwargs):
        user = request.user
        data = MyUser.objects.get(id=user.id)
        c_form = CustomerUpdateForm(instance=user)
        p_form = CustomerProfileForm(instance=user.profile)

        context = {
            'data': data,
            'c_form': c_form,
            'p_form': p_form,
        }
        return render(request, 'users/profile.html', context)

    def post(self, request, *args, **kwargs):
        user = request.user
        c_form = CustomerUpdateForm(request.POST, instance=user)
        p_form = CustomerProfileForm(request.POST, request.FILES, instance=user.profile)
        if c_form.is_valid() and p_form.is_valid():
            username = c_form.cleaned_data['username']
            c_form.save()
            p_form.save()
            messages.success(request, f"{username}'s profile has been updated successfully!")
        return redirect(reverse_lazy('user_app:profile', kwargs={'pk': user.id}))
