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