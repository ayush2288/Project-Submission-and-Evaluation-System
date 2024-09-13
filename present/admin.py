from django.contrib import admin

from present.forms import FinalMarksEvaluationForm
from .models import GroupEvaluation_ly, GroupEvaluation_ty, Sy_add_idea_no, Sy_idea_no, final_idea


class SyAddIdeaNoAdmin(admin.ModelAdmin):
    list_display = (
        'get_grp_no', 'get_sy_idea_1', 'get_sy_idea_1_description',
        'get_sy_idea_2', 'get_sy_idea_2_description',
        'get_sy_idea_3', 'get_sy_idea_3_description',
        'get_choices_guide', 'get_choices_branch', 'get_choices_year',
    )
    
    def get_grp_no(self, obj):
        return obj.get_grp_no()  # Ensure this method exists in the model
    get_grp_no.short_description = 'Group No.'
    
    def get_sy_idea_1(self, obj):
        return obj.get_sy_idea_1()  # Ensure this method exists in the model
    get_sy_idea_1.short_description = 'Idea 1'
    
    def get_sy_idea_1_description(self, obj):
        return obj.get_sy_idea_1_description()  # Ensure this method exists in the model
    get_sy_idea_1_description.short_description = 'Description 1'
    
    def get_sy_idea_2(self, obj):
        return obj.get_sy_idea_2()  # Ensure this method exists in the model
    get_sy_idea_2.short_description = 'Idea 2'
    
    def get_sy_idea_2_description(self, obj):
        return obj.get_sy_idea_2_description()  # Ensure this method exists in the model
    get_sy_idea_2_description.short_description = 'Description 2'
    
    def get_sy_idea_3(self, obj):
        return obj.get_sy_idea_3()  # Ensure this method exists in the model
    get_sy_idea_3.short_description = 'Idea 3'
    
    def get_sy_idea_3_description(self, obj):
        return obj.get_sy_idea_3_description()  # Ensure this method exists in the model
    get_sy_idea_3_description.short_description = 'Description 3'
    
    def get_choices_guide(self, obj):
        return obj.get_choices_guide()  # Ensure this method exists in the model
    get_choices_guide.short_description = 'Choices Guide'

    def get_choices_branch(self, obj):
        return obj.get_choices_branch()  # Ensure this method exists in the model
    get_choices_branch.short_description = 'Choices Branch'

    def get_choices_year(self, obj):
        return obj.get_choices_year()  # Ensure this method exists in the model
    get_choices_year.short_description = 'Choices Year'

admin.site.register(Sy_add_idea_no, SyAddIdeaNoAdmin)




class finalIdeaFormAdmin(admin.ModelAdmin):
    list_display = ('final_title', 'selected_idea')

admin.site.register(final_idea, finalIdeaFormAdmin)


class SyIdeaNoAdmin(admin.ModelAdmin):
    list_display = ('sy_name','sy_roll_no','sy_email', 'sy_group_no')

admin.site.register(Sy_idea_no, SyIdeaNoAdmin)

from django.contrib import admin
from .models import FinalMarksEvaluation

class FinalMarksEvaluationAdmin(admin.ModelAdmin):
    form = FinalMarksEvaluationForm
    list_display = (
        'get_student_name', 'get_group_no', 'get_final_idea', 'oral_practical', 
        'get_idea_description', 'get_branch', 'get_guide', 'get_year',
        'total_marks', 'p2_total_marks', 'p3_total_marks', 'p4_total_marks',
    )

    def get_student_name(self, obj):
  
        return obj.final_marks_student.sy_name if obj.final_marks_student else "No student associated"
    get_student_name.short_description = 'Student Name'
        
    def get_group_no(self, obj):
        return obj.final_marks_student.sy_group_no.Add_sy_group_no if obj.final_marks_student and obj.final_marks_student.sy_group_no else "No group available"
    get_group_no.short_description = 'Group No'

    def get_final_idea(self, obj):
        return obj.final_marks_evaluation.selected_idea
    get_final_idea.short_description = 'Final Idea'

    def get_idea_description(self, obj):
        final_title = obj.final_marks_evaluation.final_title
        selected_idea = obj.final_marks_evaluation.selected_idea

        if selected_idea == final_title.sy_idea_1:
            return final_title.get_sy_idea_1_description()
        elif selected_idea == final_title.sy_idea_2:
            return final_title.get_sy_idea_2_description()
        elif selected_idea == final_title.sy_idea_3:
            return final_title.get_sy_idea_3_description()
        
        return "No description available."
    get_idea_description.short_description = 'Idea Description'

    def get_branch(self, obj):
        return obj.final_marks_student.sy_group_no.get_choices_branch() if obj.final_marks_student else "No branch available"
    get_branch.short_description = 'Branch'

    def get_guide(self, obj):
        return obj.final_marks_student.sy_group_no.get_choices_guide() if obj.final_marks_student else "No guide available"
    get_guide.short_description = 'Guide'

    def get_year(self, obj):
        return obj.final_marks_student.sy_group_no.get_choices_year() if obj.final_marks_student else "No year available"
    get_year.short_description = 'Year'

