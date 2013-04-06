# vim: ai ts=4 sts=4 et sw=4
from django.db import models

class Space(models.Model):
    name = models.CharField('Name', max_length=100)

    def __unicode__(self):
        return self.name

class Power(models.Model):
    name = models.CharField('Name', max_length=100)

    def __unicode__(self):
        return self.name


class Network(models.Model):
    name = models.CharField('Name', max_length=100)

    def __unicode__(self):
        return self.name

class Firewall(models.Model):
    name = models.CharField('Name', max_length=100)

    def __unicode__(self):
        return self.name
    
class LoadBalancer(models.Model):
    name = models.CharField('Name', max_length=100)

    def __unicode__(self):
        return self.name

class Switch(models.Model):
    name = models.CharField('Name', max_length=100)

    def __unicode__(self):
        return self.name

class Router(models.Model):
    name = models.CharField('Name', max_length=100)

    def __unicode__(self):
        return self.name

class Server(models.Model):
    name = models.CharField('Name', max_length=100)

    def __unicode__(self):
        return self.name

class Storage(models.Model):
    name = models.CharField('Name', max_length=100)

    def __unicode__(self):
        return self.name

#class Interface(models.Model):

class Application(models.Model):
    name = models.CharField('Name', max_length=100)

    def __unicode__(self):
        return self.name

class Environment(models.Model):
    name = models.CharField('Environment Name', max_length=100, help_text="What is the name of this")
    space = models.ForeignKey(Space, verbose_name="Linked Space")
    power = models.ForeignKey(Power, verbose_name="Linked Power")
    network = models.ForeignKey(Network, verbose_name='Linked Network')
    firewall = models.ForeignKey(Firewall, verbose_name="Linked Firewall")
    loadbalancer = models.ForeignKey(LoadBalancer, verbose_name="Linked LB")
    switch = models.ForeignKey(Switch, verbose_name="Linked Switch")
    router = models.ForeignKey(Router, verbose_name="Linked Router")
    server = models.ForeignKey(Server, verbose_name="Linked Server")
    storage = models.ForeignKey(Storage, verbose_name="Linked Storage")
    application = models.ForeignKey(Application, verbose_name="Linked App")
    def __unicode__(self):
        return self.name
