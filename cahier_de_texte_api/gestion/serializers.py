from rest_framework import serializers
from .models import Campus, Filiere, Classe, Cours, Professeur, Responsable, Emargement, CahierDeTexte


class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = '__all__'
        extra_kwargs = {
            'nom': {'required': True},
            'region': {'required': True},
            'adresse': {'required': True}
        }
        

class FiliereSerializer(serializers.ModelSerializer):
    campus = CampusSerializer()
    
    class Meta:
        model = Filiere
        fields = ('id', 'nom', 'campus')

class ClasseSerializer(serializers.ModelSerializer):
    filiere = FiliereSerializer()
    
    class Meta:
        model = Classe
        fields = ('id', 'nom', 'filiere')

class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = '__all__'

class ProfesseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professeur
        fields = '__all__'

class ResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsable
        fields = '__all__'

class EmargementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emargement
        fields = '__all__'

class CahierDeTexteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CahierDeTexte
        fields = '__all__'