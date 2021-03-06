from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.response import Response

from pms.helpers.enums import ActionEnum
from pms.models.activity_log import ActivityLog
from pms.models.documents import Document
from pms.models.issues import Issue
from pms.models.projects import Project
from pms.serializers.document_serializers import DocumentSerializer
from pms.serializers.issues_serializers import IssueSerializer
from pms.serializers.projects_serializers import ProjectSerializer

__author__ = 'Ashraful'


class ProjectView(ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.filter()

    def get_queryset(self):
        params = self.request.GET
        name = params.get('name')
        queryset = self.queryset
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
        if instance:
            try:
                # Save documents
                doc_pks = self.request.data.get('documents')
                if doc_pks:
                    entries = Document.objects.filter(pk__in=doc_pks)
                    instance.documents.add(*entries)
                # Create activity log
                ActivityLog.log(
                    profile_id=self.request.user.profile.pk, action=ActionEnum.CREATE.value,
                    op_text="{0} has created {1}".format(self.request.user.profile.name, instance.name),
                    model_name=instance._meta.object_name, app_level=instance._meta.app_label,
                    reference_id=instance.pk
                )
            except Exception:
                # Here can be a error log
                pass
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetailsView(RetrieveUpdateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.filter()
    lookup_field = 'slug'


class ProjectIssuesView(ListAPIView):
    serializer_class = IssueSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        queryset = Issue.objects.filter(project__slug=slug)
        return queryset
