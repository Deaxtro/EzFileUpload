from django.db.models import FileField
from django.forms import forms
from django.utils.translation import gettext_lazy as _

class ContentTypeRestrictedFileField(FileField):
    
    def __init__(self, *args, **kwargs):
        self.content_types=kwargs.pop("content_types")
        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data=super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)
        file=data.file
        try:
            content_type=file.content_type
            if content_type not in self.content_types:
                raise forms.ValidationError(_('Only .pptx, .docx, and .xlsx file type allowed.'))
        except AttributeError:
            pass
        return data