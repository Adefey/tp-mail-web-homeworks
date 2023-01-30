from django import forms

class AskForm(forms.Form):
    header = forms.CharField(label='Заголовок', max_length=128)
    full_text = forms.CharField(widget=forms.Textarea, label='Текст вопроса', max_length=512)
    tags = forms.CharField(label='Тэги через запятую', max_length=256)
