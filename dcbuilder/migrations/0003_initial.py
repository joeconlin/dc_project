# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Space'
        db.create_table(u'dcbuilder_space', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'dcbuilder', ['Space'])

        # Adding model 'Power'
        db.create_table(u'dcbuilder_power', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'dcbuilder', ['Power'])

        # Adding model 'Network'
        db.create_table(u'dcbuilder_network', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('myip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
        ))
        db.send_create_signal(u'dcbuilder', ['Network'])

        # Adding model 'Firewall'
        db.create_table(u'dcbuilder_firewall', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'dcbuilder', ['Firewall'])

        # Adding model 'LoadBalancer'
        db.create_table(u'dcbuilder_loadbalancer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'dcbuilder', ['LoadBalancer'])

        # Adding model 'Switch'
        db.create_table(u'dcbuilder_switch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'dcbuilder', ['Switch'])

        # Adding model 'Router'
        db.create_table(u'dcbuilder_router', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'dcbuilder', ['Router'])

        # Adding model 'Server'
        db.create_table(u'dcbuilder_server', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'dcbuilder', ['Server'])

        # Adding model 'Storage'
        db.create_table(u'dcbuilder_storage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'dcbuilder', ['Storage'])

        # Adding model 'Application'
        db.create_table(u'dcbuilder_application', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'dcbuilder', ['Application'])

        # Adding model 'Environment'
        db.create_table(u'dcbuilder_environment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('space', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.Space'])),
            ('power', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.Power'])),
            ('network', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.Network'])),
            ('firewall', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.Firewall'])),
            ('loadbalancer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.LoadBalancer'])),
            ('switch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.Switch'])),
            ('router', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.Router'])),
            ('server', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.Server'])),
            ('storage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.Storage'])),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.Application'])),
        ))
        db.send_create_signal(u'dcbuilder', ['Environment'])


    def backwards(self, orm):
        # Deleting model 'Space'
        db.delete_table(u'dcbuilder_space')

        # Deleting model 'Power'
        db.delete_table(u'dcbuilder_power')

        # Deleting model 'Network'
        db.delete_table(u'dcbuilder_network')

        # Deleting model 'Firewall'
        db.delete_table(u'dcbuilder_firewall')

        # Deleting model 'LoadBalancer'
        db.delete_table(u'dcbuilder_loadbalancer')

        # Deleting model 'Switch'
        db.delete_table(u'dcbuilder_switch')

        # Deleting model 'Router'
        db.delete_table(u'dcbuilder_router')

        # Deleting model 'Server'
        db.delete_table(u'dcbuilder_server')

        # Deleting model 'Storage'
        db.delete_table(u'dcbuilder_storage')

        # Deleting model 'Application'
        db.delete_table(u'dcbuilder_application')

        # Deleting model 'Environment'
        db.delete_table(u'dcbuilder_environment')


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