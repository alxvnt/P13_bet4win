from django import forms


class JoinTeamForm(forms.Form):

    teamKey = forms.CharField(
        label="teamKey",
        widget=forms.TextInput(attrs={'placeholder': 'Clé', 'class': 'form-control'}),
        required=True

    )


# ajoutez un nom pour la team et une liste déroulante pour le championnat
class CreateTeamForm(forms.Form):
    CHOICES = [('1', 'Ligue 1'), ('2', 'Liga'), ('3', 'Bundesliga')]
    name = forms.CharField(
        label="name",
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Nom', 'class': 'form-control'}),
        required=True
    )
    champ = forms.ChoiceField(
        label="champ",
        widget=forms.Select,
        choices= CHOICES,
        required=True
    )
