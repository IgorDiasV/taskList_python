from datetime import datetime, timedelta

def get_days_to_add(request, list_days: list):
    days_to_make = []
    for day in list_days:
        status = request.POST.get(day, False)
        if status == 'on':
            days_to_make.append(day)
    return days_to_make

def last_day_of_the_week(data):
    data_obj = datetime.strptime(data, '%Y-%m-%d')

    dias_ate_sabado = (5 - data_obj.weekday() + 7) % 7

    ultimo_dia_semana = data_obj + timedelta(days=dias_ate_sabado)

    return ultimo_dia_semana


def done_this_week(done_at):
    if done_at:
        done_at = done_at.replace(tzinfo=None)
        now = datetime.now().strftime('%Y-%m-%d')
        last_day = last_day_of_the_week(now)
        dif_days = (last_day - done_at).days 
        if dif_days < 7:
            return True
    return False


def out_of_date(day_of_task):
    dict_days = {'domingo': 0,
                 'segunda': 1,
                 'terca': 2,
                 'quarta': 3,
                 'quinta': 4,
                 'sexta': 5,
                 'sabado': 6}
    
    week_day = dict_days[day_of_task]
    week_day_current = datetime.now().weekday()
    # no datetime o domingo é considerado o ultimo dia da semana
    # no programa desenvolvido o domingo é o primeiro dia da semana 
    # por esse motivo foi necessaro fazer a conta a baixo para garantir que no domingo funcionaria

    if week_day_current == 6:
        week_day_current = -1

    if week_day - 1< datetime.now().weekday():
        return True
    
    return False


