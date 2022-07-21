from rest_framework import serializers
from web_app.models import *


class StudentsSerializer(serializers.ModelSerializer):
    attendance = serializers.SerializerMethodField()
    achieved = serializers.SerializerMethodField()
    avg_grade = serializers.SerializerMethodField()

    class Meta:
        model = Students
        fields = ['fnum', 'name', 'email', 'year', 'attendance', 'achieved', 'avg_grade']

    def get_attendance(self, obj):
        request = self.context.get("request").GET

        course = request.get("course")
        year = request.get("year")
        semester = request.get("semester")

        curr_enrollment = Enrollments.objects.filter(fnum=obj.fnum, signature_id=course,
                                                     tyear=year, semester=semester)
        if curr_enrollment:
            return curr_enrollment.first().total_attendance
        else:
            return 0

    def get_achieved(self, obj):
        curr_achieved = AchievedSerializer(Achieved.objects.filter(fnum=obj.fnum), many=True)
        return curr_achieved.data

    def get_avg_grade(self, obj):
        request = self.context.get("request").GET
        course = request.get("course")
        all_actions = Actions.objects.filter(fnum=obj, signature_id=course, evaluation__isnull=False)
        if not all_actions:
            return -1
        return all_actions.aggregate(models.Avg('evaluation'))['evaluation__avg']


class AchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = '__all__'


class AchievedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achieved
        fields = ['achieve_date', 'achievement']
