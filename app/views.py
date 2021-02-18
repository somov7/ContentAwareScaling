from django.core.files.temp import NamedTemporaryFile
from django.http import FileResponse
from rest_framework.decorators import api_view
from os import remove
from app.service import parseImage, cas


# Create your views here.


@api_view(['POST'])
def scaleImage(request):
    input_image = request.FILES['image']
    image = parseImage(input_image)
    cas(image)
    return_image = open('images/result.gif', 'rb')
    #remove('images/result.gif')
    return FileResponse(return_image)
