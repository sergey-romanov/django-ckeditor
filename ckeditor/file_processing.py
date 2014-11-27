from django.conf import settings


def get_backend():
    from ckeditor.file import dummy_backend as backend
    return backend
