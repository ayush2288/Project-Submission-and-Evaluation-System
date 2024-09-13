from django import forms
from .models import GroupEvaluation, GroupEvaluation_ly, GroupEvaluation_ty, Sy_add_idea_no, Sy_idea_no, Ty_idea_no, final_idea, FinalMarksEvaluation

from django import forms
from .models import FinalMarksEvaluation

class FinalMarksEvaluationForm(forms.ModelForm):
    class Meta:
        model = FinalMarksEvaluation
        fields = [
            'final_marks_evaluation',
            'final_marks_student',
            # P1 Marks Evaluation
            'num01',
            'num1', 'num2',  
            'num21',         
            'num31', 'num32', 'num33', 'num34', 
            'num41',          
            'num51', 'num52', 'num53', 'num54',  
            
            # P2 Marks Evaluation
            'p2_num1', 
            'p2_num01', 
            'p2_num2',  
            'p2_num21',         
            'p2_num31', 'p2_num32', 'p2_num33', 'p2_num34', 
            'p2_num41',          
            'p2_num51', 'p2_num52', 'p2_num53', 'p2_num54',  
            
            # P3 Marks Evaluation
            'p3_num01',
            'p3_num1',
              'p3_num2',  
            'p3_num21',         
            'p3_num31', 'p3_num32', 'p3_num33', 'p3_num34', 
            'p3_num41',          
            'p3_num51', 'p3_num52', 'p3_num53', 'p3_num54',  
            
            # P4 Marks Evaluation
            'p4_num01',
            'p4_num1'
            , 'p4_num2',  
            'p4_num21',         
            'p4_num31', 'p4_num32', 'p4_num33', 'p4_num34', 
            'p4_num41',          
            'p4_num51', 'p4_num52', 'p4_num53', 'p4_num54',  
            
            'oral_practical'
        ]

        widgets = {
            'num01': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'num1': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'num2': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'num21': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'num31': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'num32': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'num33': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'num34': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'num41': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'num51': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'num52': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'num53': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'num54': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
           
            'p2_num01': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p2_num1': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p2_num2': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p2_num21': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p2_num31': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p2_num32': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p2_num33': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p2_num34': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p2_num41': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p2_num51': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p2_num52': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p2_num53': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p2_num54': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
        
            'p3_num01': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p3_num1': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p3_num2': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p3_num21': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p3_num31': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p3_num32': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p3_num33': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p3_num34': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p3_num41': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p3_num51': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p3_num52': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p3_num53': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p3_num54': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
           
            'p4_num01': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p4_num1': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p4_num2': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p4_num21': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p4_num31': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p4_num32': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p4_num33': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p4_num34': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p4_num41': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p4_num51': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p4_num52': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p4_num53': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
            'p4_num54': forms.RadioSelect(attrs={'class': 'horizontal-radio', 'required': False}),
           
            'oral_practical': forms.NumberInput(attrs={'class': 'form-control'}),
        }


    def clean(self):
        cleaned_data = super().clean()
        final_marks_evaluation = cleaned_data.get('final_marks_evaluation')
        final_marks_student = cleaned_data.get('final_marks_student')

        if final_marks_evaluation and final_marks_student:
            group_no = final_marks_evaluation.final_title.Add_sy_group_no
            branch = final_marks_evaluation.final_title.get_choices_branch()
            student_group_no = final_marks_student.sy_group_no.Add_sy_group_no
            student_branch = final_marks_student.sy_group_no.get_choices_branch()

            if group_no != student_group_no:
                self.add_error('final_marks_student', "The selected student does not belong to the chosen group.")
            elif branch != student_branch:
                self.add_error('final_marks_student', "The selected student does not belong to the chosen branch.")

        return cleaned_data

class FinalIdeaForm(forms.ModelForm):
    class Meta:
        model = final_idea
        fields = ['final_title', 'selected_idea']

        widgets = {
            'final_title': forms.Select(attrs={'class': 'form-control'}),
            'selected_idea': forms.TextInput(attrs={'class': 'form-control'}),
        }

