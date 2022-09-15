from django.views.generic import UpdateView
from django.urls import reverse_lazy

#Models
from .models import Bilateral

class BilateralUpdateView(UpdateView):
    model = Bilateral
    fields = ['date', 'left', 'right']
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.deficit = round(((form.instance.left/form.instance.right)-1)*100, 1)
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:user_detail', kwargs = {'id': id})
        url = success_url.format(**self.object.__dict__)
        url = url + '?tab=bilateral'
        return url


