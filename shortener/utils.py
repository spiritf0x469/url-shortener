import random
import string
from .models import Shorturl
def generate_short_code(length=6):
    while True:
        code=''.join(random.choices(string.ascii_letters+string.digits,k=length))
        if not Shorturl.objects.filter(short_code=code).exists():
            return code