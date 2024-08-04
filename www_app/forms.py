from django import forms
from .models import Agent, PropertyOwner, Member, Property, PropertyQuery, Feedback


class PropertyOwnerLoginForm(forms.Form):
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_phone', 'placeholder': 'Phone'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'id_password'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'id': 'id_phone', 'placeholder': 'Phone'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'id': 'id_password', 'placeholder': 'Password'})


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control', 'placeholder': ''})


class AgentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['id','phone', 'password', 'name', 'email', 'pic', 'address']
        widgets = {
            'password': forms.PasswordInput(),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control', 'placeholder':''})

class AgentLoginForm(forms.Form):
    phone = forms.CharField(max_length=20)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control', 'placeholder':''})


class PropertyOwnerForm(BootstrapModelForm):
    class Meta:
        model = PropertyOwner
        fields = '__all__'
        exclude = ['type']


class MemberForm(BootstrapModelForm):
    class Meta:
        model = Member
        fields = '__all__'


PROPERTY_TYPE_CHOICES = [
    ('House', 'House'),
    ('Flat', 'Flat'),
    ('Plot', 'Plot'),
    ('Land', 'Land'),
    ('Building', 'Building'),
    ('Bunglow', 'Bunglow'),
    ('Farmland', 'Farmland'),
]

class PropertyForm(BootstrapModelForm):
    class Meta:
        model = Property
        fields = '__all__'
        exclude = ['owner']
        widgets = {
            'property_type': forms.Select(choices=PROPERTY_TYPE_CHOICES,attrs={'class': 'form-select'})
        }


class PropertyQueryForm(BootstrapModelForm):
    class Meta:
        model = PropertyQuery
        fields = '__all__'
        widgets = {
            'type_of_property': forms.Select(choices=PROPERTY_TYPE_CHOICES,attrs={'class': 'form-select'})
        }


class FeedbackForm(BootstrapModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'




class MemberLoginForm(forms.Form):
    m_id = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Member ID'})
    )
    password = forms.CharField(
        max_length=32,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

    def clean(self):
        cleaned_data = super().clean()
        m_id = cleaned_data.get('m_id')
        password = cleaned_data.get('password')

        if m_id and password:
            try:
                member = Member.objects.get(m_id=m_id)
                if member.password != password:
                    raise forms.ValidationError("Incorrect password")
            except Member.DoesNotExist:
                raise forms.ValidationError("Member does not exist")
        
        return cleaned_data
    


class SeekerLoginForm(forms.Form):
    phone = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_phone', 'placeholder': 'Phone'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'id_password', 'placeholder': 'Password'}))



class SeekerRegisterForm(forms.Form):
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_phone', 'placeholder': 'Phone'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'id_password', 'placeholder': 'Password'}))
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_name', 'placeholder': 'Name'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'id_email', 'placeholder': 'Email'}))
    pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'id_address', 'placeholder': 'Address'}))