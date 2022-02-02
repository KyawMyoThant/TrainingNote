from distutils.log import Log
from sre_constants import SUCCESS
from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task, Title
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .decorators import student_only
# from .forms import TaskForm

# Create your views here.


class HomeTitleList(ListView):
    model = Title
    paginate_by = 6
    context_object_name = 'titles'
    template_name = "training_note/home.html"


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = "training_note/task_list_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['task-list'] = Task.objects.all()
        return context

# Title Detail View
# Display Detail Info of selected Title


class TitleDetail(LoginRequiredMixin, DetailView):
    model = Title
    context_object_name = 'title'
    template_name = "training_note/title.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['title'].tasks.filter(
            user=self.request.user)
        return context

# Task Detail View
# Display Detail Info of selected Task


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = "training_note/task.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titleid'] = self.request.GET.get('titleid')
        return context

    def get_success_url(self):
        titleid = self.request.GET.get('titleid')
        return reverse_lazy('title', kwargs={'pk': titleid})


class TitleCreate(LoginRequiredMixin, CreateView):
    model = Title
    fields = ['title_name', 'title_description',
              'completed', 'completed_date', 'image']
    success_url = "/"


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # form_class = TaskForm
    fields = ['task_name', 'task_description', 'completed', 'completed_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titleid'] = self.request.POST.get('titleid')
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        title = Title.objects.get(id=self.request.POST.get('titleid'))  # query
        form.instance.title = title
        return super().form_valid(form)

    def get_success_url(self):
        titleid = self.request.POST.get('titleid')
        return reverse_lazy('title', kwargs={'pk': titleid})


class TaskEdit(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['task_name', 'task_description', 'completed', 'completed_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titleid'] = self.request.GET.get('titleid')
        return context

    def get_success_url(self):
        titleid = self.request.GET.get('titleid')
        return reverse_lazy('title', kwargs={'pk': titleid})

# Task Delete View


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titleid'] = self.request.GET.get('titleid')
        return context

    def get_success_url(self):
        titleid = self.request.GET.get('titleid')
        return reverse_lazy('title', kwargs={'pk': titleid})

# LogIn View


class CustomLoginView(LoginView):
    template_name = 'training_note/login.html'
    redirect_authenticated_user = True  # TODO

    def get_success_url(self):
        if self.request.GET.get('next'):
            return redirect('/task/1/')
        else:
            return reverse_lazy('home')


class TitleEdit(LoginRequiredMixin, UpdateView):
    model = Title
    fields = ['title_name', 'title_description',
              'completed', 'completed_date', 'image']
    #template_name_suffix = "_edit_form"
    success_url = "/"


class TitleDelete(LoginRequiredMixin, DeleteView):
    model = Title
    context_object_name = 'title'
    success_url = "/"
