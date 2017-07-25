from django.db import models

# Create your models here.
PRIOR_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
)


class ToDo(models.Model):
    content = models.CharField(max_length=100)
    date = models.DateField()
    prior = models.IntegerField(default=1, choices=PRIOR_CHOICES)
    expire_date = models.DateField()
    is_finished = models.BooleanField(default=False)

    class Meta:
        db_table = 'ToDo'

    def __unicode__(self):
        return self.content