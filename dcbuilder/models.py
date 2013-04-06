# vim: ai ts=4 sts=4 et sw=4
from django.db import models

class Environment(models.Model):
    name = models.CharField('Environment Name', max_length=100, help_text="What is the name of this")
    space = 
    power =
    network =

    def __unicode__(self):
        return self.name

class Network(models.Model):

class Firewall(models.Model):
    
class LoadBalancer(models.Model):

class Switch(models.Model):

class Router(models.Model):

class Server(models.Model):

class Storage(models.Model):

class Interface(models.Model):

class Application(models.Model):



class StorageArea(models.Model):
        name = models.CharField('Area Name', max_length=100, help_text="What is the name of this ")
        created_date = models.DateTimeField('Date record created', auto_now_add=True)
        updated = models.DateTimeField( auto_now=True)
        def __unicode__(self):
           return self.name

