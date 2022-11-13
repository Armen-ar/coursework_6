from django.db import models


class Ad(models.Model):
    title = models.CharField(verbose_name="Название товара.", max_length=100)
    price = models.PositiveIntegerField(verbose_name="Цена товара.")
    description = models.TextField(verbose_name="Описание товара.")
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(verbose_name="Фото товара.", null=True)

    class Meta:
        verbose_name = "Объявление."
        verbose_name_plural = "Объявления."
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(verbose_name="Комментарии.")
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='ads')
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Комментарии."
        verbose_name_plural = "Комментария."
        ordering = ["-created_at"]

    def __str__(self):
        return self.text
