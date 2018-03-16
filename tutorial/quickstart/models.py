# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Course(models.Model):
    code = models.CharField(db_column='Code', max_length=20)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    changes = models.CharField(db_column='Changes', max_length=50, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=50, blank=True, null=True)  # Field name made lowercase.
    credit = models.IntegerField(db_column='Credit', blank=True, null=True)  # Field name made lowercase.
    size = models.IntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    p1 = models.IntegerField(db_column='P1', blank=True, null=True)  # Field name made lowercase.
    p2 = models.IntegerField(db_column='P2', blank=True, null=True)  # Field name made lowercase.
    p3 = models.IntegerField(db_column='P3', blank=True, null=True)  # Field name made lowercase.
    p4 = models.IntegerField(db_column='P4', blank=True, null=True)  # Field name made lowercase.
    p5 = models.IntegerField(db_column='P5', blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    curriculumid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'course'


class Curriculum(models.Model):
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    degreeprogramid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'curriculum'


class Degreeprogram(models.Model):
    code = models.CharField(db_column='Code', unique=True, max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'degreeprogram'

class Implementation(models.Model):
    courseid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'implementation'


class Room(models.Model):
    code = models.CharField(db_column='Code', unique=True, max_length=20)  # Field name made lowercase.
    seats = models.IntegerField(db_column='Seats', blank=True, null=True)  # Field name made lowercase.
    topic = models.CharField(db_column='Topic', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'room'


class RoomImplementation(models.Model):
    implementationid = models.IntegerField(primary_key=True)
    roomid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_implementation'
        unique_together = (('implementationid', 'roomid'),)


class Subgroup(models.Model):
    code = models.CharField(db_column='Code', max_length=20, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=50, blank=True, null=True)  # Field name made lowercase.
    groupid = models.IntegerField()
    degreeprogramid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subgroup'


class SubgroupImplementation(models.Model):
    subgroupid = models.IntegerField(primary_key=True)
    implementationid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subgroup_implementation'
        unique_together = (('subgroupid', 'implementationid'),)


class Teacher(models.Model):
    code = models.CharField(db_column='Code', unique=True, max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teacher'


class TeacherDegreeprogram(models.Model):
    degreeprogramid = models.IntegerField(primary_key=True)
    teacherid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'teacher_degreeprogram'
        unique_together = (('degreeprogramid', 'teacherid'),)


class TeacherImplementation(models.Model):
    teacherid = models.IntegerField(primary_key=True)
    implementationid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'teacher_implementation'
        unique_together = (('teacherid', 'implementationid'),)