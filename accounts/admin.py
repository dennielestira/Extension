from django.contrib import admin
from .models import (
    CustomUser, Department, Document, DocumentComment, DocumentFile,
    ChatMessage, AnnualReport,
    ExtensionActivity, Linkage, QuarterlyReport, ExtensionProject
)

admin.site.register(CustomUser)
admin.site.register(Department)
admin.site.register(Document)
admin.site.register(DocumentComment)
admin.site.register(DocumentFile)
admin.site.register(ChatMessage)
admin.site.register(AnnualReport)
admin.site.register(ExtensionActivity)
admin.site.register(Linkage)
admin.site.register(QuarterlyReport)
admin.site.register(ExtensionProject)
