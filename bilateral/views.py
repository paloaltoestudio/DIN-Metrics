from django.views.generic import UpdateView, CreateView
from django.urls import reverse_lazy

#Models
from .models import Bilateral

class BilateralBase:
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.deficit = round(((form.instance.left/form.instance.right)-1)*100, 1)
        self.object = form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        print(form.error)
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:user_detail', kwargs = {'id': id})
        url = success_url.format(**self.object.__dict__)
        url = url + '?tab=bilateral'
        return url

class BilateralCreateView(BilateralBase, CreateView):
    model = Bilateral
    fields = ['athlete', 'date', 'jump', 'left', 'right']

class BilateralUpdateView(BilateralBase, UpdateView):
    model = Bilateral
    fields = ['date', 'left', 'right']
    pk_url_kwarg = 'id'

    


