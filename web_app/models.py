from django.db import models


class Students(models.Model):
    fnum = models.CharField(max_length=7, primary_key=True)
    name = models.CharField(max_length=60)
    email = models.EmailField()
    year = models.IntegerField()


class QRCodes(models.Model):
    id = models.BigAutoField(primary_key=True)
    fnum = models.ForeignKey('Students', on_delete=models.CASCADE, related_name="qrcodes")
    code = models.CharField(max_length=7)
    week = models.IntegerField()
    signature = models.CharField(max_length=16)
    sent = models.BooleanField(null=True)


class Courses(models.Model):
    signature = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=60)


class Enrollments(models.Model):
    fnum = models.ForeignKey('Students', on_delete=models.CASCADE, related_name="enrollments")
    signature = models.ForeignKey('Courses', on_delete=models.CASCADE, related_name="enrollments")
    tyear = models.IntegerField()
    semester = models.CharField(max_length=10)
    test_1_grade = models.FloatField(null=True)
    test_2_grade = models.FloatField(null=True)
    test_3_grade = models.FloatField(null=True)
    final_exam_grade = models.FloatField(null=True)
    project_grade = models.FloatField(null=True)
    attendance1 = models.BooleanField(null=True)
    attendance2 = models.BooleanField(null=True)
    attendance3 = models.BooleanField(null=True)
    attendance4 = models.BooleanField(null=True)
    attendance5 = models.BooleanField(null=True)
    attendance6 = models.BooleanField(null=True)
    attendance7 = models.BooleanField(null=True)
    attendance8 = models.BooleanField(null=True)
    attendance9 = models.BooleanField(null=True)
    attendance10 = models.BooleanField(null=True)
    attendance11 = models.BooleanField(null=True)
    attendance12 = models.BooleanField(null=True)
    attendance13 = models.BooleanField(null=True)
    attendance14 = models.BooleanField(null=True)
    attendance15 = models.BooleanField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['fnum', 'signature', 'tyear', 'semester'], name="id_enrollments"
            )
        ]

    @property
    def total_attendance(self):
        temp = (1 if self.attendance1 else 0) + (1 if self.attendance2 else 0) + \
               (1 if self.attendance3 else 0) + (1 if self.attendance4 else 0) + \
               (1 if self.attendance5 else 0) + (1 if self.attendance6 else 0) + \
               (1 if self.attendance7 else 0) + (1 if self.attendance8 else 0) + \
               (1 if self.attendance9 else 0) + (1 if self.attendance10 else 0) + \
               (1 if self.attendance11 else 0) + (1 if self.attendance12 else 0) + \
               (1 if self.attendance13 else 0) + (1 if self.attendance14 else 0) + \
               (1 if self.attendance15 else 0)
        return temp


class Actions(models.Model):
    fnum = models.ForeignKey('Students', on_delete=models.CASCADE, related_name="actions")
    name = models.CharField(max_length=20)
    signature = models.ForeignKey('Courses', on_delete=models.CASCADE, related_name="actions")
    evaluation = models.FloatField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['fnum', 'name', 'signature'], name="id_actions"
            )
        ]


class Achievements(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    name = models.TextField()
    description = models.TextField(null=True)


class Achieved(models.Model):
    fnum = models.ForeignKey('Students', on_delete=models.CASCADE, related_name="achieved")
    signature = models.ForeignKey('Courses', on_delete=models.CASCADE, related_name="achieved")
    achievement = models.ForeignKey('Achievements', on_delete=models.CASCADE, related_name="achieved")
    achieve_date = models.DateField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['fnum', 'signature', 'achievement'], name="id_achieved"
            )
        ]
