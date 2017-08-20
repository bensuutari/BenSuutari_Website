from __future__ import unicode_literals
from django.db import models
from django.db.models import permalink
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.core.urlresolvers import reverse
# Create your models here.
class Post(models.Model):
	title=models.CharField(max_length=140)
	slug = models.SlugField(unique=True)
	body=models.TextField()
	date=models.DateTimeField()
	def __unicode__(self):
		return self.title

	
	def get_absolute_url(self):	
		return reverse("blog:detail",kwargs={"slug":self.slug})

def create_slug(instance,new_slug=None):
	slug=slugify(instance.title)
	if new_slug is not None:
		slug=new_slug
	qs=Post.objects.filter(slug=slug)
	exists=sq.exists()
	if exists:
		new_slug="%s-%s" %(slug,qs.first().id)
		return create_slug(instance,new_slug=new_slug)
	return slug

def pre_save_post_signal_receiver(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug=create_slug(instance)


pre_save.connect(pre_save_post_signal_receiver,sender=Post)
