from P10.SoftDesk.serializers import (
    ProjectSerializer, IssueSerializer, CommentSerializer, ContributorSerializer
)
from P10.SoftDesk.models import Project, Contributor, Issue, Comment

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
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


class IsProjectAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsProjectAuthor, )
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return (Project.objects.filter(project_contributors__user=self.request.user) | Project.objects.filter(author=self.request.user)).distinct()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class IssueViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsProjectAuthor, )
    serializer_class = IssueSerializer

    def get_queryset(self):
        return (Issue.objects.filter(project_id=self.kwargs.get("project_pk"), project__project_contributors__user=self.request.user) | Issue.objects.filter(project_id=self.kwargs.get("project_pk"), project__author=self.request.user)).distinct()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = IssueSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, project=Project.objects.get(id=self.kwargs.get("project_pk")))


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsProjectAuthor, )
    serializer_class = CommentSerializer

    def get_queryset(self):
        return (Comment.objects.filter(issue=self.kwargs.get("issue_pk"), issue__project__project_contributors__user=self.request.user)
        | Comment.objects.filter(issue=self.kwargs.get("issue_pk"), issue__project__author=self.request.user)).distinct()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, issue=Issue.objects.get(id=self.kwargs.get("issue_pk")))
