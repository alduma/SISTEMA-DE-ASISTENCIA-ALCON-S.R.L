from django.shortcuts import render, redirect
from .forms import AsistenciaForm
from .models import Asistencia
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

@login_required(login_url='login')
def registrar_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            asistencia = form.save(commit=False)
            asistencia.usuario = form.cleaned_data['usuario']  
            asistencia.fecha = now().date()  
            asistencia.save()
            return redirect('ver_asistencia')
    else:
        form = AsistenciaForm()
    
    return render(request, 'asistencia/registrar_asistencia.html', {'form': form})
# Vista para mostrar las asistencias del usuario
@login_required
def ver_asistencia(request):
    asistencias = Asistencia.objects.all()  
    return render(request, 'asistencia/ver_asistencia.html', {'asistencias': asistencias})

def descargar_asistencias_pdf(request):
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="asistencias.pdf"'

    
    c = canvas.Canvas(response, pagesize=letter)
    c.setFont("Helvetica", 12)

  
    c.drawString(220, 750, "Historial de Asistencias")

    c.drawString(50, 700, "Fecha")
    c.drawString(150, 700, "Usuario")
    c.drawString(300, 700, "Hora Entrada")
    c.drawString(450, 700, "Hora Salida")

    asistencias = Asistencia.objects.all()

    y = 680

   
    for asistencia in asistencias:
        c.drawString(50, y, str(asistencia.fecha))
        c.drawString(150, y, asistencia.usuario.username)
        c.drawString(300, y, str(asistencia.hora_entrada))
        c.drawString(450, y, str(asistencia.hora_salida))
        y -= 20 

        if y < 50:  
            c.showPage()
            y = 750  

    
    c.showPage()
    c.save()

    return response