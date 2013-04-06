# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customer'
        db.create_table(u'dcbuilder_customer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'dcbuilder', ['Customer'])

        # Adding model 'Proposal'
        db.create_table(u'dcbuilder_proposal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('detail', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.Customer'], null=True, blank=True)),
            ('environment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcbuilder.Environment'], null=True, blank=True)),
        ))
        db.send_create_signal(u'dcbuilder', ['Proposal'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table(u'dcbuilder_customer')

        # Deleting model 'Proposal'
        db.delete_table(u'dcbuilder_proposal')


    models = {
        u'dcbuilder.application': {
            'Meta': {'object_name': 'Application'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dcbuilder.customer': {
            'Meta': {'object_name': 'Customer'},
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
        u'dcbuilder.proposal': {
            'Meta': {'object_name': 'Proposal'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.Customer']", 'null': 'True', 'blank': 'True'}),
            'detail': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dcbuilder.Environment']", 'null': 'True', 'blank': 'True'}),
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