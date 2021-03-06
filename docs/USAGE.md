# Usage Guide 

## Field

The quickest way to add rich text editing capabilities to your models is to use the included ``RichTextField`` model field type. A CKEditor widget is rendered as the form field but in all other regards the field behaves as the standard Django ``TextField``. For example::

    from django.db import models
    from ckeditor.fields import RichTextField

    class Post(models.Model):
        content = RichTextField()


## Widget

Alernatively you can use the included ``CKEditorWidget`` as the widget for a formfield. For example::

    from django import forms
    from django.contrib import admin
    from ckeditor.widgets import CKEditorWidget

    from post.models import Post

    class PostAdminForm(forms.ModelForm):
        content = forms.CharField(widget=CKEditorWidget())
        class Meta:
            model = Post

    class PostAdmin(admin.ModelAdmin):
        form = PostAdminForm

    admin.site.register(Post, PostAdmin)


Note that when using outside of admin panel you will have to make sure all form media is present for the editor to work. You may have to render the media like so::

    <form>
        {{ myform.media }}
        {{ myform.as_p }}
        <input type="submit"/>
    </form>



## Management Commands

Included is a management command to create thumbnails for images already contained in ``CKEDITOR_UPLOAD_PATH``. This is useful to create thumbnails when starting to use django-ckeditor with existing images. Issue the command as follows::

    $ ./manage.py generateckeditorthumbnails

**NOTE**: If you're using custom views remember to include ckeditor.js in your form's media either through ``{{ form.media }}`` or through a ``<script>`` tag. Admin will do this for you automatically. See `Django's Form Media docs <http://docs.djangoproject.com/en/dev/topics/forms/media/>`_ for more info.

## Using S3

See http://django-storages.readthedocs.org/en/latest/


## If you want to use allowedContent

To allowedContent works, disable **stylesheetparser** plugin.
So included this on your settings.py.::

    CKEDITOR_CONFIGS = {
        "default": {
            "removePlugins": "stylesheetparser",
        }
    }

## Versioning

First two numbers resemble ckeditor version used in the package. The third is used to issue releases for given ckeditor bundle (fixes, new features)
