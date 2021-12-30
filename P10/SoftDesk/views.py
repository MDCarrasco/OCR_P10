from rest_framework.generics import get_object_or_404

from P10.SoftDesk.serializers import ProjectSerializer, IssueSerializer, CommentSerializer
from P10.SoftDesk.models import Project, Issue, Comment

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class SignupView(APIView):

    def post(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class LoginView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class ProjectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer

    def list(self, request,):
        queryset = Project.objects.filter()
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Project.objects.filter()
        project = get_object_or_404(queryset, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)


class IssueViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = IssueSerializer

    def list(self, request, project_pk=None):
        queryset = Issue.objects.filter(project=project_pk)
        serializer = IssueSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, project_pk=None):
        queryset = Issue.objects.filter(pk=pk, project=project_pk)
        issue = get_object_or_404(queryset, pk=pk)
        serializer = IssueSerializer(issue)
        return Response(serializer.data)


class CommentViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def list(self, request, project_pk=None, issue_pk=None):
        queryset = Comment.objects.filter(issue__project=project_pk, issue=issue_pk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, project_pk=None, issue_pk=None):
        queryset = Comment.objects.filter(pk=pk, issue=issue_pk, issue__project=project_pk)
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