admin.site.register(FinalMarksEvaluation, FinalMarksEvaluationAdmin)


class GroupEvaluation_tyAdmin(admin.ModelAdmin):
    list_display = (
        'group_name', 'roll_no', 'num01', 'group_year', 'get_ty_grp_no', 'get_ty_idea',
        'eval1_total_display', 'eval2_total_display', 'eval3_total_display',
        'eval4_total_display', 'eval5_total_display', 'eval6_total_display',
        'eval7_total_display', 'calculate_teamwork_display', 'oral_practical'
    )


    def get_ty_grp_no(self, obj):
        return obj.ty_idea_no.ty_grp_no
    get_ty_grp_no.short_description = 'Group No.'

    def get_ty_idea(self, obj):
        return obj.ty_idea_no.ty_idea
    get_ty_idea.short_description = 'Group Idea'

    def eval1_total_display(self, obj):
        return obj.eval1_total()
    eval1_total_display.short_description = 'Substantial'

    def eval2_total_display(self, obj):
        return obj.eval2_total()
    eval2_total_display.short_description = 'Answering'

    def eval3_total_display(self, obj):
        return obj.eval3_total()
    eval3_total_display.short_description = 'Presentation'

    def eval4_total_display(self, obj):
        return obj.eval4_total()
    eval4_total_display.short_description = 'Quality of Research'

    def eval5_total_display(self, obj):
        return obj.eval5_total()
    eval5_total_display.short_description = 'Teamwork and Collaboration'

    def eval6_total_display(self, obj):
        return obj.eval6_total()
    eval6_total_display.short_description = 'Documentation and Reporting'

    def eval7_total_display(self, obj):
        return obj.eval7_total()
    eval7_total_display.short_description = 'Other'

    def calculate_teamwork_display(self, obj):
        return obj.calculate_teamwork()
    calculate_teamwork_display.short_description = 'Avg'

admin.site.register(GroupEvaluation_ty, GroupEvaluation_tyAdmin)



#for LY
class GroupEvaluation_lyAdmin(admin.ModelAdmin):
    list_display = (
        'group_no', 'group_name','group_idea','num01' ,'group_year',
        'eval1_total',
        'eval2_total',
        'eval3_total',
        'eval4_total',
        'eval5_total',
        'eval6_total',
        'eval7_total',
        'eval8_total',
        'eval9_total',
        'eval10_total',
        'calculate_teamwork',
        'oral_practical'
    )

    def eval1_total(self, obj):
        return obj.eval1_total()
    eval1_total.short_description = 'Substantial'

    def eval2_total(self, obj):
        return obj.eval2_total()
    eval2_total.short_description = 'Answering'

    def eval3_total(self, obj):
        return obj.eval3_total()
    eval3_total.short_description = 'Presentation'

    def eval4_total(self, obj):
        return obj.eval4_total()
    eval4_total.short_description = 'Communication'

    def eval5_total(self, obj):
        return obj.eval5_total()
    eval5_total.short_description = 'Quality of Research'

    def eval6_total(self, obj):
        return obj.eval6_total()
    eval6_total.short_description = 'Teamwork and Collaboration'

    def eval7_total(self, obj):
        return obj.eval7_total()
    eval7_total.short_description = 'Documentation and Reporting'

    def eval8_total(self, obj):
        return obj.eval8_total()
    eval8_total.short_description = 'Originality'

    def eval9_total(self, obj):
        return obj.eval9_total()
    eval9_total.short_description = 'Creativity'

    def eval10_total(self, obj):
        return obj.eval10_total()
    eval10_total.short_description = 'Design and Technical Feasibility'

admin.site.register(GroupEvaluation_ly, GroupEvaluation_lyAdmin)
