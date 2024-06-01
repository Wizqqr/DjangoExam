from django.db import models

class Devis(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class YoutubeVideo(models.Model):
    video = models.URLField()

    def __str__(self):
        return self.video

class Gadget(models.Model):
    name = models.CharField(max_length=100, verbose_name='Gadget name')
    description = models.TextField(verbose_name='Gadget description')
    image = models.ImageField(upload_to='images/', verbose_name='Upload a gadget image')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Gadget price')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gadget'


class ReviewGadget(models.Model):
    gadget = models.ForeignKey(Gadget, on_delete=models.CASCADE, verbose_name='Gadget')
    stars = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.gadget.name}'

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.text