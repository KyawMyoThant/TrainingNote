from django.urls import path

from training_note.decorators import student_only
from .views import CustomLoginView, HomeTitleList, TitleDelete, TitleEdit, TaskDelete, TaskList, TitleDetail, TaskCreate, TaskDetail, TaskEdit, TitleCreate
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('login/', CustomLoginView.as_view(), name='login'),
    path('', HomeTitleList.as_view(), name='home'),
    path('task-list', TaskList.as_view(), name='task-list'),
    path('title/<int:pk>/', student_only(TitleDetail.as_view()), name='title'),
    path('title-create/', TitleCreate.as_view(), name='title-create'),
    path('title-edit/<int:pk>/', TitleEdit.as_view(), name='title-edit'),
    path('title-delete/<int:pk>', TitleDelete.as_view(), name='title-delete'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-edit/<int:pk>/', TaskEdit.as_view(), name='task-edit'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
