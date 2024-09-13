from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import FinalMarksEvaluation, GroupEvaluation, GroupEvaluation_ly, GroupEvaluation_ty, Sy_add_idea_no, Sy_idea_no, final_idea
from django.template import loader
from .forms import FinalMarksEvaluationForm, GroupEvaluation_lyForm, GroupEvaluation_tyForm, GroupEvaluationForm, RatingForm1, RatingForm2, RatingForm3, RatingForm4, RatingForm5, Sy_SomeOtherForm, Sy_add_idea_no_form, Ty_SomeOtherForm
from django.shortcuts import render
from .forms import RatingForm1, RatingForm2, RatingForm3, RatingForm4, RatingForm5
from django.db.models import Count
import requests
import time
from .models import Sy_add_idea_no
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from itertools import groupby
from operator import attrgetter


# Temp idea code👇

def finalize_idea_page(request, group_id):
    group = get_object_or_404(Sy_add_idea_no, id=group_id)
    
    if request.method == "POST":
        selected_idea = request.POST.get('selected_idea')
        final_idea_instance = final_idea.objects.create(final_title=group, selected_idea=selected_idea)
        final_idea_instance.save()
        return redirect('add_idea_no_listz')  # Redirect to the appropriate view after finalization

    context = {
        'group': group,
        'ideas': [
            (group.sy_idea_1, group.sy_idea_1),
            (group.sy_idea_2, group.sy_idea_2),
            (group.sy_idea_3, group.sy_idea_3)
        ]
    }
    return render(request, 'myapp/finalize_idea_page.html', context)






def check_plagiarism(request, group_id):
    # Fetch the specific group based on the provided ID
    group = get_object_or_404(Sy_add_idea_no, id=group_id)
    
    # Prepare the data for each idea
    ideas = [
        {
            'title': group.sy_idea_1,
            'description': group.sy_idea_1_des,
            'text': f"{group.sy_idea_1}: {group.sy_idea_1_des}"
        },
        {
            'title': group.sy_idea_2,
            'description': group.sy_idea_2_des,
            'text': f"{group.sy_idea_2}: {group.sy_idea_2_des}"
        },
        {
            'title': group.sy_idea_3,
            'description': group.sy_idea_3_des,
            'text': f"{group.sy_idea_3}: {group.sy_idea_3_des}"
        },
    ]
    
    api_key = '7y98LUb3ji-6fr02Pt13kOTqVXVg6Zp4'
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    
    plagiarism_results = []
    
    for idea in ideas:
        data = {
            'text': idea['text']
        }
        
        # Step 1: Create a new document
        response = requests.post('https://plagiarismcheck.org/api/v1/documents', headers=headers, json=data)
        
        if response.status_code == 201:
            document = response.json()
            document_id = document['id']
            
            # Step 2: Initiate the plagiarism check
            check_response = requests.post(f'https://plagiarismcheck.org/api/v1/documents/{document_id}/checks', headers=headers)
            
            if check_response.status_code == 201:
                check_data = check_response.json()
                check_id = check_data['id']
                
                # Step 3: Poll for the check result
                while True:
                    result_response = requests.get(f'https://plagiarismcheck.org/api/v1/checks/{check_id}', headers=headers)
                    if result_response.status_code == 200:
                        result_data = result_response.json()
                        if result_data['status'] == 'done':
                            # Step 4: Retrieve the report
                            report_response = requests.get(f'https://plagiarismcheck.org/api/v1/checks/{check_id}/report-json', headers=headers)
                            if report_response.status_code == 200:
                                report_data = report_response.json()
                                plagiarism_percent = report_data.get('percent', None)
                                idea['plagiarism_percent'] = plagiarism_percent
                                break
                            else:
                                idea['plagiarism_percent'] = 'Error fetching report'
                                break
                        elif result_data['status'] == 'error':
                            idea['plagiarism_percent'] = 'Error in check'
                            break
                        else:
                            # Wait before polling again
                            time.sleep(5)
                    else:
                        idea['plagiarism_percent'] = 'Error checking status'
                        break
            else:
                idea['plagiarism_percent'] = 'Error starting check'
        else:
            idea['plagiarism_percent'] = 'Error creating document'
        
        plagiarism_results.append(idea)
    
    context = {
        'group': group,
        'plagiarism_results': plagiarism_results,
    }
    
    return render(request, 'myapp/plagiarism_results.html', context)

