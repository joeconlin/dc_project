# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Environment.network'
        db.alter_column(u'dcbuilder_environment', 'network_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.Network'], null=True))

        # Changing field 'Environment.power'
        db.alter_column(u'dcbuilder_environment', 'power_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.Power'], null=True))

        # Changing field 'Environment.space'
        db.alter_column(u'dcbuilder_environment', 'space_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.Space'], null=True))

        # Changing field 'Environment.firewall'
        db.alter_column(u'dcbuilder_environment', 'firewall_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.Firewall'], null=True))

        # Changing field 'Environment.storage'
        db.alter_column(u'dcbuilder_environment', 'storage_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.Storage'], null=True))

        # Changing field 'Environment.server'
        db.alter_column(u'dcbuilder_environment', 'server_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.Server'], null=True))

        # Changing field 'Environment.application'
        db.alter_column(u'dcbuilder_environment', 'application_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.Application'], null=True))

        # Changing field 'Environment.switch'
        db.alter_column(u'dcbuilder_environment', 'switch_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.Switch'], null=True))

        # Changing field 'Environment.router'
        db.alter_column(u'dcbuilder_environment', 'router_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.Router'], null=True))

        # Changing field 'Environment.loadbalancer'
        db.alter_column(u'dcbuilder_environment', 'loadbalancer_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.LoadBalancer'], null=True))

    def backwards(self, orm):

        # Changing field 'Environment.network'
        db.alter_column(u'dcbuilder_environment', 'network_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['dcbuilder.Network']))

        # Changing field 'Environment.power'
        db.alter_column(u'dcbuilder_environment', 'power_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['dcbuilder.Power']))

        # Changing field 'Environment.space'
        db.alter_column(u'dcbuilder_environment', 'space_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['dcbuilder.Space']))

        # Changing field 'Environment.firewall'
        db.alter_column(u'dcbuilder_environment', 'firewall_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['dcbuilder.Firewall']))

        # Changing field 'Environment.storage'
        db.alter_column(u'dcbuilder_environment', 'storage_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['dcbuilder.Storage']))

        # Changing field 'Environment.server'
        db.alter_column(u'dcbuilder_environment', 'server_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['dcbuilder.Server']))

        # Changing field 'Environment.application'
        db.alter_column(u'dcbuilder_environment', 'application_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['dcbuilder.Application']))

        # Changing field 'Environment.switch'
        db.alter_column(u'dcbuilder_environment', 'switch_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['dcbuilder.Switch']))

        # Changing field 'Environment.router'
        db.alter_column(u'dcbuilder_environment', 'router_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['dcbuilder.Router']))

        # Changing field 'Environment.loadbalancer'
        db.alter_column(u'dcbuilder_environment', 'loadbalancer_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['dcbuilder.LoadBalancer']))

    models = {
        u'dcbuilder.application': {
            'Meta': {'object_name': 'Application'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dcbuilder.environment': {
            'Meta': {'object_name': 'Environment'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.Application']", 'null': 'True', 'blank': 'True'}),
            'firewall': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.Firewall']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loadbalancer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.LoadBalancer']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'network': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.Network']", 'null': 'True', 'blank': 'True'}),
            'power': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.Power']", 'null': 'True', 'blank': 'True'}),
            'router': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.Router']", 'null': 'True', 'blank': 'True'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.Server']", 'null': 'True', 'blank': 'True'}),
            'space': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.Space']", 'null': 'True', 'blank': 'True'}),
            'storage': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.Storage']", 'null': 'True', 'blank': 'True'}),
            'switch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.Switch']", 'null': 'True', 'blank': 'True'})
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