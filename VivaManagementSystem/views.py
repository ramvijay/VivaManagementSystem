"""
File that is used to process all the view request
"""
from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from VivaManagementSystem.models import Tutor, User
from VivaManagementSystem.models import Faculty
from AJAXHandlers import AJAXHandlerFactory
from util import GenericUtil
from util import SessionHandler
from util import spreadsheet_module
from util.types import UserRoles
import json

def login(request):
    """
    Page for logging into the system. Contains a screen to enter username and password.
    """
    SessionHandler.set_session_obj(request.session)
    if SessionHandler.is_user_logged_in():
        return redirect("/index/")
    template = loader.get_template('newVMS/page_login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def logout(request):
    """
    Page for logging out and destroying the current session.
    """
    SessionHandler.set_session_obj(request.session)
    SessionHandler.logout_user()
    return redirect("/login/")

def index(request):
    """
    Index page that displays a dashboard containing all the meta information about the students.
    Page various according to the type of the user logged into the system.
    Loads different pages for different people.
    1. Dashboard for Guide -> Only shows alloted students details.
    2. Dashboard for Admin / Viva Coord / Tutor -> Shows graphs and tables.
        i. Tutor -> Only gets the details of the class for which the faculty is a tutor for.
    TODO Method is too big. Splitup everything.
    """
    SessionHandler.set_session_obj(request.session)
    if not SessionHandler.is_user_logged_in(): # Check login status
        return redirect('/login/')
    current_user_id = SessionHandler.get_user_id()
    current_user = User.objects.get(user_id=current_user_id) # For user_role.
    last_logged_in = current_user.logged_in_time
    if GenericUtil.is_connected(): # TODO FIXME Move this to a AJAX Request. This severly hogs up data.
        spreadsheet_module.update_database(last_logged_in)
        current_user.logged_in_time = datetime.now()
        current_user.save()
    user_name = Faculty.objects.get(employee_id=current_user_id).name # For the name
    # Check if the Faculty is a Tutor for anything
    tutors = Tutor.objects.select_related('faculty').filter(faculty=current_user_id)
    if len(tutors) > 0:
        course_name = tutors[0].course.course_name
    else: # Could be an admin or just a Guide
        if current_user.user_role == UserRoles.Admin.value:
            course_name = 'Admin View'
        elif current_user.user_role == UserRoles.Guide.value:
            course_name = 'Guide View'
        else:
            course_name = 'Guest View'
    # Change the view according to the logged in user type
    context = {
        'username': user_name,
        'userrole' : current_user.user_role,
        'pagename': 'VMS-Index',
        'course_name': course_name
    }
    if current_user.user_role != 'Guide':
        template = loader.get_template('newVMS/page_index.html')
        context['js_files'] = [
            '/static/newVMS/js/third-party/charts/raphaeljs.min.js',
            '/static/newVMS/js/third-party/charts/morris.min.js',
            '/static/newVMS/js/third-party/charts/chartjs.min.js',
            '/static/newVMS/js/third-party/materialize.min.js',
            '/static/newVMS/js/index/chartDrawing.js'
        ]
        context['css_files'] = [
            '/static/newVMS/styles/third-party/morris.css',
            '/static/newVMS/styles/third-party/materialize.min.css',
            '/static/newVMS/styles/index/custom.css'
        ]
    else: # This is for guide. Show alloted students details.
        template = loader.get_template('newVMS/page_index_guide.html')
        context['js_files'] = [
            '/static/newVMS/js/third-party/materialize.min.js',
            '/static/newVMS/js/index/index-for-guide.js'
        ]
        context['css_files'] = [
            '/static/newVMS/styles/third-party/materialize.min.css',
            '/static/newVMS/styles/index/custom.css'
        ]
    return HttpResponse(template.render(context, request))

def config(request):
    """
    Configuration page that is used to set critical settings for the System.
    Only certain Roles are allowed to acccess this page. They are,
    1. Administrator
    2. Viva Coordinator
    """
    SessionHandler.set_session_obj(request.session)
    if not SessionHandler.is_user_logged_in():
        return redirect('/login/')
    template = loader.get_template('newVMS/page_config.html')
    user_id = SessionHandler.get_user_id()
    user_name = Faculty.objects.get(employee_id=user_id).name
    user_role = SessionHandler.get_user_role()
    tutors = Tutor.objects.select_related('faculty').filter(faculty=user_id)
    if len(tutors) == 0:
        course_name = "ADMIN VIEW"
    else:
        course_name = tutors[0].course.course_name
    # Set the email to use when setting a new Form Response Sheet
    SECRETS_FILE = 'data/VivaManagementSystem-f7cde54a5c9e.json'
    file_data = json.load(open(SECRETS_FILE))
    context = {
        'username': user_name,
        'userrole' : user_role,
        'pagename': 'VMS-Config',
        'course_name': course_name,
        'google_sheets_perm_user_email': file_data['client_email'],
        'js_files': [
            '/static/newVMS/js/third-party/materialize.min.js',
            '/static/newVMS/js/config/main.js'
        ],
        'css_files': [
            '/static/newVMS/styles/third-party/materialize.min.css',
            '/static/newVMS/styles/config/main.css'
        ]
    }
    return HttpResponse(template.render(context, request))

def guide_allot(request):
    """
    Page for handling all Guide Allotments to the various Students of the system.
    """
    SessionHandler.set_session_obj(request.session)
    if not SessionHandler.is_user_logged_in():
        return redirect('/login/')
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
    """
    Page for selecting the various faculty to be Guides during the current session.
    """
    SessionHandler.set_session_obj(request.session)
    if not SessionHandler.is_user_logged_in():
        return redirect('/login/')
    user_id = SessionHandler.get_user_id()
    user_name = Faculty.objects.get(employee_id=user_id).name
    user_role = SessionHandler.get_user_role()
    tutors = Tutor.objects.select_related('faculty').filter(faculty=user_id)
    if len(tutors) == 0:
        course_name = "ADMIN VIEW"
    else:
        course_name = tutors[0].course.course_name

    query_results = Faculty.objects.all()
    template = loader.get_template('newVMS/page_guide_select.html')
    context = {
        'query_results': query_results,
        'username': user_name,
        'userrole': user_role,
        'pagename': 'VMS-Config',
        'course_name': course_name,
        'css_files':[
            "/static/newVMS/styles/guide-select/guide-select.css"
        ],
        'js_files':[
            "/static/newVMS/js/guide-select/guide-select-vue.js"
        ]
    }
    return HttpResponse(template.render(context, request))

def ajax(request, ajax_call):
    """
    Page to handle all AJAX calls throughout the system.
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
    template = loader.get_template('newVMS/page_student_list.html')
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
        'username': user_name,
        'userrole': user_role,
        'pagename': 'VMS-Config',
        'course_name': course_name,
        'course_id': course_id,
        'css_files': [
            "/static/newVMS/styles/student-list/student-list.css"
        ],
        'js_files': [
            "/static/newVMS/js/student-list/student-list.js"
        ]
    }
    return HttpResponse(template.render(context, request))

def about(request):
    """
    About page that displays the credits for the application.
    """
    SessionHandler.set_session_obj(request.session)
    if not SessionHandler.is_user_logged_in():
        return redirect('/login/')
    template = loader.get_template('newVMS/page_about.html')
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
