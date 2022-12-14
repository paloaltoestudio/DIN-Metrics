"""Users views."""
# Django
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib import messages

# Exception
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

# Models
from users.models import Athlete, User
from users.forms import (UpdateUserForm, 
                         UpdateAthletePersonal, 
                         UpdateAthleteSport, 
                         UpdateAthleteMeasures,
                         UpdateAthleteHealth,
                         UpdateAthleteLegal)

#Utils
from users.utils import age



class Index(LoginRequiredMixin, ListView):
    model = User
    ordering = ['-date_joined']
    paginate_by = 15
    template_name = 'users/index.html'
    context_object_name = 'users'
    queryset = User.objects.filter(role = 'ATHLETE', athlete__isnull = False)
    extra_context = {
        'page': 'user_list_detail'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        athletes = Athlete.objects.filter(manager = self.request.user)
        context["has_athletes"] = len(athletes) > 0
        return context

    def get(self, *args, **kwargs):
        if self.request.user.role == 'ATHLETE':
            return redirect('users:user_detail', self.request.user.id)
        return super(Index, self).get(*args, **kwargs)
    


class ManagerView(LoginRequiredMixin, ListView):
    model = User
    ordering = ['-date_joined']
    paginate_by = 15
    template_name = 'users/managers.html'
    context_object_name = 'users'
    queryset = User.objects.filter(role = 'MANAGER')
    extra_context = {
        'page': 'manager_list_detail'
    }


class UserDetail(LoginRequiredMixin, DetailView):
    managers = User.objects.filter(role = 'MANAGER')

    model = User
    pk_url_kwarg = 'id'
    template_name = 'users/detail.html'
    extra_context = {
        'page': 'user_list_detail',
        'managers': managers
    }


class ManagerDetail(LoginRequiredMixin, DetailView):
    model = User
    pk_url_kwarg = 'id'
    template_name = 'users/manager_detail.html'
    extra_context = {
        'page': 'manager_list_detail'
    }

@login_required
def manager_update(request, id):
    user = User.objects.get(id = id)

    if request.method == 'POST':
        form = UpdateUserForm(data=request.POST, instance=user)
            
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Empresario Actualizado')
            return redirect('users:manager_detail', id)

        else:
            return render(request, 'users/manager_detail.html', {'user': user, 'id': id, 'form': form})

    return render(request, 'users/manager_detail.html', {'user': user, 'id': id})


def user_update(request, id):
    if request.method == 'POST':
        print(request.POST)

        user = User.objects.get(id=request.POST['id'])

        if user:
            role = user.role

        if request.POST['type'] == 'basic':
            #Get a copy of request post to add calculated age
            data = request.POST.copy()

            # Calculate age and add it to data list
            if 'birthdate' in data:
                if data['birthdate'] != '':
                    data['age'] = age(data['birthdate'])

            form = UpdateUserForm(data=request.POST, instance=user)
            form_profile_info = UpdateAthletePersonal(data=data, instance=user.athlete)

            if form.is_valid() and form_profile_info.is_valid():
                form.save()
                form_profile_info.save()
                messages.add_message(request, messages.SUCCESS, 'Deportista Actualizado')

            else:
                messages.add_message(request, messages.ERROR, form.errors)
                return redirect('users:user_detail', id)

        if request.POST['type'] == 'sport':
            form_profile_sport = UpdateAthleteSport(data=request.POST, instance=user.athlete)
            
            if form_profile_sport.is_valid():
                form_profile_sport.save()
                messages.add_message(request, messages.SUCCESS, 'Deportista Actualizado')

            else:
                messages.add_message(request, messages.ERROR, form.errors)
                return redirect('users:user_detail', id)
        
        if request.POST['type'] == 'measures':
            form_profile_measures = UpdateAthleteMeasures(data=request.POST, instance=user.athlete)
            
            if form_profile_measures.is_valid():
                form_profile_measures.save()
                messages.add_message(request, messages.SUCCESS, 'Deportista Actualizado')

            else:
                messages.add_message(request, messages.ERROR, form.errors)
                if role and role == 'ATHLETE':
                    return redirect('users:user_detail', id)
                elif role and role == 'MANAGER':
                    return redirect('users:manager_detail', id)
        
        if request.POST['type'] == 'health':
            form_profile_health = UpdateAthleteHealth(data=request.POST, instance=user.athlete)
            
            if form_profile_health.is_valid():
                form_profile_health.save()
                messages.add_message(request, messages.SUCCESS, 'Deportista Actualizado')

            else:
                messages.add_message(request, messages.ERROR, form.errors)
                if role and role == 'ATHLETE':
                    return redirect('users:user_detail', id)
                elif role and role == 'MANAGER':
                    return redirect('users:manager_detail', id)
        
        if request.POST['type'] == 'legal':
            form_profile_legal = UpdateAthleteLegal(data=request.POST, instance=user.athlete)
            
            if form_profile_legal.is_valid():
                form_profile_legal.save()
                messages.add_message(request, messages.SUCCESS, 'Deportista Actualizado')

            else:
                messages.add_message(request, messages.ERROR, form_profile_legal.errors)
                if role and role == 'ATHLETE':
                    return redirect('users:user_detail', id)
                elif role and role == 'MANAGER':
                    return redirect('users:manager_detail', id)

        if role and role == 'ATHLETE':
            return redirect('users:user_detail', id)
        else:
            return redirect('users:manager_detail', id)

class UserLoginView(LoginView):
    next_page = 'users:index'
    template_name = 'users/login.html'
    redirect_authenticated_user = True
        

@login_required
def signup(request):
    """Sign up view."""
    if request.method == 'POST':
        passwd = request.POST['document']

        # Check if user with same document exists
        document_check = User.objects.filter(document=passwd).first()

        if document_check:
            return render(request, 'users/signup.html', {
                            'error': 'Ya existe un usuario con la misma c??dula',
                            'form': request.POST
                            })

        try:
            user = User.objects.create_user(username=request.POST['email'], password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Ya existe un usuario con el mismo email', 'form': request.POST})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.phone = request.POST['phone']
        user.email = request.POST['email']
        user.document = request.POST['document']
        user.role = request.POST['role']
        user.save()

        role = request.POST['role']
        if role and role == 'ATHLETE':
            athlete = Athlete(user=user)

            if 'birthdate' in request.POST:
                if request.POST['birthdate'] != '':
                    athlete.age = age(request.POST['birthdate'])
                    athlete.birthdate = request.POST['birthdate']

            athlete.gender = request.POST['gender']
            athlete.save()

        messages.add_message(request, messages.SUCCESS, 'Deportista Creado/a')
        return redirect('users:index')

    return render(request, 'users/signup.html', {
        'page': 'user_signup'
    })

@login_required
def new_manager(request):
    """Manager register up view."""
    if request.method == 'POST':
        passwd = request.POST['document']

        # Check if user with same document exists
        document_check = User.objects.filter(document=passwd).first()

        if document_check:
            return render(request, 'users/new_manager.html', {
                            'error': 'Ya existe un usuario con la misma c??dula',
                            'form': request.POST
                            })

        try:
            user = User.objects.create_user(username=request.POST['email'], password=passwd)
        except IntegrityError:
            return render(request, 'users/new_manager.html', {'error': 'Ya existe un usuario con el mismo email'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.phone = request.POST['phone']
        user.email = request.POST['email']
        user.document = request.POST['document']
        user.role = request.POST['role']
        user.save()

        messages.add_message(request, messages.SUCCESS, 'Empresario Creado')
        return redirect('users:managers')

    return render(request, 'users/new_manager.html', {
        'page': 'manager_signup'
    })


@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('login')
