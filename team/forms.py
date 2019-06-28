from django import forms


class JoinTeamForm(forms.Form):

    teamKey = forms.CharField(
        label="teamKey",
        widget=forms.TextInput(attrs={'placeholder': 'Clé', 'class': 'form-control'}),
        required=True

    )


# ajoutez un nom pour la team et une liste déroulante pour le championnat
class CreateTeamForm(forms.Form):
    pass
