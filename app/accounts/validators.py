from django.core.exceptions import ValidationError

def validate_national_id(value):
    """
    Validate the format of the national ID.

    Ensure that the value consists of exactly ten digits.
    """
    if not value.isdigit() or len(value) != 10:
        raise ValidationError("National ID must be a ten-digit number.")
