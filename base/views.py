from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, TemplateView, ListView
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.views.generic.edit import DeleteView
from .forms import RegisterForm
from .models import DonorRegister
from django.db.models import Q


class HomeView(TemplateView):
    template_name = "home.html"

class AboutView(TemplateView):
    template_name = "about.html"

class ContactView(TemplateView):
    template_name = "contact.html"

class ConfirmView(TemplateView):
    template_name = "confirmation.html"

class RegisterView(CreateView):
    template_name = "volunteer-registration.html"
    form_class = RegisterForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect("donorlist")
    
class UpdateView(UpdateView):
    template_name = "volunteer-registration.html"
    model = DonorRegister
    success_url = '/donorlist/'
    form_class = RegisterForm

    
class DeleteView(DeleteView):
    model = DonorRegister
    success_url = '/donorlist/'
    template_name = 'donor-delete.html'

class ProfileView(View):
    template_name = "volunteer-profile.html"

    def get(self, request):
        try:
            donor = DonorRegister.objects.get(user=request.user)
            context = {'donor': donor}
            return render(request, self.template_name, context)
        except:
            return redirect('register')
        

    
class DonorView(View):
    template_name = "volunteer-profile.html"

    def get(self, request, pk):
        donor = DonorRegister.objects.get(pk=pk)
        context = {'donor': donor}
        return render(request, self.template_name, context)

class DonorListView(ListView):
    template_name = "donor-list.html"
    model = DonorRegister

    def get_context_data(self, **kwargs):
        q = self.request.GET.get('q', '')  # Use self.request instead of request
        context = super().get_context_data(**kwargs)
        context['donors'] = DonorRegister.objects.filter(
            Q(dob__icontains=q) |
            Q(city__icontains=q) |
            Q(bgroup__icontains=q)|
            Q(lname__icontains=q)|
            Q(fname__icontains=q)
        ).order_by('-dob')
        return context