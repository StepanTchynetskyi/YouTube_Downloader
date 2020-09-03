from django.db import models

# Create your models here.
class Link(models.Model):
	link_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField(auto_now = True)
	def __str__(self):
		return f'{self.link_text}'
	class Meta:
		verbose_name_plural='Links'
