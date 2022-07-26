"""AchV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import web_app.views as views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('', views.index, name='index'),
    path('attend', views.handle_attend, name='attend'),
    path('grade', views.add_grade, name='grade'),
    path('add_achievement', views.add_achievement, name='add_achievement'),
    path('admin/', admin.site.urls),
    path('api/achievements/', views.AchievementsView.as_view(), name='achievements'),
    path('api/student/<fnum>', views.SelectedStudentInfoView.as_view(), name='student'),
    path('api/students', views.AllStudentsInfoView.as_view(), name='students'),
    path('pdf',views.pdf_maker, name='pdf_maker')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
