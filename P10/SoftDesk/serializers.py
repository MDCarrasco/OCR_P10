from P10.SoftDesk.models import Project, Contributor, Issue, Comment
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import HyperlinkedModelSerializer


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = "__all__"


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ("id", "title", "tag", "priority", "status", "assignee")


class CommentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "description")
