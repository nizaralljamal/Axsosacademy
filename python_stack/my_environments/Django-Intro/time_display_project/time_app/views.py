from django.shortcuts import render
from datetime import datetime

def index(request):
    now = datetime.now()
    context = {
        "date": now.strftime("%b %d, %Y"),
        "time": now.strftime("%I:%M %p")
    }
    return render(request, 'time_app/index.html', context)