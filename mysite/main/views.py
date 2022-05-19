from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateNewTicket
from .models import Ticket, Message
from django.contrib.auth.models import User
import datetime

# Create your views here.

def home(response):
    return render(response, 'main/home.html', {})


def create(response):

    if response.method == 'POST':
        form = CreateNewTicket(response.POST)
        if form.is_valid:
            form.is_valid()
            n = form.cleaned_data["name"]
            t = Ticket(name=n)
            t.save()
            response.user.ticket.add(t)
            return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewTicket()
    return render(response, "main/create.html", {"form":form})

def index(response, id):
    ls = Ticket.objects.get(id=id)
    
    if response.POST.get("newMessage"):
        txt = response.POST.get("new")
 
        if len(txt) > 2:
            ls.message_set.create(text=txt, date=datetime.datetime.now()) 
        else:
            print("invalid")
    
    return render(response, 'main/list.html', {'ls':ls})


def view(response):
    return render(response, 'main/view.html', {})
def report(response):
    return render(response, 'main/report.html', {})

def users(response):
    users = User.objects.all()
    
    if response.method == 'POST':
        if response.POST.get('save'):
            for user in users:
                if response.POST.get('c'+ str(user)) == 'clicked':
                    user.is_staff = True
                else:
                    user.is_staff = False
                user.save()                        
    
    return render(response, 'main/users.html', {'users':users})