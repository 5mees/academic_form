from django.db import models

class Academic(models.Model):

    BATCH = (
        ('018', '018'),
        ('017', '017'),
        ('016', '016'),
        ('015', '015'),
    )
    SP = (
        ('GIS/RM', 'GIS/RM'),
        ('Geodisy', 'Geodisy'),
        ('Photogrammetry', 'Photogrammetry'),
    )
    TIME  = (
        ('ساعتان في الاسبوع', 'ساعتان في الاسبوع'),
        ('ثلاث ساعات في الاسبوع', 'ثلاث ساعات في الاسبوع'),
        ('اكثر من ثلات ساعات', 'اكثر من ثلات ساعات'),
    )
    name = models.CharField(max_length=100)
    index = models.IntegerField(primary_key=True)
    batch = models.CharField(max_length=10, choices=BATCH)
    specialty = models.CharField(max_length=20, choices=SP)
    time = models.CharField(max_length=50, choices=TIME)
    notes = models.TextField(max_length=200)

    def __str__(self):
        return self.name