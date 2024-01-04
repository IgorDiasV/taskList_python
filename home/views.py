from django.shortcuts import render, redirect
from .models import Task, TaskDay
from .utils import get_days_to_add, done_this_week, out_of_date

days = ['domingo', 'segunda', 'terca', 'quarta' ,'quinta' ,'sexta', 'sabado']


def att_task(task):
    for day in days:
        day_of_task = task.task_day.filter(day=day)
        if day_of_task:
            if not done_this_week(day_of_task[0].done_at):
                day_of_task[0].done = False
                day_of_task[0].save()
            
                 
    
def get_colors_dones(task):
   
    class_colors = []
    list_dones = []
    for day in days:
        day_of_tasck = task.task_day.filter(day=day)
               
        if day_of_tasck:
            list_dones.append(day_of_tasck[0].done)
            if day_of_tasck[0].done:
                     class_colors.append("green")
            else:
                if out_of_date(day_of_tasck[0].day):
                    class_colors.append("red")
                else:
                    class_colors.append("")
        else:
             class_colors.append("gray")
             list_dones.append(False)


    return class_colors, list_dones

def home(request):
    tasks = Task.objects.all()
    dict_tasks = []
    for task in tasks:
        att_task(task)
        colors, dones = get_colors_dones(task)
        aux_dict = {}
        aux_dict = {'colors_dones': zip(colors, dones),
                    'assunto': task.task_name}
        dict_tasks.append(aux_dict)


    return render(request, "main.html", {'dict_tasks': dict_tasks})


def addTask(request):
    assunto = request.POST['assunto']
    days_to_make = get_days_to_add(request, days)

    task = Task.objects.create(task_name=assunto)

    for day in days_to_make:
        taks_day = TaskDay.objects.create(day=day, done=False)
        task.task_day.add(taks_day)

    return redirect("home")