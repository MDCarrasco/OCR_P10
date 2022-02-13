from P10.SoftDesk.models import Project, Contributor, Issue, Comment
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import HyperlinkedModelSerializer


class ContributorSerializer(ModelSerializer):

    @staticmethod
    def check_user(project_id, user_id):
        if Contributor.objects.filter(project_id=project_id).filter(user_id=user_id):
            raise ValidationError({"user": "Can't have same contributor id twice for one project"})

    class Meta:
        model = Contributor
        fields = ("user", "role")


class ProjectSerializer(ModelSerializer):
    contributors = ContributorSerializer(source='project_contributors', read_only=True, many=True)

    class Meta:
        model = Project
        fields = ("id", "title", "type", "description", "contributors")


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ("id", "title", "description", "tag", "priority", "status", "assignee")

    def validate(self, data):
        if 'assignee' not in data:
            data['assignee'] = self.context["request"].user
        return data


class CommentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "description")
