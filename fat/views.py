from django.views.generic import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

#Models
from .models import Fat_rate, FatObservation
from users.models import Athlete

class FatBase:
    model = Fat_rate

    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:fat_detail', kwargs = {'id': id})
        url = success_url.format(**self.object.__dict__)
        return url


class FatCreateView(FatBase, CreateView):     
    fields = ['athlete', 'date', 'triceps', 'subscap', 'abdominal', 'suprailiac', 'thigh', 'calf']

    def form_valid(self, form):
        """If the form is valid, save the associated model."""

        total_fat = [float(self.request.POST['triceps']), float(self.request.POST['subscap']), float(self.request.POST['abdominal']), 
                     float(self.request.POST['suprailiac']), float(self.request.POST['thigh']), float(self.request.POST['calf'])
                     ]
        total_fat = sum(total_fat)

        athlete_id = self.request.POST['athlete']
        athlete = Athlete.objects.filter(id=athlete_id)

        rate = 0

        
        
        if(athlete[0] and athlete[0].is_athlete):
            if(athlete[0].gender == 'M'):
                rate = (0.1051*total_fat)+2.585
                print('is athlete an M, rate: ', rate)
            else:
                rate = (0.1548*total_fat)+3.58
                print('is athlete an F, rate: ', rate)

        else:
            if(athlete[0].gender == 'M'):
                corp_density = 1.112-(0.00043499*total_fat)+(0.00000055*total_fat**2)-(0.00028826*athlete[0].age)
                corp_density = round(corp_density, 7)
                rate = ((495/corp_density)-450)
                print('is not athlete an M, rate: ', rate)
            else:
                corp_density = 1.112-(0.00046971*total_fat)+(0.00000056*total_fat**2)-(0.00012828*athlete[0].age)
                corp_density = round(corp_density, 7)
                rate = ((495/corp_density)-450)
                print('is not athlete an F, rate: ', rate)

        print('not conditional')
            

        rate = round(rate, 2)
        form.instance.fat_rate = rate

        print('POST INFO', athlete[0].is_athlete, self.request.POST['athlete'])

        self.object = form.save()
        return super().form_valid(form)


class FatUpdateView(FatBase, UpdateView):     
    fields = ['date', 'triceps', 'subscap', 'abdominal', 'suprailiac', 'thigh', 'calf']
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""

        total_fat = [float(self.request.POST['triceps']), float(self.request.POST['subscap']), float(self.request.POST['abdominal']), 
                     float(self.request.POST['suprailiac']), float(self.request.POST['thigh']), float(self.request.POST['calf'])
                     ]
        total_fat = sum(total_fat)

        athlete_id = self.request.POST['athlete']
        athlete = Athlete.objects.filter(id=athlete_id)

        rate = 0
        
        if(athlete[0] and athlete[0].is_athlete):
            if(athlete[0].gender == 'M'):
                rate = (0.1051*total_fat)+2.585
                print('is athlete an M, rate: ', rate)
            else:
                rate = (0.1548*total_fat)+3.58
                print('is athlete an F, rate: ', rate)

        else:
            if(athlete[0].gender == 'M'):
                corp_density = 1.112-(0.00043499*total_fat)+(0.00000055*total_fat**2)-(0.00028826*athlete[0].age)
                corp_density = round(corp_density, 7)
                rate = ((495/corp_density)-450)
                print('is not athlete an M, rate: ', rate)
            else:
                corp_density = 1.112-(0.00046971*total_fat)+(0.00000056*total_fat**2)-(0.00012828*athlete[0].age)
                corp_density = round(corp_density, 7)
                rate = ((495/corp_density)-450)
                print('is not athlete an F, rate: ', rate)
            

        rate = round(rate, 2)
        form.instance.fat_rate = rate

        self.object = form.save()
        return super().form_valid(form)

class FatDeleteView(FatBase, DeleteView):
    pk_url_kwarg = 'id'


class FatObservationBase:
    model = FatObservation

    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:fat_detail', kwargs = {'id': id})
        url = success_url.format(**self.object.__dict__)
        return url


class FatObservationCreateView(FatObservationBase, CreateView):
    fields = ['athlete', 'observation', ]


class FatObservationUpdateView(FatObservationBase, UpdateView):
    fields = ['observation', ]
    pk_url_kwarg = 'id'


class FatObservationDeleteView(FatObservationBase, DeleteView):
    pk_url_kwarg = 'id'