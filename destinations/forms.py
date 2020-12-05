from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': "Write your comment here...",
                'class': 'comment',
                   }
        )
    )
