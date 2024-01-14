from django.shortcuts import render, redirect
from .models import Task, TaskDay
from .utils import get_days_to_add, get_colors_dones, att_task
import json
from datetime import datetime

days = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']


def home(request):
    tasks = Task.objects.all()
    dict_tasks = []
    for task in tasks:
        att_task(task)
        ids, colors, dones = get_colors_dones(task)
        aux_dict = {}
        aux_dict = {'colors_dones': zip(ids, colors, dones),
                    'task_name': task.task_name,
                    'id': task.id,
                    'duration': task.duration}
        dict_tasks.append(aux_dict)

    return render(request, "main.html", {'dict_tasks': dict_tasks})


def addTask(request):
    task_name = request.POST['task_name']
    duration = request.POST['duration']
    days_to_make = get_days_to_add(request, days)

    task = Task.objects.create(task_name=task_name,
                               duration=duration)

    for day in days_to_make:
        taks_day = TaskDay.objects.create(day=day, done=False)
        task.task_day.add(taks_day)

    return redirect("home")


def save(request):
    alteracoes = json.loads(request.POST.get("mapData"))
    for id_altercao in alteracoes:
        done_str = alteracoes[id_altercao]
        done = False

        if done_str == 'True':
            done = True

        task_day = TaskDay.objects.filter(id=int(id_altercao)).first()
        task_day.done = done
        task_day.done_at = datetime.now()
        task_day.save()

    return redirect('home')


def delete(request):
    id = request.POST.get("id")

    task = Task.objects.filter(id=int(id)).first()

    task.delete()

    return redirect('home')