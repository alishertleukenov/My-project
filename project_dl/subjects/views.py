from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.template.context_processors import csrf
from django.contrib import auth

from .models import Student, Parent


def students(request, page_number=1):
    all_subjects = Student.objects.all()
    all_parents = Parent.objects.all()
    return render_to_response('students.html', {'student': all_subjects,
                                                'parent': all_parents,})


def student(request, student_id=1, parents_id=1):
    args = {}
    args.update(csrf(request))
    args['parent'] = Parent.objects.get(id = parents_id)
    args['student'] = Student.objects.get(id = student_id)
    return render_to_response('student.html', args)

