"""
File that is used to process all the view request
"""

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from VivaManagementSystem.models import Tutor
from VivaManagementSystem.models import Faculty
from AJAXHandlers import AJAXHandlerFactory
from util import SessionHandler
from util import spreadsheet_module
import socket


def is_connected():
    try:
        # see if we can resolve the host name -- tells us if there is
        # a DNS listening
        host = socket.gethostbyname("www.google.com")
        # connect to the host -- tells us if the host is actually
        # reachable
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

def login(request):
    SessionHandler.set_session_obj(request.session)
    if SessionHandler.is_user_logged_in():
        return redirect("/index/")
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
    if len(tutors) == 0:
        course_name = "ADMIN VIEW"
    else:
        course_name = tutors[0].course.course_name

    context = {
        'username': user_name,
        'userrole' : user_role,
        'pagename': 'VMS-Index',
        'course_name': course_name,
        'js_files': [
            '/static/newVMS/js/charts/raphaeljs.min.js',
            '/static/newVMS/js/charts/morris.min.js',
            '/static/newVMS/js/index/chartDrawing.js'
        ],
        'css_files' : [
            '/static/newVMS/styles/index/custom.css',
            '/static/newVMS/styles/index/morris.css'
        ]
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
    if len(tutors) == 0:
        course_name = "ADMIN VIEW"
    else:
        course_name = tutors[0].course.course_name

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
    if is_connected():
        spreadsheet_module.update_student_records()
    template = loader.get_template('newVMS/page_guide_allot.html')
    user_id = SessionHandler.get_user_id()
    user_name = Faculty.objects.get(employee_id=user_id).name
    user_role = SessionHandler.get_user_role()
    tutors = Tutor.objects.select_related('faculty').filter(faculty=user_id)
    if len(tutors) == 0:
        course_name = "ADMIN VIEW"
        course_id = "-1"
    else:
        course_name = tutors[0].course.course_name
        course_id = SessionHandler.get_user_course_id()
    context = {
        'userid'  :user_id,
        'username': user_name,
        'userrole': user_role,
        'pagename': 'VMS-GuideAllot',
        'course_name':course_name,
        'course_id':course_id,
        'css_files': [
            "/static/newVMS/styles/guide-allot.css"
        ],
        'js_files': [
            '/static/newVMS/js/guide_allot.js'
        ]
    }
    return HttpResponse(template.render(context, request))


def guide_select(request):
    if is_connected():
        spreadsheet_module.update_faculty_records()
    SessionHandler.set_session_obj(request.session)
    if not SessionHandler.is_user_logged_in():
        return redirect('/login/')
    template = loader.get_template('newVMS/page_guide_allot.html')
    user_id = SessionHandler.get_user_id()
    print(user_id)
    user_name = Faculty.objects.get(employee_id=user_id).name
    user_role = SessionHandler.get_user_role()
    tutors = Tutor.objects.select_related('faculty').filter(faculty=user_id)
    if len(tutors) == 0:
        course_name = "ADMIN VIEW"
    else:
        course_name = tutors[0].course.course_name

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
    if len(tutors) == 0:
        course_name = "ADMIN VIEW"
    else:
        course_name = tutors[0].course.course_name

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


def about(request):
    SessionHandler.set_session_obj(request.session)
    if not SessionHandler.is_user_logged_in():
        return redirect('/login/')
    template = loader.get_template('newVMS/about.html')
    user_id = SessionHandler.get_user_id()
    user_name = Faculty.objects.get(employee_id=user_id).name
    user_role = SessionHandler.get_user_role()
    tutors = Tutor.objects.select_related('faculty').filter(faculty=user_id)
    if len(tutors) == 0:
        course_name = "ADMIN VIEW"
    else:
        course_name = tutors[0].course.course_name

    context = {
        'username': user_name,
        'userrole': user_role,
        'pagename': 'VMS-Config',
        'course_name': course_name,
        'css_files': [
        ],
        'js_files': [
        ]
    }
    return HttpResponse(template.render(context, request))

def chatBot(request):
    template = loader.get_template('newVMS/vBot.html')
    context = {}
    return HttpResponse(template.render(context, request))


