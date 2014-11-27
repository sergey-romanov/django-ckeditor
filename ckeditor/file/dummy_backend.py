import os.path

from ckeditor import utils


def create_thumbnail(file_path, format):
    raise NotImplementedError


def should_create_thumbnail(file_path):
    return False


def file_verify(file_object):
    valid_extensions = ['.zip', '.rar', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.pdf', '.swf']
    _, extension = os.path.splitext(file_object.name)
    if not extension.lower() in valid_extensions:
        raise utils.NotAnPermittedFileTypeException
