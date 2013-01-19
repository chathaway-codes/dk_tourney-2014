# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'File'
        db.create_table('tournament_file', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('tournament', ['File'])

        # Adding model 'Player'
        db.create_table('tournament_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('handle', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('tournament', ['Player'])

        # Adding M2M table for field games on 'Player'
        db.create_table('tournament_player_games', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('player', models.ForeignKey(orm['tournament.player'], null=False)),
            ('game', models.ForeignKey(orm['tournament.game'], null=False))
        ))
        db.create_unique('tournament_player_games', ['player_id', 'game_id'])

        # Adding M2M table for field platforms on 'Player'
        db.create_table('tournament_player_platforms', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('player', models.ForeignKey(orm['tournament.player'], null=False)),
            ('platform', models.ForeignKey(orm['tournament.platform'], null=False))
        ))
        db.create_unique('tournament_player_platforms', ['player_id', 'platform_id'])

        # Adding model 'Game'
        db.create_table('tournament_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('platforms', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournament.Platform'])),
        ))
        db.send_create_signal('tournament', ['Game'])

        # Adding M2M table for field files on 'Game'
        db.create_table('tournament_game_files', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game', models.ForeignKey(orm['tournament.game'], null=False)),
            ('file', models.ForeignKey(orm['tournament.file'], null=False))
        ))
        db.create_unique('tournament_game_files', ['game_id', 'file_id'])

        # Adding model 'Platform'
        db.create_table('tournament_platform', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('tournament', ['Platform'])

        # Adding model 'Computer'
        db.create_table('tournament_computer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tournament.Player'], unique=True)),
            ('cpu', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('gpu', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ram', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('hdd', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('wat', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('other', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('tournament', ['Computer'])

        # Adding model 'Team'
        db.create_table('tournament_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('tournament', ['Team'])

        # Adding M2M table for field members on 'Team'
        db.create_table('tournament_team_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm['tournament.team'], null=False)),
            ('player', models.ForeignKey(orm['tournament.player'], null=False))
        ))
        db.create_unique('tournament_team_members', ['team_id', 'player_id'])

        # Adding M2M table for field tournaments on 'Team'
        db.create_table('tournament_team_tournaments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm['tournament.team'], null=False)),
            ('tournament', models.ForeignKey(orm['tournament.tournament'], null=False))
        ))
        db.create_unique('tournament_team_tournaments', ['team_id', 'tournament_id'])

        # Adding model 'Tournament'
        db.create_table('tournament_tournament', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournament.Game'])),
            ('team_game', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('team_size', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('tournament', ['Tournament'])

        # Adding M2M table for field players on 'Tournament'
        db.create_table('tournament_tournament_players', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tournament', models.ForeignKey(orm['tournament.tournament'], null=False)),
            ('player', models.ForeignKey(orm['tournament.player'], null=False))
        ))
        db.create_unique('tournament_tournament_players', ['tournament_id', 'player_id'])


    def backwards(self, orm):
        # Deleting model 'File'
        db.delete_table('tournament_file')

        # Deleting model 'Player'
        db.delete_table('tournament_player')

        # Removing M2M table for field games on 'Player'
        db.delete_table('tournament_player_games')

        # Removing M2M table for field platforms on 'Player'
        db.delete_table('tournament_player_platforms')

        # Deleting model 'Game'
        db.delete_table('tournament_game')

        # Removing M2M table for field files on 'Game'
        db.delete_table('tournament_game_files')

        # Deleting model 'Platform'
        db.delete_table('tournament_platform')

        # Deleting model 'Computer'
        db.delete_table('tournament_computer')

        # Deleting model 'Team'
        db.delete_table('tournament_team')

        # Removing M2M table for field members on 'Team'
        db.delete_table('tournament_team_members')

        # Removing M2M table for field tournaments on 'Team'
        db.delete_table('tournament_team_tournaments')

        # Deleting model 'Tournament'
        db.delete_table('tournament_tournament')

        # Removing M2M table for field players on 'Tournament'
        db.delete_table('tournament_tournament_players')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'tournament.computer': {
            'Meta': {'object_name': 'Computer'},
            'cpu': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'gpu': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'hdd': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'player': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['tournament.Player']", 'unique': 'True'}),
            'ram': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'wat': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'tournament.file': {
            'Meta': {'object_name': 'File'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'tournament.game': {
            'Meta': {'object_name': 'Game'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tournament.File']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'platforms': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tournament.Platform']"})
        },
        'tournament.platform': {
            'Meta': {'object_name': 'Platform'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'tournament.player': {
            'Meta': {'object_name': 'Player'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'games': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tournament.Game']", 'null': 'True', 'blank': 'True'}),
            'handle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'platforms': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tournament.Platform']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'tournament.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tournament.Player']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tournaments': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tournament.Tournament']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'tournament.tournament': {
            'Meta': {'object_name': 'Tournament'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tournament.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'players': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tournament.Player']", 'symmetrical': 'False', 'blank': 'True'}),
            'team_game': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'team_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tournament']