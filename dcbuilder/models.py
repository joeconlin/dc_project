# vim: ai ts=4 sts=4 et sw=4
from django.db import models

class Space(models.Model):
    name = models.CharField('Name', max_length=100, help_text="")

    def __unicode__(self):
        return self.name

class Power(models.Model):
    name = models.CharField('Name', max_length=100, help_text="")

    def __unicode__(self):
        return self.name


class Network(models.Model):
    name = models.CharField('Name', max_length=100, help_text="")
    myip = models.IPAddressField('ip',)
    def __unicode__(self):
        return self.name

class Firewall(models.Model):
    name = models.CharField('Name', max_length=100, help_text="")

    def __unicode__(self):
        return self.name
    
class LoadBalancer(models.Model):
    name = models.CharField('Name', max_length=100, help_text="")

    def __unicode__(self):
        return self.name

class Switch(models.Model):
    name = models.CharField('Name', max_length=100, help_text="")

    def __unicode__(self):
        return self.name

class Router(models.Model):
    name = models.CharField('Name', max_length=100, help_text="Select a name for this router")

    def __unicode__(self):
        return self.name

class Server(models.Model):
    name = models.CharField('Name', max_length=100, help_text="Select a name for this Server")

    def __unicode__(self):
        return self.name

class Storage(models.Model):
    name = models.CharField('Name', max_length=100, help_text="")

    def __unicode__(self):
        return self.name

#class Interface(models.Model):

class Application(models.Model):
    name = models.CharField('Name', max_length=100, help_text="")

    def __unicode__(self):
        return self.name

class Environment(models.Model):
    name = models.CharField('Environment Name', max_length=100, help_text="Select a name for this environment")
    space = models.ForeignKey(Space, verbose_name="Linked Space", blank=True, null=True)
    power = models.ForeignKey(Power, verbose_name="Linked Power", blank=True, null=True)
    network = models.ForeignKey(Network, verbose_name='Linked Network', blank=True, null=True)
    firewall = models.ForeignKey(Firewall, verbose_name="Linked Firewall", blank=True, null=True)
    loadbalancer = models.ForeignKey(LoadBalancer, verbose_name="Linked LB", blank=True, null=True)
    switch = models.ForeignKey(Switch, verbose_name="Linked Switch", blank=True, null=True)
    router = models.ForeignKey(Router, verbose_name="Linked Router", blank=True, null=True)
    server = models.ForeignKey(Server, verbose_name="Linked Server", blank=True, null=True)
    storage = models.ForeignKey(Storage, verbose_name="Linked Storage", blank=True, null=True)
    application = models.ForeignKey(Application, verbose_name="Linked App", blank=True, null=True)
    def __unicode__(self):
        return self.name
