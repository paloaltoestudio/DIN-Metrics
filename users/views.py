"""Users views."""
# Django
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib import messages

# Exception
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

# Models
from users.models import Athlete, User
from users.forms import (UpdateUserForm, 
                         PictureForm,
                         UpdateAthletePersonal, 
                         UpdateAthleteSport, 
                         UpdateAthleteMeasures,
                         UpdateAthleteHealth,
                         UpdateAthleteLegal)
from osteo.models import Osteo
from fms.models import Fms
from profile_fv.models import FV_register, FV
from fat.models import Fat_rate

#Utils
from users.utils import age, get_sum

#data
from users.data.jumps_data import jump_data
from users.data.fat_data import fat_data
from users.data.bilateral_data import bilateral_data
from users.data.profile_data import profile_data
from users.data.fv_data import fv_data

#filters
from users.filters import UserFilter, ManagerFilter



class Index(LoginRequiredMixin, ListView):
    model = User
    ordering = ['-date_joined']
    paginate_by = 15
    template_name = 'users/index.html'
    context_object_name = 'users'
    extra_context = {
        'page': 'user_list_detail'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        athletes = Athlete.objects.filter(manager = self.request.user)
        context["has_athletes"] = len(athletes) > 0

        f = UserFilter(self.request.GET, User.objects.filter(role = 'ATHLETE', athlete__isnull = False).order_by('-date_joined'))
        context['filter'] = f

        return context

    def get_queryset(self):
        return ManagerFilter(self.request.GET, User.objects.filter(role = 'ATHLETE', athlete__isnull = False).order_by('-date_joined')).qs

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
    extra_context = {
        'page': 'manager_list_detail'
    }


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        f = ManagerFilter(self.request.GET, User.objects.filter(role = 'MANAGER').order_by('-date_joined'))
        context['filter'] = f

        return context
    
    def get_queryset(self):
        return ManagerFilter(self.request.GET, User.objects.filter(role = 'MANAGER').order_by('-date_joined')).qs


class ReportDetail(LoginRequiredMixin, DetailView):
    model = User
    pk_url_kwarg = 'id'
    template_name = 'users/report_detail.html'
    extra_context = {
        'page': 'user_list_detail',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        managers = User.objects.filter(role = 'MANAGER')

        context['managers'] = managers

        #Get Osteomuscular data
        osteo = Osteo.objects.filter(athlete = context['user'].athlete)
        if len(osteo) > 0:
            context['osteo'] = osteo[0]

        #Get FMS data
        fms = Fms.objects.filter(athlete = context['user'].athlete)
        if len(fms) > 0:
            fms = fms[0]
            
            def check_value(value):
                if type(value) == str:
                    return 0.0
                else:
                    return value

            fms.fence_total = get_sum(check_value(fms.fence_step_l_score), check_value(fms.fence_step_r_score))
            fms.lunge_total = get_sum(check_value(fms.lunge_l_score), check_value(fms.lunge_r_score))
            fms.shoulder_total = get_sum(check_value(fms.shoulder_l_score), check_value(fms.shoulder_r_score))
            fms.leg_total = get_sum(check_value(fms.leg_raise_l_score), check_value(fms.leg_raise_r_score))
            fms.trunk_total = get_sum(check_value(fms.trunk_l_score), check_value(fms.trunk_r_score))
            fms.trunk_rot_total = get_sum(check_value(fms.trunk_rot_l_score), check_value(fms.trunk_rot_r_score))

            fms.total = sum([check_value(fms.squat_score), check_value(fms.fence_total), check_value(fms.lunge_total), check_value(fms.shoulder_total), 
                             check_value(fms.leg_total), check_value(fms.trunk_total), check_value(fms.trunk_rot_total)])

            context['fms'] = fms

        #Get data from neuro and make chart
        jump_data(context)

        #Get data from bilateral and make chart
        if 'date' in self.request.GET:
            date = self.request.GET['date']
        else:
            date = ''
        
        bilateral_data(context, date)

        #Get data from profile FV and make chart
        profile_data(context)

        return context


class UserDetail(LoginRequiredMixin, DetailView):
    model = User
    pk_url_kwarg = 'id'
    template_name = 'users/detail.html'
    extra_context = {
        'page': 'user_list_detail',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        managers = User.objects.filter(role = 'MANAGER')

        context['managers'] = managers
        return context


class OsteoDetail(LoginRequiredMixin, DetailView):
    model = User
    pk_url_kwarg = 'id'
    template_name = 'users/detail_osteo.html'
    extra_context = {
        'page': 'user_list_detail',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        osteo = Osteo.objects.filter(athlete = context['user'].athlete)
        if len(osteo) > 0:
            context['osteo'] = osteo[0]

        return context


class FMSDetail(LoginRequiredMixin, DetailView):
    model = User
    pk_url_kwarg = 'id'
    template_name = 'users/detail_fms.html'
    extra_context = {
        'page': 'user_list_detail',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        fms = Fms.objects.filter(athlete = context['user'].athlete)
        if len(fms) > 0:
            fms = fms[0]
            
            def check_value(value):
                if type(value) == str:
                    return 0.0
                else:
                    return value

            fms.fence_total = get_sum(check_value(fms.fence_step_l_score), check_value(fms.fence_step_r_score))
            fms.lunge_total = get_sum(check_value(fms.lunge_l_score), check_value(fms.lunge_r_score))
            fms.shoulder_total = get_sum(check_value(fms.shoulder_l_score), check_value(fms.shoulder_r_score))
            fms.leg_total = get_sum(check_value(fms.leg_raise_l_score), check_value(fms.leg_raise_r_score))
            fms.trunk_total = get_sum(check_value(fms.trunk_l_score), check_value(fms.trunk_r_score))
            fms.trunk_rot_total = get_sum(check_value(fms.trunk_rot_l_score), check_value(fms.trunk_rot_r_score))

            fms.total = sum([check_value(fms.squat_score), check_value(fms.fence_total), check_value(fms.lunge_total), check_value(fms.shoulder_total), 
                             check_value(fms.leg_total), check_value(fms.trunk_total), check_value(fms.trunk_rot_total)])

            context['fms'] = fms

        return context


class JumpDetail(LoginRequiredMixin, DetailView):
    model = User
    pk_url_kwarg = 'id'
    template_name = 'users/detail_jump.html'
    extra_context = {
        'page': 'user_list_detail',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        #Get data from jumps and make chart
        jump_data(context)

        return context


class BilateralDetail(LoginRequiredMixin, DetailView):
    model = User
    pk_url_kwarg = 'id'
    template_name = 'users/detail_bilateral.html'
    extra_context = {
        'page': 'user_list_detail',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if 'date' in self.request.GET:
            date = self.request.GET['date']
        else:
            date = ''
        
        #Get data from bilateral and make chart
        bilateral_data(context, date)

        return context


class FatDetailView(LoginRequiredMixin, DetailView):
    model = User
    pk_url_kwarg = 'id'
    template_name = 'users/detail_fat.html'
    extra_context = {
        'page': 'user_list_detail',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        #Get data from fat and make chart
        fat_data(context)

        return context


class ProfileFVDetail(LoginRequiredMixin, DetailView):
    model = User
    pk_url_kwarg = 'id'
    template_name = 'users/detail_profile_fv.html'
    extra_context = {
        'page': 'user_list_detail',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        #Get data from profile FV and make chart
        profile_data(context)

        return context


class FVDetail(LoginRequiredMixin, DetailView):
    model = User
    pk_url_kwarg = 'id'
    template_name = 'users/detail_fv.html'
    extra_context = {
        'page': 'user_list_detail',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        #Get data from profile FV and make chart
        fv_id = self.request.GET['fv_id']
        fv_data(fv_id, context)

        return context


class ProfileFVGraph(LoginRequiredMixin, DetailView):
    model = User
    pk_url_kwarg = 'id'
    template_name = 'users/graph_profile_fv.html'
    extra_context = {
        'page': 'user_list_detail',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        #Get data from profile FV and make chart
        profile_data(context)

        return context



class ManagerDetail(LoginRequiredMixin, DetailView):
    model = User
    pk_url_kwarg = 'id'
    template_name = 'users/manager_detail.html'
    extra_context = {
        'page': 'manager_list_detail'
    }


class AccountDetail(LoginRequiredMixin, DetailView):
    model = User
    pk_url_kwarg = 'id'
    template_name = 'users/account_detail.html'
    extra_context = {
        'page': 'account_detail'
    }


class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:password_change_done')

class PasswordChangeDone(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'


@login_required
def manager_update(request, id):
    user = get_object_or_404(User, id = id)

    if user:
        role = user.role

    if request.method == 'POST':
        form = UpdateUserForm(data=request.POST, instance=user)
            
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Empresario Actualizado')

        else:
            return render(request, 'users/manager_detail.html', {'user': user, 'id': id, 'form': form})

        if 'referer' in request.POST and request.POST['referer'] == 'profile_info':
                print('referer')
                return redirect('users:account_detail', id)

        else:
            if role and role == 'MANAGER':
                return redirect('users:manager_detail', id)
            else:
                return redirect('users:manager_detail', id)

    return render(request, 'users/manager_detail.html', {'user': user, 'id': id})


def user_update(request, id):
    if request.method == 'POST':

        user = User.objects.get(id=request.POST['id'])

        if user:
            role = user.role

        if request.POST['type'] == 'picture':

            form = PictureForm(request.POST, request.FILES, instance=user)
            
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Usuario Actualizado')

            else:
                messages.add_message(request, messages.ERROR, form.errors)
                
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
                #return redirect('users:user_detail', id)
                return render(request, 'users/detail.html', {'user': user, 'id': id, 'form': form, 'form_type': 'exampleModal'})

        if request.POST['type'] == 'sport':
            form_profile_sport = UpdateAthleteSport(data=request.POST, instance=user.athlete)

            if request.POST.get('is_athlete') and request.POST.get('is_athlete') == 'on':
                is_athlete = True
            else:
                is_athlete = False
            
            if form_profile_sport.is_valid():
                sport = form_profile_sport.save(commit=False)
                sport.is_athlete = is_athlete
                sport.save()

                messages.add_message(request, messages.SUCCESS, 'Deportista Actualizado')

            else:
                messages.add_message(request, messages.ERROR, form.errors)
                #return redirect('users:user_detail', id)
                return render(request, 'users/detail.html', {'user': user, 'id': id, 'form': form, 'form_type': 'sportModal'})
        
        if request.POST['type'] == 'measures':
            form_profile_measures = UpdateAthleteMeasures(data=request.POST, instance=user.athlete)
            
            if form_profile_measures.is_valid():
                form_profile_measures.save()
                messages.add_message(request, messages.SUCCESS, 'Deportista Actualizado')

            else:
                messages.add_message(request, messages.ERROR, form.errors)
                #return redirect('users:user_detail', id)
                return render(request, 'users/detail.html', {'user': user, 'id': id, 'form': form, 'form_type': 'measuresModal'})

        
        if request.POST['type'] == 'health':
            form_profile_health = UpdateAthleteHealth(data=request.POST, instance=user.athlete)
            
            if form_profile_health.is_valid():
                form_profile_health.save()
                messages.add_message(request, messages.SUCCESS, 'Deportista Actualizado')

            else:
                messages.add_message(request, messages.ERROR, form.errors)
                #return redirect('users:user_detail', id)
                return render(request, 'users/detail.html', {'user': user, 'id': id, 'form': form, 'form_type': 'healthModal'})

        
        if request.POST['type'] == 'legal':
            form_profile_legal = UpdateAthleteLegal(data=request.POST, instance=user.athlete)
            
            if form_profile_legal.is_valid():
                form_profile_legal.save()
                messages.add_message(request, messages.SUCCESS, 'Deportista Actualizado')

            else:
                messages.add_message(request, messages.ERROR, form_profile_legal.errors)
                #return redirect('users:user_detail', id)
                return render(request, 'users/detail.html', {'user': user, 'id': id, 'form': form, 'form_type': 'legalModal'})

        if 'referer' in request.POST and request.POST['referer'] == 'profile_info':
            print('referer')
            return redirect('users:account_detail', id)

        else:
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
                            'error': 'Ya existe un usuario con la misma cédula',
                            'form': request.POST
                            })

        try:
            user = User.objects.create_user(email=request.POST['email'], password=passwd)
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
                            'error': 'Ya existe un usuario con la misma cédula',
                            'form': request.POST
                            })

        try:
            user = User.objects.create_user(email=request.POST['email'], password=passwd)
        except IntegrityError:
            return render(request, 'users/new_manager.html', {'error': 'Ya existe un usuario con el mismo email', 'form': request.POST})

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
