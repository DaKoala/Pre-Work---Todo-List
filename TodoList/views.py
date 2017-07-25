from django.shortcuts import render
from django.http import HttpResponse
from .forms import ToDoForm
from .models import *
import re
import datetime

# Create your views here.


def index(request):
    to_do_list = ToDo.objects.all()
    week_list = list()
    for i in range(7):
        week_list.append(datetime.date.today() + datetime.timedelta(days=i))
    return render(request, 'index.html', locals())


def list_all(request):
    to_do_list = ToDo.objects.all()
    all_day_list = list()
    for to_do in to_do_list:
        all_day_list.append(to_do.date)
    all_day_list.sort()
    return render(request, 'list_all.html', locals())


def list_prior(request):
    to_do_list = ToDo.objects.all()
    all_day_list = list()
    prior_list = [1, 2, 3, 4]
    return render(request, 'list_prior.html', locals())


def list_expire(request):
    to_do_list = ToDo.objects.all()
    all_expire_day_list = list()
    for to_do in to_do_list:
        all_expire_day_list.append(to_do.expire_date)
    all_expire_day_list.sort()
    return render(request, 'list_expire.html', locals())


def add(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            to_do_info = form.save()
            to_do_info.save()
            return render(request, 'finish.html', locals())

    else:
        form = ToDoForm()

    return render(request, 'add.html', {'form_info': form})


def delete(request):
    url = request.get_full_path()
    id_filter = re.compile(r'\d+')
    delete_id = int(id_filter.findall(url)[-1])
    ToDo.objects.filter(id=delete_id).delete()
    return render(request, 'delete.html', locals())


def edit(request):
    url = request.get_full_path()
    id_filter = re.compile(r'\d+')
    edit_id = int(id_filter.findall(url)[-1])
    edit_object = ToDo.objects.filter(id=edit_id)
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            new_date = form.cleaned_data['date']
            new_content = form.cleaned_data['content']
            new_prior = form.cleaned_data['prior']
            new_is_finished = form.cleaned_data['is_finished']
            new_expire_date = form.cleaned_data['expire_date']
            edit_object.update(date=new_date,
                               content=new_content,
                               prior=new_prior,
                               is_finished=new_is_finished,
                               expire_date=new_expire_date)
            return render(request, 'finish.html', locals())

    else:
        form = ToDoForm(initial={'content': ToDo.objects.get(id=edit_id).content,
                                 'date': ToDo.objects.get(id=edit_id).date,
                                 'prior': ToDo.objects.get(id=edit_id).prior,
                                 'is_finished': ToDo.objects.get(id=edit_id).is_finished,
                                 'expire_date': ToDo.objects.get(id=edit_id).expire_date, })

    return render(request, 'edit.html', locals())


def complete(request):
    url = request.get_full_path()
    id_filter = re.compile(r'\d+')
    complete_id = int(id_filter.findall(url)[-1])
    ToDo.objects.filter(id=complete_id).update(is_finished=True)
    return render(request, 'finish.html', locals())