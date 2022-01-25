from django.db import models
from django.conf import settings
from rest_framework import serializers


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    type = models.CharField(max_length=128)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='project_author',
        related_query_name='project_author'
    )


class Contributor(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user',
        related_query_name='user'
    )
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name='project_contributors',
        related_query_name='project_contributors'
    )
    permission = serializers.ChoiceField(choices=[('1', 'all'), ('2', 'none')])
    role = models.CharField(max_length=128, default='contributor')


class Issue(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    tag = models.CharField(max_length=128)
    priority = models.CharField(max_length=128)
    status = models.CharField(max_length=128)
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name='issue_project',
        related_query_name='issue_project'
    )
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='issue_author',
        related_query_name='issue_author'
    )
    assignee = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='issue_assignee',
        related_query_name='issue_assignee'
    )
    create_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.TextField(max_length=2048)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comment_author',
        related_query_name='comment_author'
    )
    issue = models.ForeignKey(
        to=Issue,
        on_delete=models.CASCADE,
        related_name='comment_issue',
        related_query_name='comment_issue'
    )
    create_time = models.DateTimeField(auto_now_add=True)
