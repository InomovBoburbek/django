from django.http import HttpResponse
from .models import Task
from django.shortcuts import render


def week(request, week_name):
    daily_task = Task.objects.get(week_name=week_name)
    return HttpResponse(f"{daily_task.task}")

def home(request):
    html = """
    <p><a href=' http://127.0.0.1:8000/table/Dushanba'>Dushanba<p/>
    <p><a href=' http://127.0.0.1:8000/table/Seshanba'>Seshanba<p/>
    <p><a href=' http://127.0.0.1:8000/table/Chorshanba'>Chorshanba<p/>
    <p><a href=' http://127.0.0.1:8000/table/Payshanba'>Payshanba<p/>
    <p><a href=' http://127.0.0.1:8000/table/Juma'>Juma<p/>
    <p><a href=' http://127.0.0.1:8000/table/Shanba'>Shanba<p/>
    <p><a href=' http://127.0.0.1:8000/table/Yakshanba'>Yakshanba<p/>
    """
    return HttpResponse(html)