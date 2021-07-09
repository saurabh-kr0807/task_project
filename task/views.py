from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from task.models import TaskDetail
from task.forms import TaskForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

class HomeView(TemplateView):
    template_name = 'home.html'

class TaskListView(ListView):
    model = TaskDetail
    context_object_name = 'tasks'
    queryset = TaskDetail.objects.all()
    # def get_queryset(self):
    #     return TaskDetail.objects.all()

class TaskDetailView(DetailView):
    model = TaskDetail

class CreateTaskView(CreateView):
    redirect_field_name = 'task/taskdetail_list.html'
    form_class = TaskForm
    model = TaskDetail

class TaskUpdateView(UpdateView):
    #redirect_field_name = 'task/taskdetail_list.html'
    form_class = TaskForm
    model = TaskDetail
    success_url ="/task/"

class TaskDeleteView(DeleteView):
    model = TaskDetail
    success_url = reverse_lazy('task_list')

@login_required
def next(request):
    return redirect('task_list')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
