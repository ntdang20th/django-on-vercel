from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django.views.decorators.csrf import csrf_exempt
import json

connection = mail.get_connection()
@csrf_exempt
@api_view(['POST'])
def ResponesData(request):
    connection.open()
    print("connected!")
    json_string = json.dumps(request.data)
    send_mail(
        'Reply mess!!',
        json_string,
        settings.EMAIL_HOST_USER,
        ['ntdang_20th@student.agu.edu.vn', 'eliane.schroeter@gmail.com'],
        connection=connection,
    )
    connection.close()
    return Response(request.data)
def index(request):
    return render(request, 'index.html', context={
        "title": "Hello world!",
    })
