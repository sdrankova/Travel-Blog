from django import forms

from destinations.models import Destination


class CommentForm(forms.Form):
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': "Write your comment here...",
                'class': 'comment',
            }
        )
    )


class EditCreateForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ('title', 'destination', 'description', 'image',)


class FilterForm(forms.Form):
    ORDER_ASC = 'asc'
    ORDER_DESC = 'desc'
    ORDER_CHOICES = (
        (ORDER_ASC, 'Ascending'),
        (ORDER_DESC, 'Descending'),
    )
    text = forms.CharField(required=False)
    order = forms.ChoiceField(
        choices=ORDER_CHOICES,
        required=False,
    )
