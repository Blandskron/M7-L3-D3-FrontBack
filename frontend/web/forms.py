from django import forms


class AuthorCreateForm(forms.Form):
    name = forms.CharField(max_length=150, label="Nombre")
    birth_date = forms.DateField(
        label="Fecha de nacimiento",
        required=False,
        widget=forms.DateInput(attrs={"type": "date"})
    )


class BookCreateForm(forms.Form):
    title = forms.CharField(max_length=200, label="Título")
    isbn = forms.CharField(max_length=13, label="ISBN")
    author_id = forms.ChoiceField(label="Autor")  # lo llenamos en el view

    published_date = forms.DateField(
        label="Fecha publicación",
        required=False,
        widget=forms.DateInput(attrs={"type": "date"})
    )

    # Entrada simple para n categorías:
    # formato: "Novela:1, Historia:2, Ciencia:3"
    categories_input_text = forms.CharField(
        label="Categorías (nombre:prioridad)",
        required=False,
        help_text='Ej: "Novela:1, Realismo mágico:2" (prioridad opcional)',
        widget=forms.Textarea(attrs={"rows": 2, "placeholder": "Novela:1, Realismo mágico:2"})
    )