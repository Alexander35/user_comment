from django import forms
from django.contrib.auth.models import User
from .models import Comment, Region, Town

class NewCommentForm(forms.Form):

    user_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
                'type': 'text',
                'required': 'true',
            }),
        label='Имя', max_length=100)  

    user_family_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
                'type': 'text',
                'required': 'true',
            }),
        label='Фамилия', max_length=100)    

    patronomic = forms.CharField(
    	required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Отчество',
                'type': 'text',
            }),
        label='Отчество', max_length=100)

    region = forms.ModelChoiceField(
    	required=False,
    	queryset=Region.objects.all(),
    	empty_label="/Выберите Регион/",
		widget=forms.Select(attrs={'class': 'form-control'})     	
    	)

    town = forms.ModelChoiceField(
    	required=False,
    	queryset=Town.objects.all(),
    	empty_label="/Выберите Город/",
    	widget=forms.Select(attrs={'class': 'form-control'})   	
    	)    		       

    phone = forms.CharField(
    	required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Телефон (555)555-55-55',
                'type': 'tel',
                'pattern': '\(\d{3}\)\d{3}-\d{2}-\d{2}'
            }),
        label='Контактный Телефон', max_length=100)                                    

    email = forms.EmailField(
    	required=False,
    	widget=forms.TextInput(
    		attrs={
    				'class': 'form-control', 
    				'aria-describedby': 'emailHelp',
    				'placeholder': 'Enter Email',
    				'type': 'email',
    			}),
    	label='Email address', max_length=100)

    comment = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Коментарий',
                'type': 'text',
            }),
        label='Коментарий', max_length=1000)       
