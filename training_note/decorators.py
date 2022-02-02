from django.http import HttpResponse
from django.shortcuts import redirect, render


def student_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        teacher = False
        if request.user.is_teacher:
            teacher = True

        if teacher:
            return HttpResponse("You are a teacher.")
        elif request.user.is_superuser:
            return redirect('/admin/')

        else:
            return view_func(request, *args, **kwargs)
    return wrapper_function
