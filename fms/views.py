from django.views.generic import UpdateView
from django.urls import reverse_lazy

from users.models import Athlete
from fms.models import Fms

# class FmsBase:
#     model = Fms
#     pk_url_kwarg = 'id'

#     def get_object(self, queryset=None):
#         athlete = Athlete.objects.get(id = self.request.POST['id'])
        
#         if queryset is None:
#             queryset = self.get_queryset()
            
#         print('slug: ', self.request.POST['test_slug'])
#         obj = queryset.get_or_create(test_slug = self.request.POST['test_slug'])[0]
#         return obj

#     def get_success_url(self):
#         id = self.request.POST['id']
#         success_url = reverse_lazy('users:user_detail', kwargs = {'id': id})
#         url = success_url.format(**self.object.__dict__)
#         url = url + '?tab=fms'
#         return url

class FmsUpdate(UpdateView):
    fields = ['name', 'test_slug', 'score', 'observations']