def add_idea_no_listz(request):
    items1 = Sy_idea_no.objects.select_related('sy_group_no').order_by('sy_group_no__Add_sy_group_no')

    grouped_items = []
    current_group = None

    for item in items1:
        if current_group != item.sy_group_no:
            current_group = item.sy_group_no
            grouped_items.append({
                'group': current_group,
                'students': [],
                'check_plagiarism': "#",  
                'finalize_idea_page': item.pk,
                'sy_idea_1': current_group.sy_idea_1,
                'sy_idea_1_des': current_group.sy_idea_1_des,
                'sy_idea_2': current_group.sy_idea_2,
                'sy_idea_2_des': current_group.sy_idea_2_des,
                'sy_idea_3': current_group.sy_idea_3,
                'sy_idea_3_des': current_group.sy_idea_3_des,
                'get_choices_guide': current_group.get_choices_guide
            })
        
        grouped_items[-1]['students'].append(item)

    return render(request, 'myapp/add_idea_no_list.html', {'grouped_items': grouped_items})



def delete_idea_no(request, pk):
    item = get_object_or_404(Sy_idea_no, pk=pk)
    item.delete()
    return redirect('add_idea_no_listz')  

def add_idea_no(request, pk=None):
 
        if request.method == "POST":
            form = Sy_add_idea_no_form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('add_idea_no_listz')
        else:
            form = Sy_add_idea_no_form()

        return render(request, 'myapp/add_idea_no.html', {'form': form})


def update_idea_no(request, pk=None):
    # Fetch the instance to update using the primary key (pk)
    idea_no_instance = get_object_or_404(Sy_add_idea_no, pk=pk)
    
    if request.method == "POST":
        # When form is submitted, populate it with POST data and the existing instance
        form = Sy_add_idea_no_form(request.POST, instance=idea_no_instance)
        if form.is_valid():
            # Save the updated data to the database
            form.save()
            # Redirect to a list view or another page after saving
            return redirect('add_idea_no_listz')
        else:
            print(form.errors)  # Debug form errors
            print(request.POST)  # Debug POST data
    else:  
        # On a GET request, pre-populate the form with the existing instance data
        form = Sy_add_idea_no_form(instance=idea_no_instance)
       
    # Render the form in the template
    return render(request, 'myapp/add_idea_no.html', {'form': form})



def add_name_roll(request):
    if request.method == "POST":
        form = Sy_SomeOtherForm(request.POST)
        if form.is_valid():
            # Get the Sy_add_idea_no instance from the form
            sy_group_instance = form.cleaned_data.get('sy_group_no')
            sy_group_no = sy_group_instance.Add_sy_group_no  # Extract the group number from the instance
            
            matching_groups = Sy_add_idea_no.objects.filter(Add_sy_group_no=sy_group_no)

            if matching_groups.count() == 1:
                # Proceed with saving if exactly one match
                form.save()
                return redirect('add_idea_no_listz')
            elif matching_groups.count() > 1:
                # Handle the case where multiple objects are returned
                form.add_error(None, "Multiple groups found for this group number.")
            else:
                # Handle the case where no objects are found
                form.add_error('sy_group_no', "No group found with this number.")
        else:
            print(form.errors)  # Print form errors to the console for debugging
    else:
        form = Sy_SomeOtherForm()
    
    return render(request, 'myapp/template.html', {'form': form})







