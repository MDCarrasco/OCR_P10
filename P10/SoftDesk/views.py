from rest_framework.generics import get_object_or_404

from P10.SoftDesk.serializers import (
    ProjectSerializer, IssueSerializer, CommentSerializer, ContributorSerializer
)
from P10.SoftDesk.models import Project, Contributor, Issue, Comment

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ContributorViewSet(viewsets.ModelViewSet):
    lookup_field = 'user'
    permission_classes = (IsAuthenticated,)
    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.filter(project_id=self.kwargs.get("project_pk"))

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ContributorSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.check_user(self.kwargs.get("project_pk"), self.request.data["user"])
        serializer.save(project=Project.objects.get(id=self.kwargs.get("project_pk")))

    def perform_update(self, serializer):
        serializer.check_user(self.kwargs.get("project_pk"), self.request.data["user"])
        serializer.save(project=Project.objects.get(id=self.kwargs.get("project_pk")))


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class IssueViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.filter(project_id=self.kwargs.get("project_pk"))

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = IssueSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, project=Project.objects.get(id=self.kwargs.get("project_pk")))

    def perform_update(self, serializer):
        serializer.save(author=self.request.user, project=Project.objects.get(id=self.kwargs.get("project_pk")))


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

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
