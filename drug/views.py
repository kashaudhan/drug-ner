from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from .models import Drug
import pickle
import os
from django.db.models import Q


@api_view(['POST'])
def post_text(request):
  text = request.data['text']
  mdl = pickle.load(open(os.path.dirname(__file__) + '/../model.pkl', 'rb'))
  docx2 = mdl(text)
  drug_name = []
  for entity in docx2.ents:
    if entity.label_ == 'DRUG':
      drug_name.append(entity)
  result = list(Drug.objects.filter(salt_name__in=drug_name).values())
  return JsonResponse({'drug': result})