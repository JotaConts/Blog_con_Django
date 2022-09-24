#Formularios para el sitio.
#Para conocer los froms de django ver: https://docs.djangoproject.com/en/4.0/ref/forms/fields/

from django import forms
from django.core import validators

class Form_article(forms.Form):
    title = forms.CharField(
        label="Título",
        max_length= 500,
        required=True, #Si esta habilitado o no para escribir
        widget=forms.TextInput(
            attrs={ # agrega atributos a la etiqueta html que le corresponda
                'placeholder': 'Escribe el título',
                'class': 'titulo_from_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'Titulo muy corto'),
            validators.RegexValidator('^[A-Za-z0-9ñÑ áéíóúÁÉÍÓÚ¡!¿?.]*$', 'Caracteres no permitidos', 'invalid title')
        ]
    )
    
    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea,
        validators=[
            validators.MaxLengthValidator(20, 'Exceso de texto')
        ]
    )
    public_options = [
        (1, 'Sí'),
        (0, 'No')
    ]
    public = forms.TypedChoiceField(
        label = "Publicado",
        choices = public_options
    )