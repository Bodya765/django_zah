from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name
    
class Category2(models.Model):
    name = models.CharField(max_length=255)

class News(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=50)
    author = models.CharField(max_length=38)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Оголошення'
        verbose_name_plural = 'Оголошення'
