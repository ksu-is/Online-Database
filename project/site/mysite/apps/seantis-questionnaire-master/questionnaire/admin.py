#!/usr/bin/python
from django.utils.translation import ugettext as _
from django.contrib import admin
from models import Answer
from models import Choice
from models import Question
from models import Questionnaire
from models import QuestionSet
from models import RunInfo
from models import RunInfoHistory
from models import Subject

adminsite = admin.site


class SubjectAdmin(admin.ModelAdmin):
    search_fields = [
        'surname',
        'givenname',
        'email'
    ]

    list_display = [
        'surname',
        'givenname',
        'email'
    ]


class ChoiceAdmin(admin.ModelAdmin):
    list_display = [
        'sortid',
        'text',
        'value',
        'question'
    ]


class ChoiceInline(admin.TabularInline):
    model = Choice

    ordering = [
        'sortid'
    ]

    extra = 5


class QuestionSetAdmin(admin.ModelAdmin):
    ordering = [
        'questionnaire',
        'sortid'
    ]

    list_filter = [
        'questionnaire'
    ]

    list_display = [
        'questionnaire',
        'heading',
        'sortid'
    ]

    list_editable = [
        'sortid'
    ]


class QuestionAdmin(admin.ModelAdmin):
    ordering = [
        'questionset__questionnaire',
        'questionset',
        'number'
    ]

    inlines = [
        ChoiceInline
    ]

    list_filter = [
        'questionset__questionnaire'
    ]

    def changelist_view(self, request, extra_context=None):
        """Hack to have Questionnaire list accessible for custom changelist
        template

        """
        if not extra_context:
            extra_context = {}

        questionnaire_id = request.GET.get(
            'questionset__questionnaire__id__exact', None
        )
        if questionnaire_id:
            args = {"id": questionnaire_id}
        else:
            args = {}
        extra_context['questionnaires'] = Questionnaire.objects.filter(
            **args
        ).order_by('name')
        return super(QuestionAdmin, self).changelist_view(
            request, extra_context
        )


class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'redirect_url',
        'export'
    ]
    readonly_fields = [
        'export'
    ]

    def export(self, obj):
        return '<a href="/q/csv/%s">%s</a>' % (obj.id, _("Download data"))

    export.allow_tags = True
    export.short_description = _('Export to CSV')


class RunInfoAdmin(admin.ModelAdmin):
    list_display = [
        'random',
        'runid',
        'subject',
        'created',
        'emailsent',
        'lastemailerror'
    ]


class RunInfoHistoryAdmin(admin.ModelAdmin):
    pass


class AnswerAdmin(admin.ModelAdmin):
    search_fields = [
        'subject__email',
        'runid',
        'question__number',
        'answer'
    ]

    list_display = [
        'runid',
        'subject',
        'question'
    ]

    list_filter = [
        'subject',
        'runid'
    ]

    ordering = [
        'subject',
        'runid',
        'question'
    ]


adminsite.register(Questionnaire, QuestionnaireAdmin)
adminsite.register(Question, QuestionAdmin)
adminsite.register(QuestionSet, QuestionSetAdmin)
adminsite.register(Subject, SubjectAdmin)
adminsite.register(RunInfo, RunInfoAdmin)
adminsite.register(RunInfoHistory, RunInfoHistoryAdmin)
adminsite.register(Answer, AnswerAdmin)