def home(request):
    # Your home view logic here
    return render(request, 'myapp/home.html')

def tablepage(request):
 
    return render(request, 'myapp/tablepage.html')

# Temp idea code👆


def rating_view(request):
    if request.method == 'POST':
        forms = {
            'form1': RatingForm1(request.POST),
            'form2': RatingForm2(request.POST),
            'form3': RatingForm3(request.POST),
            'form4': RatingForm4(request.POST),
            'form5': RatingForm5(request.POST)
        }
        
        if all(form.is_valid() for form in forms.values()):
            scores = {name: sum(float(value) for value in form.cleaned_data.values()) for name, form in forms.items()}
            return render(request, 'myapp/result.html', scores)
    else:
        forms = {
            'form1': RatingForm1(),
            'form2': RatingForm2(),
            'form3': RatingForm3(),
            'form4': RatingForm4(),
            'form5': RatingForm5()
        }
    
    return render(request, 'myapp/rating.html', forms)


def evaluation_list(request):
    # Get all FinalMarksEvaluation instances with related student and group data
    evaluations = FinalMarksEvaluation.objects.select_related(
        'final_marks_student',  # Related to the student
        'final_marks_student__sy_group_no',  # Related to the group number via student
        'final_marks_evaluation__final_title',  # Access final_title through final_marks_evaluation
    ).all()

    context = {
        'evaluations': evaluations,
    }
    return render(request, 'myapp/evaluation_list.html', context)

  
def send_test_smtp_email(name, email):
    subject = 'Test SMTP Email'
    
    html_message = render_to_string(
        'myapp/email.html', {'name': name})
    plain_message = strip_tags(html_message)
    from_email = 'admin@demomailtrap.com'
    to_email = ['aayushshah11223344@gmail.com']
    
    email = EmailMultiAlternatives(subject = subject,body = plain_message, from_email = from_email, to =to_email )
    email.attach_alternative(html_message, "text/html")
    email.send()

