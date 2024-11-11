# main/context_processors.py
from django.utils.timezone import now

def base_context_processor(request):
    return {'timestamp': now().timestamp()}
