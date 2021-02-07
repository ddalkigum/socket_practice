import os
import django
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socket_practice.settings')

django.setup()

application = get_asgi_application()