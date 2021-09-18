from django.forms import ModelForm, fields
from app.models import Carros

class CarrosForm(ModelForm):
  class Meta:
    model = Carros
    fields = ['modelo', 'marca', 'ano']