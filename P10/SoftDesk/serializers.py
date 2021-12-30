from P10.SoftDesk.models import Project, Issue, Comment
from rest_framework.serializers import HyperlinkedModelSerializer


class ProjectSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ...


class ContributorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Issue
        fields = ...


class IssueSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Issue
        fields = ...


class CommentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ...
