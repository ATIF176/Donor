from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import DonorRegister

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return redirect("donorlist")  # Redirect to the profile page upon successful submission
    else:
        form = RegisterForm()  # Initialize a new form for rendering

    return render(request, "volunteer-registration.html", {'form': form})


def profile(request, pk):
    donor = DonorRegister.objects.get(pk=pk)
    context = {'donor': donor}
    return render(request, "volunteer-profile.html", context)

def donorlist(request):
    donor = DonorRegister.objects.all()
    context = {'donors': donor}
    return render(request, "donor-list.html", context)

