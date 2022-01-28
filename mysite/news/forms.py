from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'photo', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})

        }
        # title = forms.CharField(max_length=150, label='Заголовок новости', help_text='Введите название для новости',
        #                         widget=forms.TextInput(attrs={'class': 'form-control'}))
        # content = forms.CharField(label='Текст новости', initial='Введите текст...', required=False,
        #                           widget=forms.Textarea(attrs={'class': 'form-control'}))
        # photo = forms.ImageField(label='', required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
        #
        # is_published = forms.BooleanField(label='Опубликовать сразу?', initial=True)
        #
        # category = forms.ModelChoiceField(empty_label='Выберите категорию...', label='Категория',
        #                                   queryset=Category.objects.all(),
        #                                   widget=forms.Select(attrs={'class': 'form-control'}))