def evaluation_list_form(request, pk=None):
    if pk:
        mymember = FinalMarksEvaluation.objects.get(pk=pk)
    else:
        mymember = None  # For creating a new instance if no primary key is provided
    
    if request.method == "POST":
        form = FinalMarksEvaluationForm(request.POST, instance=mymember)
        if form.is_valid():
            instance = form.save(commit=False)

            # Handle first practical
            if 'num01' in form.changed_data and instance.num01 == '0':

                instance.num1 = '0'
                instance.num2 = '0'
                instance.num21 = '0'
                instance.num31 = '0'
                instance.num32 = '0'
                instance.num33 = '0'
                instance.num34 = '0'
                instance.num41 = '0'
                instance.num51 = '0'
                instance.num52 = '0'
                instance.num53 = '0'
                instance.num54 = '0'
                instance.save()
          
                student_name = instance.final_marks_student.sy_name
                student_email = instance.final_marks_student.sy_email

                context = {
                    'name': student_name,
                    'email': student_email,
                
                }
               
                send_test_smtp_email(name=student_name, email=student_email)

                # Redirect or return an appropriate response after sending the email
                return render(request, 'myapp/email_send.html', context)
                    
            # Handle second practical
            if 'p2_num01' in form.changed_data and instance.p2_num01 == '0':
                instance.p2_num1 = '0'
                instance.p2_num2 = '0'
                instance.p2_num21 = '0'
                instance.p2_num31 = '0'
                instance.p2_num32 = '0'
                instance.p2_num33 = '0'
                instance.p2_num34 = '0'
                instance.p2_num41 = '0'
                instance.p2_num51 = '0'
                instance.p2_num52 = '0'
                instance.p2_num53 = '0'
                instance.p2_num54 = '0'
                instance.save()
                
                student_name = instance.final_marks_student.sy_name
                student_email = instance.final_marks_student.sy_email

                context = {
                    'name': student_name,
                    'email': student_email,
                
                }
               
                send_test_smtp_email(name=student_name, email=student_email)

                # Redirect or return an appropriate response after sending the email
                return render(request, 'myapp/email_send.html', context)
                    
            # Handle third practical
            if 'p3_num01' in form.changed_data and instance.p3_num01 == '0':
                instance.p3_num1 = '0'
                instance.p3_num2 = '0'
                instance.p3_num21 = '0'
                instance.p3_num31 = '0'
                instance.p3_num32 = '0'
                instance.p3_num33 = '0'
                instance.p3_num34 = '0'
                instance.p3_num41 = '0'
                instance.p3_num51 = '0'
                instance.p3_num52 = '0'
                instance.p3_num53 = '0'
                instance.p3_num54 = '0'
                instance.save()
            
                student_name = instance.final_marks_student.sy_name
                student_email = instance.final_marks_student.sy_email

                context = {
                    'name': student_name,
                    'email': student_email,
                
                }
               
                send_test_smtp_email(name=student_name, email=student_email)

                # Redirect or return an appropriate response after sending the email
                return render(request, 'myapp/email_send.html', context)
                      
            # Handle fourth practical
            if 'p4_num01' in form.changed_data and instance.p4_num01 == '0':
                instance.p4_num1 = '0'
                instance.p4_num2 = '0'
                instance.p4_num21 = '0'
                instance.p4_num31 = '0'
                instance.p4_num32 = '0'
                instance.p4_num33 = '0'
                instance.p4_num34 = '0'
                instance.p4_num41 = '0'
                instance.p4_num51 = '0'
                instance.p4_num52 = '0'
                instance.p4_num53 = '0'
                instance.p4_num54 = '0'
                instance.save()
               
                student_name = instance.final_marks_student.sy_name
                student_email = instance.final_marks_student.sy_email

                context = {
                    'name': student_name,
                    'email': student_email,
                
                }
               
                send_test_smtp_email(name=student_name, email=student_email)

                # Redirect or return an appropriate response after sending the email
                return render(request, 'myapp/email_send.html', context)
                    

            # Save the form without redirection if the student is present for the latest practical
            instance.save()
            return redirect('evaluation_list')
    else:
        form = FinalMarksEvaluationForm(instance=mymember)
    
    context = {
        'form': form,
        'mymember': mymember
    }
    
    return render(request, 'myapp/evaluation_edit.html', context)

def evaluation_edit(request, pk=None):
    evaluation = get_object_or_404(FinalMarksEvaluation, pk=pk)

    if request.method == "POST":
        form = FinalMarksEvaluationForm(request.POST, instance=evaluation)
        if form.is_valid():
            evaluation = form.save(commit=False)
            # Perform any additional logic if necessary
            evaluation.save()
            return redirect('evaluation_list')
        else:
            print(form.errors)  # Debug form errors
            print(request.POST)  # Debug POST data
    else:
        form = FinalMarksEvaluationForm(instance=evaluation)
        if hasattr(evaluation, 'sy_idea') and evaluation.sy_idea:
            form.fields['sy_idea_no'].initial = evaluation.sy_idea.sy_grp_no
    
    return render(request, 'myapp/evaluation_edit.html', {'form': form})

def delete_view(request, id):
    obj = get_object_or_404(FinalMarksEvaluation, id=id)
    obj.delete()
    return redirect('evaluation_list')
    


def update_view(request, id):
    evaluation = get_object_or_404(FinalMarksEvaluation, pk=id)

    if request.method == "POST":
        form = FinalMarksEvaluationForm(request.POST, instance=evaluation)
        if form.is_valid():
            evaluation = form.save(commit=False)
            # Perform any additional logic if necessary
            evaluation.save()
            return redirect('evaluation_list')
        else:
            print(form.errors)  # Debug form errors
            print(request.POST)  # Debug POST data
    else:
        form = FinalMarksEvaluationForm(instance=evaluation)
     
        if hasattr(evaluation, 'sy_idea') and evaluation.sy_idea:
            form.fields['sy_idea_no'].initial = evaluation.sy_idea.sy_grp_no

    return render(request, 'myapp/evaluation_edit.html', {'form': form})


