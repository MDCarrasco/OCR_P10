from rest_framework.generics import get_object_or_404
from rest_framework import status

from P10.SoftDesk.serializers import (
    ProjectSerializer, IssueSerializer, CommentSerializer, ContributorSerializer
)
from P10.SoftDesk.models import Project, Contributor, Issue, Comment

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ContributorSerializer

    def list(self, request, project_pk=None):
        queryset = Contributor.objects.filter(project=project_pk)
        serializer = ContributorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, project_pk=None):
        queryset = Contributor.objects.filter(pk=pk, project=project_pk)
        user = get_object_or_404(queryset, pk=pk)
        serializer = IssueSerializer(user)
        return Response(serializer.data)


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class IssueViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.filter(project_id=self.kwargs.get("project_pk"))

    def list(self, request, *args, **kwargs):
        queryset = Issue.objects.filter(project_id=kwargs.get("project_pk"))
        serializer = IssueSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, project=Project.objects.get(id=self.kwargs.get("project_pk")))

    def perform_update(self, serializer):
        serializer.save(author=self.request.user, project=Project.objects.get(id=self.kwargs.get("project_pk")))


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Issue.objects.filter(project_id=self.kwargs.get("project_pk"))

    def list(self, request, *args, **kwargs):
        queryset = Comment.objects.filter(issue__project=kwargs.get("project_pk"), issue=kwargs.get("issue_pk"))
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        queryset = Comment.objects.filter(id=kwargs.get("pk"), issue_id=kwargs.get("issue_pk"), issue__project_id=kwargs.get("project_pk"))
        comment = get_object_or_404(queryset, id=kwargs.get("pk"))
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, issue=Issue.objects.get(id=self.kwargs.get("issue_pk")))

    def perform_update(self, serializer):
        serializer.save(author=self.request.user, issue=Issue.objects.get(id=self.kwargs.get("issue_pk")))
