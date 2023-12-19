from django.shortcuts import render, redirect
from django import forms
from django.forms import widgets
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Card 
from .forms import CardForm

# Sign Up User:
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - please try again!'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


# Create a new Activity Card
class CardCreate(LoginRequiredMixin, CreateView):
  model = Card
  #======= Leaving off complete_date to program in a checkbox or similar ============
  # fields = ['activity', 'due_date']
  
  form_class = CardForm
  
  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)


# Delete an Activity Card
class CardDelete(LoginRequiredMixin, DeleteView):
  model = Card
  success_url = '/cards'


# Update an Activity Card
class CardUpdate(LoginRequiredMixin, UpdateView):
  model = Card
  fields = ['activity', 'due_date', 'complete_date', 'complete']


@login_required
def cards_index(request):
  cards = Card.objects.filter(user=request.user)
  return render(request, 'cards/index.html', { 'cards': cards })


def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')


@login_required
def cards_detail(request, card_id):
  card = Card.objects.get(id=card_id)
  return render(request, 'cards/detail.html', { 'card': card })