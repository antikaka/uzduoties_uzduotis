from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import forms, login, mixins
from .models import Uzduotis
from django.views import generic

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, template_name="index.html")


def register(request):
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = forms.UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class UzduotysListView(mixins.LoginRequiredMixin, generic.ListView):
    model = Uzduotis
    template_name = "uzduotys.html"
    context_object_name = "uzduotys"

    def get_queryset(self):
        return Uzduotis.objects.filter(vartotojas=self.request.user)

def viena_uzduotis(request, uzduotis_id):
    viena_uzduotis = get_object_or_404(Uzduotis, pk=uzduotis_id)
    return render(request, "viena_uzduotis.html", {"viena_uzduotis": viena_uzduotis})

class UzduotisCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    model = Uzduotis
    fields = ["uzduoties_tekstas"]
    success_url = "/uzduotis/uzduotys"
    template_name = "uzduota_uzduotis.html"

    def form_valid(self, form):
        form.instance.vartotojas = self.request.user
        return super().form_valid(form)

class UzduotisUpdateView(mixins.LoginRequiredMixin, mixins.UserPassesTestMixin, generic.UpdateView):
    model = Uzduotis
    fields = ["uzduoties_tekstas"]
    success_url = "/uzduotis/uzduotys"
    template_name = "uzduota_uzduotis.html"

    def form_valid(self, form):
        form.instance.vartotojas = self.request.user
        return super().form_valid(form)

    def test_func(self):
        instance = self.get_object()
        return instance.vartotojas == self.request.user

class UzduotisDeleteView(mixins.LoginRequiredMixin, mixins.UserPassesTestMixin, generic.DeleteView):
    model = Uzduotis
    success_url = "/uzduotis/uzduotys"
    template_name = "istrinta_uzduotis.html"

    def test_func(self):
        instance = self.get_object()
        return instance.vartotojas == self.request.user


