from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Usuario

class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Por favor, confirma la contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = Usuario
        fields = ('username', 'email')
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2
        
    def save(self, commit=True):
        usuario = super(RegistroForm, self).save(commit=False)
        usuario.set_password(self.cleaned_data["password1"])
        if commit:
            usuario.save()
        return usuario

class UsuarioActualizarForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password', 'universo', 'rango')
    
    def clean_password(self):
        return self.initial['password']
        
        
    
    