class Sy_add_idea_no_form(forms.ModelForm):
    class Meta:
        model = Sy_add_idea_no
        fields = [
            'Add_sy_group_no', 
            'sy_idea_1', 'sy_idea_1_des', 
            'sy_idea_2', 'sy_idea_2_des', 
            'sy_idea_3', 'sy_idea_3_des', 
            'choices_guide', 'choices_branch', 'choices_year'
        ]

        common_text_input_attrs = {'class': 'form-control'}
        common_textarea_attrs = {'class': 'form-control', 'rows': 3}
        common_select_attrs = {'class': 'form-control'}

        widgets = {
            'choices_branch': forms.Select(attrs=common_select_attrs),
            'choices_guide': forms.Select(attrs=common_select_attrs),
            'choices_year': forms.Select(attrs=common_select_attrs),
            'sy_idea_1': forms.TextInput(attrs=common_text_input_attrs),
            'sy_idea_1_des': forms.Textarea(attrs=common_textarea_attrs),
            'sy_idea_2': forms.TextInput(attrs=common_text_input_attrs),
            'sy_idea_2_des': forms.Textarea(attrs=common_textarea_attrs),
            'sy_idea_3': forms.TextInput(attrs=common_text_input_attrs),
            'sy_idea_3_des': forms.Textarea(attrs=common_textarea_attrs),
        }

        labels = {
            'Add_sy_group_no': 'Enter Group Number',
            'choices_guide': 'Select Guide',
            'choices_year': 'Select Year',
            'choices_branch': 'Select Branch',
            'sy_idea_1': 'Enter the first idea here',
            'sy_idea_1_des': 'Provide a detailed description for the first idea',
            'sy_idea_2': 'Enter the second idea here',
            'sy_idea_2_des': 'Provide a detailed description for the second idea',
            'sy_idea_3': 'Enter the third idea here',
            'sy_idea_3_des': 'Provide a detailed description for the third idea'
        }

    def clean(self):
        cleaned_data = super().clean()
        Add_sy_group_no = cleaned_data.get('Add_sy_group_no')
        sy_idea_1 = cleaned_data.get('sy_idea_1')
        sy_idea_2 = cleaned_data.get('sy_idea_2')
        sy_idea_3 = cleaned_data.get('sy_idea_3')
        choices_guide = cleaned_data.get('choices_guide')
        choices_branch = cleaned_data.get('choices_branch')
        choices_year = cleaned_data.get('choices_year')

        if Sy_add_idea_no.objects.filter(
            Add_sy_group_no=Add_sy_group_no,
            sy_idea_1=sy_idea_1,
            sy_idea_2=sy_idea_2,
            sy_idea_3=sy_idea_3,
            choices_guide=choices_guide,
            choices_branch=choices_branch,
            choices_year=choices_year
        ).exists() and Sy_add_idea_no.objects.filter(
            Add_sy_group_no=Add_sy_group_no,
            choices_branch=choices_branch,
            choices_year=choices_year
        ).exists() and Sy_add_idea_no.objects.filter(
            Add_sy_group_no=None,
            sy_idea_1=None,
            sy_idea_2=None,
            sy_idea_3=None,
            choices_guide=None,
            choices_branch=None,
            choices_year=None
        ).exists():
            raise forms.ValidationError('Form with these details has already been submitted, or some required fields are empty')

        
        # Additional check to ensure no required fields are empty
        if not Add_sy_group_no or not sy_idea_1 or not sy_idea_2 or not sy_idea_3 or not choices_guide or not choices_branch or not choices_year:
            raise forms.ValidationError('Please fill in all the required fields.')

        return cleaned_data

    def clean_Add_sy_group_no(self):
        Add_sy_group_no = self.cleaned_data.get('Add_sy_group_no')
        if Add_sy_group_no is None or Add_sy_group_no < 0:
            raise forms.ValidationError('Group number must be positive.')
        return Add_sy_group_no


