from django.urls import path
from .views import registrar_asistencia, ver_asistencia , descargar_asistencias_pdf
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('registrar/', registrar_asistencia, name='registrar_asistencia'),
    path('ver/', ver_asistencia, name='ver_asistencia'),
    path('login/', LoginView.as_view(template_name='asistencia/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
        path('descargar_pdf/', descargar_asistencias_pdf, name='descargar_pdf'),

]
