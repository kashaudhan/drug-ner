from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from .models import Drug
import pickle
import os


@api_view(['POST'])
def post_text(request):
  text = request.data['text']
  result = list(Drug.objects.filter(salt_name__icontains=text).values())
  ex1 = "James went to London to buy Ibuprofen last year 2019"
  mdl = pickle.load(open(os.path.dirname(__file__) + '/../model.pkl', 'rb'))
  docx2 = mdl(ex1)
  for entity in docx2.ents:
    print(entity,entity.label_)
  print(result)
  return JsonResponse({'text': result})