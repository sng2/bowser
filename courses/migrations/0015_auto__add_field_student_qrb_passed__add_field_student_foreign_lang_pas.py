# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Student.qrb_passed'
        db.add_column(u'courses_student', 'qrb_passed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Student.foreign_lang_passed'
        db.add_column(u'courses_student', 'foreign_lang_passed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Enrollment.date_taken'
        db.alter_column(u'courses_enrollment', 'date_taken', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Enrollment.rating'
        db.alter_column(u'courses_enrollment', 'rating', self.gf('django.db.models.fields.IntegerField')(null=True))
        # Adding unique constraint on 'Enrollment', fields ['student', 'course']
        db.create_unique(u'courses_enrollment', ['student_id', 'course_id'])

        # Adding field 'Course.dept'
        db.add_column(u'courses_course', 'dept',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)


        # Changing field 'Course.comments'
        db.alter_column(u'courses_course', 'comments', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):
        # Removing unique constraint on 'Enrollment', fields ['student', 'course']
        db.delete_unique(u'courses_enrollment', ['student_id', 'course_id'])

        # Deleting field 'Student.qrb_passed'
        db.delete_column(u'courses_student', 'qrb_passed')

        # Deleting field 'Student.foreign_lang_passed'
        db.delete_column(u'courses_student', 'foreign_lang_passed')


        # Changing field 'Enrollment.date_taken'
        db.alter_column(u'courses_enrollment', 'date_taken', self.gf('django.db.models.fields.DateField')(default=''))

        # Changing field 'Enrollment.rating'
        db.alter_column(u'courses_enrollment', 'rating', self.gf('django.db.models.fields.IntegerField')(default=''))
        # Deleting field 'Course.dept'
        db.delete_column(u'courses_course', 'dept')


        # Changing field 'Course.comments'
        db.alter_column(u'courses_course', 'comments', self.gf('django.db.models.fields.TextField')(default=''))

    models = {
        u'courses.course': {
            'Meta': {'ordering': "['name']", 'object_name': 'Course'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'dept': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'dists': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courses.Distribution']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'prof': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'prof_site': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'courses.course_bucket': {
            'Meta': {'object_name': 'Course_Bucket'},
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courses.Course']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'courses.distribution': {
            'Meta': {'object_name': 'Distribution'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '200'}),
            'num_courses': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'courses.enrollment': {
            'Meta': {'unique_together': "[('student', 'course')]", 'object_name': 'Enrollment'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Course']"}),
            'date_taken': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Student']"})
        },
        u'courses.major': {
            'Meta': {'object_name': 'Major'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Undecided'", 'max_length': '200'})
        },
        u'courses.student': {
            'Meta': {'object_name': 'Student'},
            'class_year': ('django.db.models.fields.CharField', [], {'default': "'fy'", 'max_length': '200'}),
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courses.Course']", 'through': u"orm['courses.Enrollment']", 'symmetrical': 'False'}),
            'distribution_requirements_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'foreign_lang_passed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gpa': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'major_requirements_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_major': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'primary major'", 'to': u"orm['courses.Major']"}),
            'qrb_passed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'secondary_major': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'secondary major'", 'null': 'True', 'to': u"orm['courses.Major']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['courses']