from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Votre pseudo', 'class': 'form-control'}),
        required=True
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs=
                                   {'placeholder': 'Mot de passe', 'class': 'form-control', 'autocomplete': 'off'}),
        required=True
    )


class RegisterForm(forms.Form):
    username = forms.CharField(
        label="Pseudo",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    last_name = forms.CharField(
        label="Nom",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    first_name = forms.CharField(
        label="Prénom",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    email = forms.EmailField(
        label='Adresse mail',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required = True

    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'autocomplete': 'off'}),
        required = True
    )
