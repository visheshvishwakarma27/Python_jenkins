from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path,include
from app.views import PersonView
from rest_framework import routers
from . import views
# from django.conf.urls import  url
from django.urls import re_path as url
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   )
)

Person_router = routers.DefaultRouter()
Person_router.register(r'^PersonAPI', PersonView, basename='PersonView')

urlpatterns = [

    # Schema 
    
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
    # url(r'^api/', include(Person_router.urls)),
    path('api/post', views.PersonView.as_view(), name="PersonView"),
]