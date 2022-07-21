from base64 import encode
import os
import datetime
from inspect import signature
from turtle import ht, pd
from xmlrpc.client import Boolean
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from weasyprint import HTML

from web_app.models import *
from web_app.serializers import *
from rest_framework import generics
from django.shortcuts import render, redirect

from django.core.mail import send_mail

#Pdf maker# importing the necessary libraries
from django.http import HttpResponse
from django.template.loader import get_template
# from xhtml2pdf import pisa  
from django.conf import settings



def is_float(value):
    try:
        float(value)
        return True
    except:
        return False


class SelectedStudentInfoView(generics.RetrieveAPIView):
    lookup_field = "fnum"
    serializer_class = StudentsSerializer
    queryset = Students.objects.all()
    permission_classes = [IsAuthenticated]


class AllStudentsInfoView(generics.ListAPIView):
    serializer_class = StudentsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        course = self.request.GET.get('course')
        year = self.request.GET.get('year')
        semester = self.request.GET.get('semester')
        all_enrollments = Enrollments.objects.all()
        if course:
            all_enrollments = all_enrollments.filter(signature_id=course)
        if year:
            all_enrollments = all_enrollments.filter(tyear=year)
        if semester:
            all_enrollments = all_enrollments.filter(semester=semester)
        queryset = Students.objects.filter(enrollments__in=all_enrollments)
        return queryset


class AchievementsView(generics.ListAPIView):
    serializer_class = AchievementsSerializer
    queryset = Achievements.objects.all()
    permission_classes = [IsAuthenticated]


RESPONSE_404 = JsonResponse({
    'status_code': 404,
    'error': 'The resource was not found'
}, status=404)


@login_required
def index(request):
    if not request.user.is_authenticated:
        return RESPONSE_404
    """View function for home page of site."""
    students = Students.objects.all()
    context = {
        'students': students,
        'weeks_range': range(1, 16),
        'courses': Courses.objects.all()
    }
    return render(request, 'index.html', context=context)


@login_required
def handle_attend(request):
    if request.method == 'POST':
        fnum = request.POST.get('fnum')
        week = request.POST.get('week')
        course = request.POST.get('course')
        year = request.POST.get('year')
        semester = request.POST.get('semester')
        if fnum and week and is_float(week) and 1 <= int(week) <= 15:
            week = int(week)
            enrollment = Enrollments.objects.filter(fnum=fnum, signature_id=course, tyear=year,
                                                    semester=semester)
            if enrollment:
                prev_val = enrollment.first().__getattribute__("attendance" + str(week))
                kwargs = {"attendance" + str(week): not prev_val}
                enrollment.update(**kwargs)
            else:
                kwargs = {"attendance" + str(week): True}
                enrollment.create(fnum_id=fnum, signature_id=course, tyear=year,
                                  semester=semester, **kwargs)
            enrollment.first().save()
            return JsonResponse({'status_code': 200, 'fnum': fnum})
        return JsonResponse({'status': 'error', 'error': 'Please provide valid fnum and week.'}, status=400)
    return RESPONSE_404


@login_required
def add_grade(request):
    if request.method == 'POST':
        fnum = request.POST.get('fnum')
        grade_name = request.POST.get('gradeName')
        grade_val = request.POST.get('gradeEvaluation')
        course = request.POST.get('course')
        if grade_name and grade_val and fnum and is_float(grade_val):
            new_grade = Actions.objects.update_or_create(fnum_id=fnum, name=grade_name,
                                               evaluation=float(grade_val), signature_id=course)
            new_grade.save()
        return JsonResponse({'status_code': 200, 'fnum': fnum})
    return RESPONSE_404


@login_required
def add_achievement(request):
    if request.method == 'POST':
        fnum = request.POST.get('fnum')
        achiev = request.POST.get('achievement')
        course = request.POST.get('course')
        if achiev and fnum:
            new_achieved, _ = Achieved.objects.update_or_create(fnum_id=fnum, achievement_id=achiev,
                                                                signature_id=course,
                                                                achieve_date=datetime.datetime.now())
            new_achieved.save()
            student_temp = Students.objects.get(fnum = fnum)
            achievement_temp = new_achieved.achievement
            '''
            send_mail(
                 achievement_temp.name, #Subject
                'Hello ' + student_temp.name + ' congratulations on getting the achivement, keep the good work!\n Your Profesor', #Msg
                "gmail that will be used to send those", #from email FILL IN YOUR MAIL HERE
                student_temp.email, #to email
                fail_silently=False,
            )
            '''
            #uncomment this and go to settings.py
            
        return JsonResponse({'status_code': 200, 'fnum': fnum})
    return RESPONSE_404





'''
def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    sUrl = settings.STATIC_URL        # Typically /static/
    sRoot = os.getcwd()
    sRoot = os.path.join(sRoot, "web_app/static/")
    if uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri
    return path
'''


@login_required
def pdf_maker(request):
    if request.method == 'GET':
        course = request.GET.get('course')
        year = request.GET.get('year')
        semester = request.GET.get('semester')

        if not course or not year or not semester:
            return RESPONSE_404

        view_func = AllStudentsInfoView.as_view()
        students = view_func(request=request).data
        context = {
            'students': students,
            'course': course,
        }


        html_template = get_template('pdf_achievements.html')        
        rendered_html = html_template.render(context).encode(encoding="UTF-8")

        
        # response = HttpResponse(content_type='application/pdf')
        # pisa_status = pisa.CreatePDF(rendered_html, dest=response, link_callback=link_callback)
        # return response

        pdf = HTML(string=rendered_html, base_url=request.build_absolute_uri()).write_pdf()

        return  HttpResponse(pdf, content_type='application/pdf')
    return RESPONSE_404
