from django.views.generic import UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

#Models
from .models import Bilateral, BilateralObservation
from users.models import User

#utils
from users.data.bilateral_data import bilateral_data

class BilateralBase:
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        jumps = [form.instance.right, form.instance.left]
        form.instance.deficit = round(((min(jumps)/max(jumps))-1)*100, 1)
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:bilateral_detail', kwargs = {'id': id})
        url = success_url.format(**self.object.__dict__)
        return url


class BilateralObservationBase:
    model = BilateralObservation

    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:bilateral_detail', kwargs = {'id': id})
        url = success_url.format(**self.object.__dict__)
        return url


class BilateralObservationCreateView(BilateralObservationBase, CreateView):
    fields = ['athlete', 'observation', ]


class BilateralObservationUpdateView(BilateralObservationBase, UpdateView):
    fields = ['observation', ]
    pk_url_kwarg = 'id'


class BilateralObservationDeleteView(BilateralObservationBase, DeleteView):
    pk_url_kwarg = 'id'


class BilateralCreateView(BilateralBase, CreateView):
    model = Bilateral
    fields = ['athlete', 'date', 'jump', 'left', 'right']


class BilateralUpdateView(BilateralBase, UpdateView):
    model = Bilateral
    fields = ['date', 'left', 'right']
    pk_url_kwarg = 'id'


class BilateralDelete(DeleteView):
    model = Bilateral
    pk_url_kwarg = 'id'

    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:bilateral_detail', kwargs = {'id': id})
        url = success_url.format(**self.object.__dict__)
        return url


class BilateralReportView(LoginRequiredMixin, DetailView):
    model = User
    pk_url_kwarg = 'id'
    template_name = 'users/report_bilateral.html'
    extra_context = {
        'page': 'user_list_detail',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        bilaterals = Bilateral.objects.filter(athlete=context['user'].athlete).order_by('-date')

        if 'date' in self.request.GET:
                date = self.request.GET['date']
        else:
            date = ''
        
        bilateral_data(context, date)

        if len(bilaterals) > 0:
            context['bilaterals']

        return context



