from django import forms


class ComposeForm(forms.Form):
    """
    Form to send the request with whom you are going
    to connect for the chat
    """
    message = forms.CharField(
            widget=forms.TextInput(
                attrs={"class": "form-control"}
                )
            )
