"""
File that is used to process all the view request
"""

from django.http import HttpResponse,JsonResponse
from django.template import loader
<<<<<<< HEAD
from .models import Faculty
=======
from django.shortcuts import redirect
from VivaManagementSystem.models import Student, Tutor
from VivaManagementSystem.models import Faculty
from AJAXHandlers import AJAXHandlerFactory
from util import SessionHandler
from util import spreadsheet_module


>>>>>>> e67038f93270b05c15c8a2b4d95959c17e85ff33

def guide_allotment(request):
    query_results = Faculty.objects.all()
    template = loader.get_template('newVMS/guide-allot.html')
    context = {'query_results': query_results}
    return HttpResponse(template.render(context, request))

def login(request):
    SessionHandler.set_session_obj(request.session)
    if SessionHandler.is_user_logged_in():
        return redirect("/ind   ex/")
    template = loader.get_template('newVMS/page-login.html')
    context = {}
    return HttpResponse(template.render(context, request))


def logout(request):
    SessionHandler.set_session_obj(request.session)
    SessionHandler.logout_user()
    return redirect("/login/")


def index(request):
    SessionHandler.set_session_obj(request.session)
    if not SessionHandler.is_user_logged_in():
        return redirect('/login/')
    template = loader.get_template('newVMS/page_index.html')
    user_id = SessionHandler.get_user_id()
    user_name = Faculty.objects.get(employee_id=user_id).name
    user_role = SessionHandler.get_user_role()
    tutors = Tutor.objects.select_related('faculty').filter(faculty=user_id)
    course_name = tutors[0].course.course_name;

    context = {
        'username': user_name,
        'userrole' : user_role,
        'pagename': 'VMS-Index',
        'course_name': course_name,
        'js_files': []
    }
    return HttpResponse(template.render(context, request))


def config(request):
    SessionHandler.set_session_obj(request.session)
    if not SessionHandler.is_user_logged_in():
        return redirect('/login/')
    template = loader.get_template('newVMS/page-config.html')
    user_id = SessionHandler.get_user_id()
    user_name = Faculty.objects.get(employee_id=user_id).name
    user_role = SessionHandler.get_user_role()
    tutors = Tutor.objects.select_related('faculty').filter(faculty=user_id)
    course_name = tutors[0].course.course_name;

    context = {
        'username': user_name,
        'userrole' : user_role,
        'pagename': 'VMS-Config',
        'course_name': course_name,
        'js_files': [
            '/static/newVMS/js/config/main.js',
            '/static/newVMS/js/accordion/jquery.accordionjs.js'
        ],
        'css_files': [
            '/static/newVMS/styles/config/main.css',
            '/static/newVMS/styles/accordion/jquery.accordionjs.css'
        ]
    }
    return HttpResponse(template.render(context, request))


def guide_allot(request):
    SessionHandler.set_session_obj(request.session)
    if not SessionHandler.is_user_logged_in():
        return redirect('/login/')
    template = loader.get_template('newVMS/page_guide_allot.html')
    user_id = SessionHandler.get_user_id()
    user_name = Faculty.objects.get(employee_id=user_id).name
    user_role = SessionHandler.get_user_role()
    tutors = Tutor.objects.select_related('faculty').filter(faculty=user_id)
    course_name = tutors[0].course.course_name;

    context = {
        'userid'  :user_id,
        'username': user_name,
        'userrole': user_role,
        'pagename': 'VMS-GuideAllot',
        'course_name':course_name,
        'css_files': [
            "/static/newVMS/styles/guide-allot.css"
        ],
        'js_files': [
            '/static/newVMS/js/guide_allot.js'
        ]
    }
    return HttpResponse(template.render(context, request))


def guide_select(request):

    spreadsheet_module.update_faculty_records()

    SessionHandler.set_session_obj(request.session)
    if not SessionHandler.is_user_logged_in():
        return redirect('/login/')
    template = loader.get_template('newVMS/page_guide_allot.html')
    user_id = SessionHandler.get_user_id()
    user_name = Faculty.objects.get(employee_id=user_id).name
    user_role = SessionHandler.get_user_role()
    tutors = Tutor.objects.select_related('faculty').filter(faculty=user_id)
    course_name = tutors[0].course.course_name;

    query_results = Faculty.objects.all()
    template = loader.get_template('newVMS/guide-select.html')
    context = {
        'query_results': query_results,
        'username': user_name,
        'userrole': user_role,
        'pagename': 'VMS-Config',
        'course_name': course_name,
        'css_files':[
            "/static/newVMS/styles/guide-select/guide-select.css",
            "/static/newVMS/js/libs/jquery.tablesorter/themes/blue/style.css",
            "/static/newVMS/js/libs/jquery.tablesorter/addons/pager/jquery.tablesorter.pager.css"
        ],
        'js_files':[
            "/static/newVMS/js/guide-select/guide-select.js"
        ]
    }
    return HttpResponse(template.render(context, request))



def ajax(request, ajax_call):
    """
    Method to handle all AJAX calls throughout the system.
    :param request:
    :param ajax_call: Used for routing the AJAX calls.
    :return: HTTPResponse containing the result
    """
    SessionHandler.set_session_obj(request.session)
    handler = AJAXHandlerFactory.create_instance(ajax_call)
    processed_data = handler.handle_request(request)
    return HttpResponse(processed_data)


def student_list(request):
    SessionHandler.set_session_obj(request.session)
    if not SessionHandler.is_user_logged_in():
        return redirect('/login/')
    template = loader.get_template('newVMS/student_list.html')
    user_id = SessionHandler.get_user_id()
    user_name = Faculty.objects.get(employee_id=user_id).name
    user_role = SessionHandler.get_user_role()
    tutors = Tutor.objects.select_related('faculty').filter(faculty=user_id)
    course_name = tutors[0].course.course_name;

    context = {
        'username': user_name,
        'userrole': user_role,
        'pagename': 'VMS-Config',
        'course_name': course_name,
        'css_files': [
            "/static/newVMS/styles/student-list/student-list.css"
        ],
        'js_files': [
            "/static/newVMS/js/student-list/student-list.js"
        ]
    }
    return HttpResponse(template.render(context, request))
