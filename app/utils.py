import os
from django.utils import timezone
from django.core.exceptions import ValidationError


def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', 'jpeg', '.png']
    if not ext.lower() in valid_extensions:
        extensions_str = ','.join(valid_extensions)
        raise ValidationError(f'Unacceptable file extension, only support: [{extensions_str}].')


def birthdate_validator(value):
    if value >= timezone.now().date():
        raise ValidationError('Date must be in the past.')
