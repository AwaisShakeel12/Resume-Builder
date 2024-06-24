from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):

    TEMPLATE_CHOICES = [
        ('aspremium', 'AS Premium'),
        ('black', 'Black Edition'),
    ]
    template_choice = forms.ChoiceField(choices=TEMPLATE_CHOICES, required=True)
    class Meta:
        model = Resume
        fields = '__all__'
        widgets = {
            'template_choice': forms.Select(attrs={'class': 'form-control'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            
            'Headline': forms.TextInput(attrs={'class': 'form-control'}),
            'aboutYou': forms.Textarea(attrs={'class': 'form-control'}),
            'eduTitle1': forms.TextInput(attrs={'class': 'form-control'}),
            'eduInstitute1': forms.TextInput(attrs={'class': 'form-control'}),
            'edu1Marks1': forms.TextInput(attrs={'class': 'form-control'}),
            'eduStartDate1': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'eduEndDate1': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'eduTitle2': forms.TextInput(attrs={'class': 'form-control'}),
            'eduInstitute2': forms.TextInput(attrs={'class': 'form-control'}),
            'edu1Marks2': forms.TextInput(attrs={'class': 'form-control'}),
            'eduStartDate2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'eduEndDate2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            
            'eduTitle3': forms.TextInput(attrs={'class': 'form-control'}),
            'eduInstitute3': forms.TextInput(attrs={'class': 'form-control'}),
            'edu1Marks3': forms.TextInput(attrs={'class': 'form-control'}),
            'eduStartDate3': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'eduEndDate3': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            
            'skil1': forms.TextInput(attrs={'class': 'form-control'}),
            'skil2': forms.TextInput(attrs={'class': 'form-control'}),
            'skil3': forms.TextInput(attrs={'class': 'form-control'}),
            'skil4': forms.TextInput(attrs={'class': 'form-control'}),
            'skil5': forms.TextInput(attrs={'class': 'form-control'}),
            'skil6': forms.TextInput(attrs={'class': 'form-control'}),
            'projectTitle1': forms.TextInput(attrs={'class': 'form-control'}),
            'projectDescription1': forms.Textarea(attrs={'class': 'form-control'}),
            'proStartDate1': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'proEndDate1': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'projectTitle2': forms.TextInput(attrs={'class': 'form-control'}),
            'projectDescription2': forms.Textarea(attrs={'class': 'form-control'}),
            'proStartDate2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'proEndDate2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

            'experienceLevel': forms.Select(attrs={'class': 'form-control'}),
            'experienceTitle1': forms.TextInput(attrs={'class': 'form-control'}),
            'experienceCompany1': forms.TextInput(attrs={'class': 'form-control'}),
            'expStartDate1': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'expEndDate1': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'experienceTitle2': forms.TextInput(attrs={'class': 'form-control'}),
            'experienceCompany2': forms.TextInput(attrs={'class': 'form-control'}),
            'expStartDate2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'expEndDate2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
          


        }
        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'address': 'Address',
            'Headline': 'Resume Headline',
            'aboutYou': 'About You',
            'eduTitle1': 'Education University',
            'eduInstitute1': 'Institute',
            'edu1Marks1': 'Marks',
            'eduStartDate1': 'Start Date ',
            'eduEndDate1': 'End Date ',
            'eduTitle2': 'Education Collage (Optional)',
            'eduInstitute2': 'Institute  (Optional) ',
            'edu1Marks2': 'Marks (Optional)',
            'eduStartDate2': 'Start Date',
            'eduEndDate2': 'End Date',
            'eduTitle3': 'Education School (Optional)',
            'eduInstitute3': 'Institute (Optional)',
            'edu1Marks3': 'Marks (Optional)',
            'eduStartDate3': 'Start Date',
            'eduEndDate3': 'End Date',
            'skil1': 'Skill 1',
            'skil2': 'Skill 2',
            'skil3': 'Skill 3 (Optional) ',
            'skil4': 'Skill 4 (Optional) ',
            'skil5': 'Skill 5 (Optional) ',
            'skil6': 'Skill 6 (Optional)',
            'projectTitle1': 'Project Title (Optional)',
            'projectDescription1': 'Project Description (Optional)',

            'projectTitle2': 'Project Title 2 (Optional)',
            'projectDescription2': 'Project Description 2 (Optional)',
    
            'experienceLevel': 'Experience Level',
            'experienceTitle1': 'Experience Title 1 (Optional)',
            'experienceCompany1': 'Company Name (Optional)',
            'expStartDate1': 'Experience Start Date',
            'expEndDate1': 'Experience End Date',
            'experienceTitle2': 'Experience Title 2 (Optional)',
            'experienceCompany2': 'Company Name (Optional)',
            'expStartDate2': 'Experience Start Date 2',
            'expEndDate2': 'Experience End Date 2',
        }