def filter_evaluations(request):
    branch = request.GET.get('branch', '')
    year = request.GET.get('year', '')
    
    # Filter evaluations based on branch and year
    evaluations = GroupEvaluation.objects.all()
    if branch:
        evaluations = evaluations.filter(num01=branch)
    if year:
        evaluations = evaluations.filter(group_year=year)
    
     # Group evaluations by sy_idea_no and num01 (branch)
    grouped_evaluations = evaluations.values_list('sy_idea_no', 'num01').annotate(count=Count('id')).order_by('sy_idea_no', 'num01')
    grouped_evaluations = {key: evaluations.filter(sy_idea_no=key[0], num01=key[1]) for key in grouped_evaluations}

    # List of years
    years = [str(y) for y in range(2023, 2040) if y != 2033]

    return render(request, "myapp/evaluation_list.html", {
        'grouped_evaluations': grouped_evaluations,
        'years': years,
        'selected_branch': branch,
        'selected_year': year,
    })




# TY


def ty_evaluation_list(request):
    # Aggregate evaluations by group number and idea
    evaluations_ty = GroupEvaluation_ty.objects.select_related('ty_idea_no').all().order_by('ty_idea_no__ty_grp_no', 'ty_idea_no__ty_idea')
    grouped_evaluations_ty = {}
    
    for eval in evaluations_ty:
        key = (eval.ty_idea_no.ty_grp_no, eval.ty_idea_no.ty_idea)
        if key not in grouped_evaluations_ty:
            grouped_evaluations_ty[key] = []
        grouped_evaluations_ty[key].append(eval)
    
    context = {
        'grouped_evaluations_ty': grouped_evaluations_ty
    }
    return render(request, 'myapp_ty/ty_evaluation_list.html', context)












def ty_evaluation_edit(request, pk=None):
    if pk:
        evaluation_ty = get_object_or_404(GroupEvaluation_ty, pk=pk)
    else:
        evaluation_ty = GroupEvaluation_ty()

    if request.method == "POST":
        form = GroupEvaluation_tyForm(request.POST, instance=evaluation_ty)
        if form.is_valid():
            evaluation_ty = form.save(commit=False)
            # Perform any additional logic if necessary
            evaluation_ty.save()
            return redirect('ty_evaluation_list')
        else:
            print(form.errors)  # Debug form errors
    else:
        form = GroupEvaluation_tyForm(instance=evaluation_ty)
        # Example of setting initial value for a different field, if needed
        if hasattr(evaluation_ty, 'ty_idea') and evaluation_ty.ty_idea:
            form.fields['ty_idea_no'].initial = evaluation_ty.ty_idea.ty_grp_no
    
    return render(request, 'myapp_ty/ty_evaluation_edit.html', {'form': form})



