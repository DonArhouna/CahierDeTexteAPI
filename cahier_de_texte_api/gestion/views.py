from rest_framework import viewsets
from .models import Campus, Filiere, Classe, Cours, Professeur, Responsable, Emargement, CahierDeTexte
from .serializers import CampusSerializer, FiliereSerializer, ClasseSerializer, CoursSerializer, ProfesseurSerializer, ResponsableSerializer, EmargementSerializer, CahierDeTexteSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

class CampusViewSet(viewsets.ModelViewSet):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print("Données reçues:", request.data)  # Log pour débogage
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
 
    
class FiliereViewSet(viewsets.ModelViewSet):
    queryset = Filiere.objects.all()
    serializer_class = FiliereSerializer


class ClasseViewSet(viewsets.ModelViewSet):
    queryset = Classe.objects.all().order_by('id') 
    serializer_class = ClasseSerializer


class CoursViewSet(viewsets.ModelViewSet):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer

class ProfesseurViewSet(viewsets.ModelViewSet):
    queryset = Professeur.objects.all()
    serializer_class = ProfesseurSerializer

class ResponsableViewSet(viewsets.ModelViewSet):
    queryset = Responsable.objects.all()
    serializer_class = ResponsableSerializer

class EmargementViewSet(viewsets.ModelViewSet):
    queryset = Emargement.objects.all()
    serializer_class = EmargementSerializer

class CahierDeTexteViewSet(viewsets.ModelViewSet):
    queryset = CahierDeTexte.objects.all()
    serializer_class = CahierDeTexteSerializer