class Sy_SomeOtherForm(forms.ModelForm):
    sy_group_no = forms.ModelChoiceField(
        queryset=Sy_add_idea_no.objects.all(),  # Fetch all records
        label='Group No',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Sy_idea_no
        fields = ['sy_name', 'sy_roll_no','sy_email', 'sy_group_no']
        widgets = {
            'sy_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sy_roll_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'sy_email': forms.TextInput(attrs={'class': 'form-control'}),
            'sy_group_no': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'sy_name': 'Enter Name:',
            'sy_roll_no': 'Enter your Roll No:',
            'sy_email': 'Enter your Somaiya mail:',
            'sy_group_no': 'Select your Group No:',
        }


class final_idea_form(forms.ModelForm):
    final_title = forms.ModelChoiceField(
        queryset=Sy_add_idea_no.objects.all(),
        label='Final Topic',
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'final_title'})
    )

    selected_idea = forms.ChoiceField(
        label='Select Idea',
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'selected_idea'})
    )

    class Meta:
        model = final_idea
        fields = ['final_title', 'selected_idea']
        labels = {
            'final_title': 'Final Title:',
            'selected_idea': 'Select Idea:'
        }

    def __init__(self, *args, **kwargs):
        super(final_idea_form, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['selected_idea'].choices = self.get_idea_choices(self.instance.final_title)

    def get_idea_choices(self, final_title):
        if final_title:
            return [
                (final_title.sy_idea_1, final_title.sy_idea_1),
                (final_title.sy_idea_2, final_title.sy_idea_2),
                (final_title.sy_idea_3, final_title.sy_idea_3)
            ]
        return []

    def clean(self):
        cleaned_data = super().clean()
        final_title = cleaned_data.get("final_title")
        selected_idea = cleaned_data.get("selected_idea")

        if final_title and selected_idea:
            available_choices = [idea for idea, _ in self.get_idea_choices(final_title)]
            if selected_idea not in available_choices:
                self.add_error('selected_idea', "The selected idea is not valid for the chosen group.")





class GroupEvaluationForm(forms.ModelForm):
    sy_idea_no = forms.ModelChoiceField(
        queryset=Sy_idea_no.objects.all(),
        empty_label="Select an Idea No",
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = GroupEvaluation
        fields = [
            'group_name', 'roll_no', 'group_year', 'num01', 'sy_idea_no', 'oral_practical', 
            'num1', 'num2', 'num21', 'num31', 'num32', 'num33', 'num34',
            'num41', 'num51', 'num52', 'num53', 'num54'
        ]
        widgets = {
            'num01': forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
            'num1': forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
            'num2': forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
            'num21': forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
            'num31': forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
            'num32': forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
            'num33': forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
            'num34': forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
            'num41': forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
            'num51': forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
            'num52': forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
            'num53': forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
            'num54': forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
        }

class RatingForm1(forms.Form):
    CHOICES1 = [
        ('5', 'Cites substantial current quality literature'),
        ('4', 'Cites reasonable quantity of current quality literature'),
        ('3', 'Cites current literature'),
        ('2', 'Does not cite any current quality literature'),
    ]
    CHOICES2 = [
        ('5', 'Provides good understanding of literature cited'),
        ('4', 'Provides understanding of literature cited'),
        ('3', 'Exhibits poor understanding of literature cited'),
        ('2', 'Very poor in understanding literature cited'),
    ]

    criteria_1 = forms.ChoiceField(
        choices=CHOICES1,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )
    criteria_2 = forms.ChoiceField(
        choices=CHOICES2,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )

class RatingForm2(forms.Form):
    CHOICES3 = [
        ('10', 'Very good clarity about the subject matter'),
        ('8', 'Somewhat good clarity'),
        ('6', 'Not so good clarity'),
        ('4', 'Very poor'),
    ]
    
    criteria_3 = forms.ChoiceField(
        choices=CHOICES3,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )

class RatingForm3(forms.Form):
    CHOICES4 = [
        ('3', 'Written in own, grammatically correct language'),
        ('2.4', 'Written in own language, has many grammatical errors'),
        ('1.8', 'Language not good'),
        ('1.2', 'Mostly copied'),
    ]
    CHOICES5 = [
        ('2', 'Recommended format used'),
        ('1.4', 'Mostly in recommended format'),
        ('1.2', 'Many deviations from format'),
        ('0.8', 'No format'),
    ]
    CHOICES6 = [
        ('3', 'Very good presentation'),
        ('2.4', 'Somewhat good presentation'),
        ('1.8', 'Messy presentation'),
        ('1.2', 'Very poor presentation'),
    ]
    CHOICES7 = [
        ('2', 'Very good Communication Skill'),
        ('1.4', 'Good Communication Skill'),
        ('1.2', 'Poor Communication Skill'),
        ('0.8', 'Very poor Communication Skill'),
    ]
    
    criteria_4 = forms.ChoiceField(
        choices=CHOICES4,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )
    criteria_5 = forms.ChoiceField(
        choices=CHOICES5,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )
    criteria_6 = forms.ChoiceField(
        choices=CHOICES6,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )
    criteria_7 = forms.ChoiceField(
        choices=CHOICES7,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )

class RatingForm4(forms.Form):
    CHOICES8 = [
        ('10', 'International (Refereed) print Journal'),
        ('8', 'National (Refereed) print Journal'),
        ('6', 'International (Refereed) Conference'),
        ('4', 'National (Refereed) Conference and Online Journal'),
    ]
    
    criteria_8 = forms.ChoiceField(
        choices=CHOICES8,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )

class RatingForm5(forms.Form):
    CHOICES9 = [
        ('2.5', 'Highly effective communication'),
        ('2.0', 'Good communication'),
        ('1.5', 'Adequate communication'),
        ('1.0', 'Ineffective communication'),
    ]
    CHOICES10 = [
        ('2.5', 'Equal contribution from all members'),
        ('2.0', 'Good contribution from most members'),
        ('1.5', 'Uneven contribution'),
        ('1.0', 'Poor contribution from members'),
    ]
    CHOICES11 = [
        ('2.5', 'Excellent coordination'),
        ('2.0', 'Good coordination'),
        ('1.5', 'Adequate coordination'),
        ('1.0', 'Poor coordination'),
    ]
    CHOICES12 = [
        ('2.5', 'Excellent coordination'),
        ('2.0', 'Good coordination'),
        ('1.5', 'Adequate coordination'),
        ('1.0', 'Poor coordination'),
    ]

    criteria_9 = forms.ChoiceField(
        choices=CHOICES9,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )
    criteria_10 = forms.ChoiceField(
        choices=CHOICES10,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )
    criteria_11 = forms.ChoiceField(
        choices=CHOICES11,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )
    criteria_12 = forms.ChoiceField(
        choices=CHOICES12,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )


# for TY

class Ty_SomeOtherForm(forms.ModelForm):
    class Meta:
        model = Ty_idea_no
        fields = ['ty_idea', 'ty_grp_no']
        labels = {
            'ty_idea': 'Enter Idea:',
            'ty_grp_no': 'Enter Group Number:',
        }


class GroupEvaluation_tyForm(forms.ModelForm):
    ty_idea_no = forms.ModelChoiceField(
        queryset=Ty_idea_no.objects.all(),
        empty_label="Select an Idea No",
        widget=forms.Select(),
        required=False
    )
    class Meta:
        model = GroupEvaluation_ty
        fields = [
            'group_name','roll_no', 'group_year', 'num01', 'ty_idea_no', 'oral_practical', 
            'num1', 'num2', 'num21', 'num31', 'num32', 'num33',
            'num41', 'num51', 'num61', 'num71'
        ]
        widgets = {
            'num01': forms.RadioSelect(),
            'num1': forms.RadioSelect(),
            'num2': forms.RadioSelect(),
            'num21': forms.RadioSelect(),
            'num31': forms.RadioSelect(),
            'num32': forms.RadioSelect(),
            'num33': forms.RadioSelect(),
            'num41': forms.RadioSelect(),
            'num51': forms.RadioSelect(),
            'num61': forms.RadioSelect(),
            'num71': forms.RadioSelect(),
        }

class RatingForm1_ty(forms.Form):
    CHOICES1 = [
        ('5', 'Cites substantial current quality literature'),
        ('4', 'Cites reasonable quantity of current quality literature'),
        ('3', 'Cites current literature'),
        ('2', 'Does not cite any current quality literature'),
    ]
    CHOICES2 = [
        ('5', 'Provides good understanding of literature cited'),
        ('4', 'Provides understanding of literature cited'),
        ('3', 'Exhibits poor understanding of literature cited'),
        ('2', 'Very poor in understanding literature cited'),
    ]

    criteria_1 = forms.ChoiceField(
        choices=CHOICES1,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )
    criteria_2 = forms.ChoiceField(
        choices=CHOICES2,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )

class RatingForm2_ty(forms.Form):
    CHOICES3 = [
        ('10', 'Very good clarity about the subject matter'),
        ('8', 'Somewhat good clarity'),
        ('6', 'Not so good clarity'),
        ('4', 'Very poor'),
    ]
    
    criteria_3 = forms.ChoiceField(
        choices=CHOICES3,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )

class RatingForm3_ty(forms.Form):
    CHOICES4 = [
        ('4', 'Written in own, grammatically correct language'),
        ('3.2', 'Written in own language, has many grammatical errors'),
        ('2.4', 'Language not good'),
        ('1.6', 'Mostly copied'),
    ]
    CHOICES5 = [
        ('4', 'Very good presentation'),
        ('3.2', 'Somewhat good presentation'),
        ('2.4', 'Messy presentation'),
        ('1.6', 'Very poor presentation'),
    ]
    CHOICES6 = [
        ('2', 'Recommended format used'),
        ('1.4', 'Mostly in recommended format'),
        ('1.2', 'Many deviations from format'),
        ('0.8', 'No format'),
    ]
    
    criteria_4 = forms.ChoiceField(
        choices=CHOICES4,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )
    criteria_5 = forms.ChoiceField(
        choices=CHOICES5,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )
    criteria_6 = forms.ChoiceField(
        choices=CHOICES6,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )

class RatingForm4_ty(forms.Form):
    CHOICES7 = [
        ('10', 'Very good Communication Skill'),
        ('8', 'Good Communication Skill'),
        ('6', 'Poor Communication Skill'),
        ('4', 'Very poor Communication Skill'),
    ]
    
    criteria_7 = forms.ChoiceField(
        choices=CHOICES7,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )

class RatingForm5_ty(forms.Form):
    CHOICES8 = [
        ('10', 'International (Refereed) print Journal'),
        ('8', 'National (Refereed) print Journal'),
        ('6', 'International (Refereed) Conference'),
        ('4', 'National (Refereed) Conference and Online Journal'),
    ]
    criteria_8 = forms.ChoiceField(
        choices=CHOICES8,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )

class RatingForm6_ty(forms.Form):
    CHOICES9 = [
        ('2.5', 'Highly effective communication and Equal contribution from all members'),
        ('2.0', 'Good communication and good contribution from most members'),
        ('1.5', 'Adequate communication and uneven contribution'),
        ('1.0', 'Ineffective communication and poor contribution from members'),
    ]
    criteria_9 = forms.ChoiceField(
        choices=CHOICES9,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )

class RatingForm7_ty(forms.Form):
    CHOICES10 = [
        ('10', 'Very clear, concise, well organized and logical'),
        ('8', 'Mostly clear, concise and organized'),
        ('6', 'Somewhat clear, concise and organized'),
        ('4', 'Lacks clarity and conciseness and Poorly organized.'),
    ]
    criteria_10 = forms.ChoiceField(
        choices=CHOICES10,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )




# for LY
class GroupEvaluation_lyForm(forms.ModelForm):
    class Meta:
        model = GroupEvaluation_ly
        fields = '__all__'
        widgets = {
            'num01': forms.RadioSelect(),
            'num1': forms.RadioSelect(),
            'num2': forms.RadioSelect(),
            'num21': forms.RadioSelect(),
            'num31': forms.RadioSelect(),
            'num32': forms.RadioSelect(),
            'num33': forms.RadioSelect(),
            'num41': forms.RadioSelect(),
            'num51': forms.RadioSelect(),
            'num61': forms.RadioSelect(),
            'num71': forms.RadioSelect(),
            'num81': forms.RadioSelect(),
            'num91': forms.RadioSelect(),
            'num101': forms.RadioSelect(),
           
        }

# Substantial current and good quality literature (10)
class RatingForm1_ly(forms.Form):
    CHOICES1 = [
        ('5', 'Cites substantial current quality literature'),
        ('4', 'Cites reasonable quantity of current quality literature'),
        ('3', 'Cites current literature'),
        ('2', 'Does not cite any current quality literature'),
    ]
    CHOICES2 = [
        ('5', 'Provides good understanding of literature cited'),
        ('4', 'Provides understanding of literature cited'),
        ('3', 'Exhibits poor understanding of literature cited'),
        ('2', 'Very poor in understanding literature cited'),
    ]

    criteria_1 = forms.ChoiceField(
        choices=CHOICES1,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )
    criteria_2 = forms.ChoiceField(
        choices=CHOICES2,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )

 # Answering Questions Posed by Examiner (10)
class RatingForm2_ly(forms.Form):
    CHOICES3 = [
        ('10', 'Very good clarity about the subject matter'),
        ('8', 'Somewhat good clarity'),
        ('6', 'Not so good clarity'),
        ('4', 'Very poor'),
    ]
    
    criteria_3 = forms.ChoiceField(
        choices=CHOICES3,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )

    # Presentation skills(10)
class RatingForm3_ly(forms.Form):
    CHOICES4 = [
        ('4', 'Written in own, grammatically correct language'),
        ('3.2', 'Written in own language, has many grammatical errors'),
        ('2.4', 'Language not good'),
        ('1.6', 'Mostly copied'),
    ]
    CHOICES5 = [
        ('4', 'Very good presentation'),
        ('3.2', 'Somewhat good presentation'),
        ('2.4', 'Messy presentation'),
        ('1.6', 'Very poor presentation'),
    ]
    CHOICES6 = [
        ('2', 'Recommended format used'),
        ('1.4', 'Mostly in recommended format'),
        ('1.2', 'Many deviations from format'),
        ('0.8', 'No format'),
    ]
    
    criteria_4 = forms.ChoiceField(
        choices=CHOICES4,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )
    criteria_5 = forms.ChoiceField(
        choices=CHOICES5,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )
    criteria_6 = forms.ChoiceField(
        choices=CHOICES6,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )

    # Communication skills(10):
class RatingForm4_ly(forms.Form):
    CHOICES7 = [
        ('10', 'Very good Communication Skill'),
        ('8', 'Good Communication Skill'),
        ('6', 'Poor Communication Skill'),
        ('4', 'Very poor Communication Skill'),
    ]
    
    criteria_7 = forms.ChoiceField(
        choices=CHOICES7,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )

# Quality of Research Paper (10)
class RatingForm5_ly(forms.Form):
    CHOICES8 = [
        ('10', 'International (Refereed) print Journal'),
        ('8', 'National (Refereed) print Journal'),
        ('6', 'International (Refereed) Conference'),
        ('4', 'National (Refereed) Conference and Online Journal'),
    ]
    criteria_8 = forms.ChoiceField(
        choices=CHOICES8,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )

# Teamwork and Collaboration (10)
class RatingForm6_ly(forms.Form):
    CHOICES9 = [
        ('2.5', 'Highly effective communication and Equal contribution from all members'),
        ('2.0', 'Good communication and good contribution from most members'),
        ('1.5', 'Adequate communication and uneven contribution'),
        ('1.0', 'Ineffective communication and poor contribution from members'),
    ]
    criteria_9 = forms.ChoiceField(
        choices=CHOICES9,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )


# Documentation and Reporting (10)
class RatingForm7_ly(forms.Form):
    CHOICES10 = [
        ('10', 'Very clear, concise, well organized and logical'),
        ('8', 'Mostly clear, concise and organized'),
        ('6', 'Somewhat clear, concise and organized'),
        ('4', 'Lacks clarity and conciseness and Poorly organized.'),
    ]
    criteria_10 = forms.ChoiceField(
        choices=CHOICES10,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )

    # Originality (10)
class RatingForm8_ly(forms.Form):
    CHOICES11 = [
        ('10', 'Highly innovative and original'),
        ('8', 'Some innovation and originality'),
        ('6', 'Minimal innovation and originality'),
        ('4', 'Lacks innovation and originality.'),
    ]
    criteria_11 = forms.ChoiceField(
        choices=CHOICES11,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )

    # Creativity (10)
class RatingForm9_ly(forms.Form):
    CHOICES12 = [
        ('10', 'Demonstrates exceptional creativity'),
        ('8', 'Shows good creativity'),
        ('6', 'Demonstrates average creativity'),
        ('4', 'Lacks creativity'),
    ]
    criteria_12 = forms.ChoiceField(
        choices=CHOICES12,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )


   # Design and Technical Feasibility (10)
class RatingForm10_ly(forms.Form):
    CHOICES13 = [
        ('10', 'Design is highly effective and it is highly feasible and practical'),
        ('8', 'Design is mostly effective and technically feasible and practical'),
        ('6', 'Design is somewhat effective and feasibility is questionable'),
        ('4', 'Design is ineffective and neither feasible nor practical'),
    ]
    criteria_13 = forms.ChoiceField(
        choices=CHOICES13,
        widget=forms.RadioSelect(attrs={'class': 'horizontal-radio'})
    )

