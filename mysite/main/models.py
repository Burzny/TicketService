from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ticket(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ticket", null=True)

    
def __str__(self):
		return self.name


class Message(models.Model):
	ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
	text = models.CharField(max_length=1000)
	date = models.DateTimeField(null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="message", null=True)	
 
	def __str__(self):
		return self.text