from django import forms
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={
                'class': 'form-control',
                'placeholder': 'DD/MM/AAAA'
            }
        )
    )

    class Meta:
        model = Funcionario
        fields = '__all__'