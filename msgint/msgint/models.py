from django.db import models
from hashlib import md5

class SampleMessage(models.Model):
    
    TAG_CHOICES = ((u'*', u'spam'), (u'+', u'normal'))
    
    content = models.TextField()
    digest = models.TextField()
    tag = models.TextField(choices = TAG_CHOICES)
    
    def update_content_digest(self):
        h = md5()
        h.update(self.content)
        self.digest = h.hexdigest().upper()
        