
from models import Course,Curriculum,Degreeprogram,Implementation,Room,RoomImplementation,Subgroup,SubgroupImplementation,Teacher,TeacherDegreeprogram,TeacherImplementation
from rest_framework import serializers


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('url', 'code', 'name', 'changes', 'language', 'credit', 'size', 'p1', 'p2', 'p3', 'p4', 'p5', 'total', 'curriculumid')

class CurriculumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curriculum
        fields = ('url', 'name', 'degreeprogramid')

class DegreeprogramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Degreeprogram
        fields = ('url', 'code', 'name')

		
class ImplementationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Implementation
        fields = ('url', 'courseid')		
		
class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('url', 'code', 'seats',  'topic')		

class RoomImplementationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoomImplementation
        fields = ('url', 'implementationid', 'rooim')

class SubgroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subgroup
        fields = ('url', 'code', 'department',  'groupid', 'degreeprogramid')

class SubgroupImplementationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubgroupImplementation
        fields = ('url', 'subgroupid', 'implementationid')

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ('url', 'code', 'name')		
		
class TeacherDegreeprogramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeacherDegreeprogram
        fields = ('url', 'degreeprogramid', 'teacherid')	
		
class TeacherImplementationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeacherImplementation
        fields = ('url', 'teacherid', 'implementationid')	