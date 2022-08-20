"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages


# Exception
from django.db.utils import IntegrityError

# Models
from users.models import Athlete, User
from users.forms import UpdateUserForm

class Index(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'
    extra_context = {
        'page': 'user_list_detail'
    }


class ManagerView(ListView):
    model = User
    template_name = 'users/managers.html'
    context_object_name = 'users'
    extra_context = {
        'page': 'manager_list_detail'
    }


class UserDetail(DetailView):
    model = User
    pk_url_kwarg = 'id'
    template_name = 'users/detail.html'
    extra_context = {
        'page': 'user_list_detail'
    }


class ManagerDetail(DetailView):
    model = User
    pk_url_kwarg = 'id'
    template_name = 'users/manager_detail.html'
    extra_context = {
        'page': 'manager_list_detail'
    }


def user_update(request, id):
    if request.method == 'POST':

        form = UpdateUserForm(request.POST)
        user = User.objects.get(id=request.POST['id'])
        athlete = Athlete.objects.get_or_create(user=user)
        athlete = athlete[0]

        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data

            athlete.age = data['age']
            athlete.phone = data['phone']
            athlete.birthdate = data['birthdate']
            athlete.gender = data['gender']
            athlete.save()

            return redirect('users:user_detail', id=id)

        else:
            messages.add_message(request, messages.ERROR, form.errors)
            return redirect('users:user_detail', id)




def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')


def signup(request):
    """Sign up view."""
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in user'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.role = request.POST['role']
        user.save()

        athlete = Athlete(user=user)
        athlete.phone = request.POST['phone']
        athlete.save()

        # return redirect('login')
        return render(request, 'users/signup.html', {
            'page': 'user_signup'
        })

    return render(request, 'users/signup.html', {
        'page': 'user_signup'
    })


@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('login')
