from django.db import models

class Community(models.Model):
    name = models.CharField(max_length=30)
    creationDate = models.DateTimeField(auto_now_add=True)
    imageUrl = models.ImageField(upload_to='communities/', null=True, blank=True)

class Discussion(models.Model):
    theme = models.CharField(max_length=150)
    description = models.TextField()
    imageUrl = models.ImageField(upload_to='discussions/', null=True, blank=True)
    creationDate = models.DateTimeField(auto_now_add=True)
    userId = models.CharField(max_length=30)
    communityId = models.ForeignKey(Community, on_delete=models.CASCADE)

class Comment(models.Model):
    comm = models.TextField()
    creationDate = models.DateTimeField(auto_now_add=True)
    userId = models.CharField(max_length=30)

    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name="commentaries")

    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replies", null=True, blank=True)