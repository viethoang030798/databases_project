from models import Course,Curriculum,Degreeprogram,Implementation,Room,RoomImplementation,Subgroup,SubgroupImplementation,Teacher,TeacherDegreeprogram,TeacherImplementation
from rest_framework import viewsets
from tutorial.quickstart.serializers import CourseSerializer, CurriculumSerializer, DegreeprogramSerializer, ImplementationSerializer, RoomSerializer ,RoomImplementationSerializer ,SubgroupSerializer ,SubgroupImplementationSerializer ,TeacherSerializer ,TeacherDegreeprogramSerializer ,TeacherImplementationSerializer 

class CourseViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
	
class CurriculumViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer
	
class DegreeprogramViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = Degreeprogram.objects.all()
    serializer_class = DegreeprogramSerializer
	

class ImplementationViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = Implementation.objects.all()
    serializer_class = ImplementationSerializer
	
class RoomViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
	
class RoomImplementationViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = RoomImplementation.objects.all()
    serializer_class = RoomImplementationSerializer
	
class SubgroupViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = Subgroup.objects.all()
    serializer_class = SubgroupSerializer
	
class SubgroupImplementationViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = SubgroupImplementation.objects.all()
    serializer_class = SubgroupImplementationSerializer
	
class TeacherViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
	
class TeacherDegreeprogramViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = TeacherDegreeprogram.objects.all()
    serializer_class = TeacherDegreeprogramSerializer
	
class TeacherImplementationViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = TeacherImplementation.objects.all()
    serializer_class = TeacherImplementationSerializer
	
	
