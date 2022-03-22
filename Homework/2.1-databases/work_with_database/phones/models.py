from django.db import models


class Phone(models.Model):
    # Добавьте требуемые поля
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField(max_length=150)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return f"{self.name}, {self.slug}"


