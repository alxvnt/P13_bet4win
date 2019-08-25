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


week_dict = [
    "2019-07-22",
    "2019-07-29",
    "2019-08-05",
    "2019-08-12",
    "2019-08-19",
    "2019-08-26",
    "2019-09-02",
    "2019-09-09",
    "2019-09-16",
    "2019-09-23",
    "2019-09-30",
    "2019-10-14",
    "2019-10-21",
    "2019-10-28",
    "2019-11-04",
    "2019-11-18",
    "2019-11-25",
    "2019-12-02",
    "2019-12-09",
    "2020-12-16",
    "2020-01-06",
    "2020-01-20",
    "2020-01-27",
    "2020-02-03",
    "2020-02-10",
    "2020-02-17",
    "2020-02-24",
    "2020-03-02",
    "2020-03-09",
    "2020-03-16",
    "2020-03-30",
    "2020-04-06",
    "2020-04-13",
    "2020-04-20",
    "2020-04-27",
    "2020-05-04",
    "2020-05-11"]


class DayChampForm(forms.Form):
    CHOICES = [
        ("2019-07-22", "Journée 1"),
        ("2019-07-29", "Journée 2"),
        ("2019-08-05", "Journée 3"),
        ("2019-08-12", "Journée 4"),
        ("2019-08-19", "Journée 5"),
        ("2019-08-26", "Journée 6"),
        ("2019-09-02", "Journée 7"),
        ("2019-09-09", "Journée 8"),
        ("2019-09-16", "Journée 9"),
        ("2019-09-23", "Journée 10"),
        ("2019-09-30", "Journée 11"),
        ("2019-10-14", "Journée 12"),
        ("2019-10-21", "Journée 13"),
        ("2019-10-28", "Journée 14"),
        ("2019-11-04", "Journée 15"),
        ("2019-11-18", "Journée 16"),
        ("2019-11-25", "Journée 17"),
        ("2019-12-02", "Journée 18"),
        ("2019-12-09", "Journée 19"),
        ("2020-12-16", "Journée 20"),
        ("2020-01-06", "Journée 21"),
        ("2020-01-20", "Journée 22"),
        ("2020-01-27", "Journée 23"),
        ("2020-02-03", "Journée 24"),
        ("2020-02-10", "Journée 25"),
        ("2020-02-17", "Journée 26"),
        ("2020-02-24", "Journée 27"),
        ("2020-03-02", "Journée 28"),
        ("2020-03-09", "Journée 29"),
        ("2020-03-16", "Journée 30"),
        ("2020-03-30", "Journée 31"),
        ("2020-04-06", "Journée 32"),
        ("2020-04-13", "Journée 33"),
        ("2020-04-20", "Journée 34"),
        ("2020-04-27", "Journée 35"),
        ("2020-05-04", "Journée 36"),
        ("2020-05-11", "Journée 37")]
    date = forms.CharField(
        max_length=15,
        widget=forms.Select(choices=CHOICES),
        required=True
    )
