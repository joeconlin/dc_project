from django.contrib import admin
from dcbuilder.models import Environment,Space,Power,Network,Firewall,LoadBalancer,Switch,Router,Server,Storage,Application

admin.site.register(Environment)
admin.site.register(Space)
admin.site.register(Power)
admin.site.register(Network)
admin.site.register(Firewall)
admin.site.register(LoadBalancer)
admin.site.register(Switch)
admin.site.register(Router)
admin.site.register(Server)
admin.site.register(Storage)
admin.site.register(Application)

