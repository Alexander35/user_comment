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
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Отчество',
                'type': 'text',
                'required': 'true',

            }),
        label='Отчество', max_length=100)   

    region = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Регион',
                'type': 'text',


            }),
        label='Регион', max_length=100)    

    town = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Город',
                'type': 'text',


            }),
        label='Город', max_length=100)      

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Контактный Телефон',
                'type': 'text',


            }),
        label='Контактный Телефон', max_length=100)                                    

    email = forms.EmailField(
    	widget=forms.TextInput(
    		attrs={
    				'class': 'form-control', 
    				'aria-describedby': 'emailHelp',
    				'placeholder': 'Enter Email',
    				'type': 'email',
    				'required': 'true',
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
