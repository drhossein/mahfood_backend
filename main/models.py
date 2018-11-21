from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Food(models.Model):
    name = models.CharField(max_length=128, default="food")
    description = models.CharField(max_length=512)
    create_date = models.DateTimeField(auto_now_add=True)
    picture = models.FileField(blank=True, null=True, upload_to="static/food_pics/")

    def image_tag(self):
        return ("<img src='/%s' style='max-width:250px; "
                         "height=auto'/>" % self.picture)


class Reserve(models.Model):
    TYPE_CHOICE = (
        (1, "lunch"),
        (2, 'dinner',)
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    food = models.ForeignKey('main.Food',on_delete=models.CASCADE)
    reserve_date = models.DateField(auto_now_add=True)
    type = models.IntegerField(choices=TYPE_CHOICE,default=1)



REPO = "https://github.com/drhossein/mahfood.git"