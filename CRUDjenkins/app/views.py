from app.serializers import PersonSerializer
from .models import Person
# Create your views here.
from rest_framework.generics import CreateAPIView

class PersonView(CreateAPIView):

    serializer_class = PersonSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    
