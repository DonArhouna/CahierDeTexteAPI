""" from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('api/', include('gestion.urls')),  
] """

# gestion/urls.py
# gestion/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CampusViewSet,
    FiliereViewSet,
    ClasseViewSet,
    CoursViewSet,
    ProfesseurViewSet,
    ResponsableViewSet,
    EmargementViewSet,
    CahierDeTexteViewSet
)

router = DefaultRouter()
router.register(r'campuses', CampusViewSet, basename='campus')
router.register(r'filieres', FiliereViewSet, basename='filiere')
router.register(r'classes', ClasseViewSet, basename='classe')
router.register(r'cours', CoursViewSet, basename='cours')
router.register(r'professeurs', ProfesseurViewSet, basename='professeur')
router.register(r'responsables', ResponsableViewSet, basename='responsable')
router.register(r'emargements', EmargementViewSet, basename='emargement')
router.register(r'cahiers-de-texte', CahierDeTexteViewSet, basename='cahierdetexte')

urlpatterns = [
    path('', include(router.urls)),
]