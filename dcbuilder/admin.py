from django.forms import ModelForm
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from dcbuilder.models import Environment,Space,Power,Network,Firewall,LoadBalancer,Switch,Router,Server,Storage,Application,Proposal,Customer
from suit_redactor.widgets import RedactorWidget

class PageForm(ModelForm):
    class Meta:
        widgets = {
            'detail': RedactorWidget(editor_options={'lang': 'en'})
        }

class ProposalAdmin(ModelAdmin):
    form = PageForm
    fieldsets = [
        ('General', {
            'fields': ('name', 'customer', 'environment')
        }),
      ('Detail Fieldset', {'classes': ('full-width',), 'fields': ('detail',)})
    ]

admin.site.register(Proposal, ProposalAdmin)
admin.site.register(Customer)
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

