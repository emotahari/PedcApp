from django.core.exceptions import ValidationError


def positive_check(value):
    if value < 0 :
        raise  ValidationError("این مقدار نمی تواند مقداری منفی باشد.")