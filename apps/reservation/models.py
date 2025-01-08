from apps.common.models import BaseModel
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.translation import gettext_lazy as _
from apps.users.models import User



def resize_image(image_field, size=(800, 800)):
    """ Tasvirni qayta o'lchash funksiyasi """
    if image_field:
        img = Image.open(image_field)
        img.thumbnail(size)
        img_io = BytesIO()
        img.save(img_io, img.format)
        img_io.seek(0)
        image_field = InMemoryUploadedFile(img_io, None, image_field.name, 'image/jpeg', img_io.getbuffer().nbytes, None)
        return image_field
    return image_field


class Restaurant(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    address = models.CharField(max_length=255, verbose_name=_("Address"))
    description = models.TextField(verbose_name=_("Description"))
    resized_image = models.ImageField(
        upload_to="restaurants/", null=True, blank=True, verbose_name=_("Resized Image")
    )
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0, verbose_name=_("Average Rating"))
    reviews = models.PositiveIntegerField(default=0, verbose_name=_("Number of Reviews"))
    available_sites = models.PositiveIntegerField(verbose_name=_("Available sites"))
    opening_hours = models.JSONField(verbose_name=_("Opening Hours"))
    closed_days = models.JSONField(verbose_name=_("Closed Days"), null=True, blank=True)

    class Meta:
        verbose_name = _("Restaurant")
        verbose_name_plural = _("Restaurants")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.resized_image:
            self.resized_image = resize_image(self.resized_image)
        super(Restaurant, self).save(*args, **kwargs)


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()
    number_people = models.PositiveIntegerField()

    def __str__(self):
        return f"Reservation for {self.user} at {self.restaurant} on {self.reservation_time}"

    class Meta:
        verbose_name = _("Reservation")
        verbose_name_plural = _("Reservations")
