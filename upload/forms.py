from django import forms

class UploadForm(forms.Form):
    upload_file = forms.FileField(
	label='Select a file',
	help_text='max. 42 megabytes'
	)

