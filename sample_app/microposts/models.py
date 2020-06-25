from django.db import models
from django.contrib.auth.models import User

class Micropost(models.Model):
    content = models.TextField(max_length=140)
    user = models.ForeignKey(User, editable=False, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __unicode__(self):
        return "%s: %s" % (self.user, self.content)

    def gravatar(self):
        return self.user.get_profile().gravatar(size=30)
