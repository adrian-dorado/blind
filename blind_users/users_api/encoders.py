from common.json import ModelEncoder
from .models import *

class UserEncoder(ModelEncoder):
    model = User
    properties = [
        "username",
        "email",
        "first_name",
        "last_name",
        "password",
        "phone_number",
    ]
