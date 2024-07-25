from django import forms


class NoteForm(forms.Form):
    note = forms.CharField( 
        label=None,
        required=False,
        widget=forms.Textarea (
            attrs={
                'class':'form-control',
                
                }))
        