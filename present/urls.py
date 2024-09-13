from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home-page'),
    path('tablepage/', views.tablepage, name='tablepage'),
    
    path('delete_view/<id>/', views.delete_view, name='delete_view'),
    path('update_view/<id>', views.update_view, name='update_view'),
    path('evaluation_list', views.evaluation_list, name='evaluation_list'),
    path('edit/<int:pk>/', views.evaluation_edit, name='evaluation_edit'),
    path('new/', views.evaluation_edit, name='evaluation_new'),
    path('rate/', views.rating_view, name='rating_view'),
    path('filter/', views.filter_evaluations, name='filter_evaluations'),


    path('add_name_roll/', views.add_name_roll, name='add_name_roll'),
    path('add_idea_no_listz', views.add_idea_no_listz, name='add_idea_no_listz'),
   
    path('add_idea_no/', views.add_idea_no, name='add_idea_no'), #grpup,idea 1 idea 2 idea 3
    path('update_idea_no/<int:pk>/', views.update_idea_no, name='update_idea_no'),
    path('delete_idea_no/<int:pk>/', views.delete_idea_no, name='delete_idea_no'),
    path('send_test_smtp_email/', views.send_test_smtp_email, name='send_test_smtp_email'),
    
    
    #  path('delete/<int:group_id>/', views.delete_idea_student, name='delete_idea_student'),
    path('check_plagiarism/<int:group_id>/', views.check_plagiarism, name='check_plagiarism'),
    path('finalize_idea_page/<int:group_id>/', views.finalize_idea_page, name='finalize_idea_page'),
    path('evaluation_list_form/', views.evaluation_list_form, name='evaluation_list_form'),


    # ty
    path('ty_list/', views.ty_evaluation_list, name='ty_evaluation_list'),
    path('ty_new/', views.ty_evaluation_edit, name='ty_evaluation_new'),
    path('ty_delete_view/<id>/', views.ty_delete_view, name='ty_delete_view'),
    path('ty_update_view/<id>', views.ty_update_view, name='ty_update_view'),
    path('ty_filter_by_branch_and_year/', views.ty_filter_evaluations, name='ty_filter_evaluations'),
    path('ty_add_grp_no_grp_idea/', views.ty_add_grp_no_grp_idea, name='ty_add_grp_no_grp_idea'),

    # ty
    path('ly_list/', views.ly_evaluation_list, name='ly_evaluation_list'),
    path('ly_new/', views.ly_evaluation_edit, name='ly_evaluation_new'),
    path('ly_delete_view/<id>/', views.ly_delete_view, name='ly_delete_view'),
    path('ly_update_view/<id>', views.ly_update_view, name='ly_update_view'),
    path('ly_filter_by_branch_and_year/', views.ly_filter_by_branch_and_year, name='ly_filter_by_branch_and_year'),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