def ty_delete_view(request, id):
    obj = get_object_or_404(GroupEvaluation_ty, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('ty_evaluation_list')
    return render(request, "myapp_ty/ty_delete_view.html", {'object': obj})




def ty_update_view(request, id):
    # Retrieve the existing instance of the model
    mymember = get_object_or_404(GroupEvaluation_ty, id=id)
    print(mymember)  # Check if this prints the expected data

    if request.method == "POST":
        # Bind the form to the POST data and the existing instance
        form = GroupEvaluation_tyForm(request.POST, instance=mymember)
        if form.is_valid():
            form.save()
            return redirect('ty_evaluation_list')
    else:
        # Bind the form to the existing instance for GET request
        form = GroupEvaluation_tyForm(instance=mymember)

    context = {
        'form': form,
        'mymember': mymember,
    }
    return render(request, "myapp_ty/ty_evaluation_edit.html", context)






def ty_filter_evaluations(request):
    branch = request.GET.get('branch', '')
    year = request.GET.get('year', '')

    # Filter evaluations based on branch and year
    evaluations_ty = GroupEvaluation_ty.objects.all()
    if branch:
        evaluations_ty = evaluations_ty.filter(num01=branch)
    if year:
        evaluations_ty = evaluations_ty.filter(group_year=year)

    # Group evaluations by ty_idea_no and num01 (branch)
    grouped_evaluations_ty = evaluations_ty.values_list('ty_idea_no__ty_grp_no', 'num01').annotate(count=Count('id')).order_by('ty_idea_no', 'num01')
    grouped_evaluations_ty = {key: evaluations_ty.filter(ty_idea_no__ty_grp_no=key[0], num01=key[1]) for key in grouped_evaluations_ty}

    # List of years
    years = [str(y) for y in range(2023, 2040) if y != 2033]

    return render(request, "myapp_ty/ty_evaluation_list.html", {
        'grouped_evaluations_ty': grouped_evaluations_ty,
        'years': years,
        'selected_branch': branch,
        'selected_year': year,
    })



def  ty_add_grp_no_grp_idea(request):
        if request.method == "POST":
         form = Ty_SomeOtherForm(request.POST)
         if form.is_valid():
            form.save()
            return redirect('ty_evaluation_list') 
        else:
            form = Ty_SomeOtherForm()
        
        return render(request, 'myapp_ty/ty_template.html', {'form': form})


# LY

def ly_evaluation_list(request):
    evaluations_ly = GroupEvaluation_ly.objects.all()
    context = {'evaluations': evaluations_ly}
    return render(request, 'myapp_ly/ly_evaluation_list.html', context)


def ly_evaluation_edit(request, pk=None):
    if pk:
        evaluation_ly = get_object_or_404(GroupEvaluation_ly, pk=pk)
    else:
        evaluation_ly = GroupEvaluation_ly()

    if request.method == "POST":
        form = GroupEvaluation_lyForm(request.POST, instance=evaluation_ly)
        if form.is_valid():
            evaluation_ly = form.save(commit=False)
            evaluation_ly.teamwork = evaluation_ly.calculate_teamwork()
            evaluation_ly.save()
            return redirect('ly_evaluation_list')
        else:
            print(form.errors)  # Debug form errors
    else:
        form = GroupEvaluation_tyForm(instance=evaluation_ly)
    
    return render(request, 'myapp_ly/ly_evaluation_edit.html', {'form': form})



def ly_delete_view(request, id):
    obj = get_object_or_404(GroupEvaluation_ly, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('ly_evaluation_list')
    return render(request, "myapp_ly/ly_delete_view.html", {'object': obj})

def ly_update_view(request, id):
    # Retrieve the existing instance of the model
    mymember = get_object_or_404(GroupEvaluation_ly, id=id)
    print(mymember)  # Check if this prints the expected data

    if request.method == "POST":
        # Bind the form to the POST data and the existing instance
        form = GroupEvaluation_lyForm(request.POST, instance=mymember)
        if form.is_valid():
            form.save()
            return redirect('ly_evaluation_list')
    else:
        # Bind the form to the existing instance for GET request
        form = GroupEvaluation_lyForm(instance=mymember)

    context = {
        'form': form,
        'mymember': mymember,
    }
    return render(request, "myapp_ly/ly_evaluation_edit.html", context)


def ly_filter_by_branch_and_year(request):
    branch = request.GET.get('branch')
    year = request.GET.get('year')
    
    filters = {}
    if branch:
        filters['num01'] = branch
    if year:
        filters['group_year'] = year
    
    evaluations_ly = GroupEvaluation_ly.objects.filter(**filters)
    
    return render(request, 'myapp_ly/ly_evaluation_list.html', {'evaluations': evaluations_ly})

