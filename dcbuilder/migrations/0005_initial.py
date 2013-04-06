# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Remember to use orm['appname.ModelName'] rather than "from appname.models..."

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'dcbuilder.application': {
            'Meta': {'object_name': 'Application'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dcbuilder.environment': {
            'Meta': {'object_name': 'Environment'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.Application']"}),
            'firewall': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.Firewall']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loadbalancer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.LoadBalancer']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'network': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.Network']"}),
            'power': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.Power']"}),
            'router': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.Router']"}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.Server']"}),
            'space': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.Space']"}),
            'storage': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.Storage']"}),
            'switch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.Switch']"})
        },
        u'dcbuilder.firewall': {
            'Meta': {'object_name': 'Firewall'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dcbuilder.loadbalancer': {
            'Meta': {'object_name': 'LoadBalancer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dcbuilder.network': {
            'Meta': {'object_name': 'Network'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'myip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dcbuilder.power': {
            'Meta': {'object_name': 'Power'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dcbuilder.router': {
            'Meta': {'object_name': 'Router'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dcbuilder.server': {
            'Meta': {'object_name': 'Server'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dcbuilder.space': {
            'Meta': {'object_name': 'Space'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dcbuilder.storage': {
            'Meta': {'object_name': 'Storage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dcbuilder.switch': {
            'Meta': {'object_name': 'Switch'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['dcbuilder']
    symmetrical = True
