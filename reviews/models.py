from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from PIL import Image


class Ticket(models.Model):
    """
    Represents a ticket created by a user,
    which can be reviewed by others.
    """
    title = models.CharField(max_length=128, verbose_name='Titre')
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (300, 300)

    def resize_image(self):
        """
        Resizes the image associated with the ticket to a maximum size
        if the image dimensions exceed IMAGE_MAX_SIZE.
        """
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to resize the image
        after the Ticket instance is saved, if an image is provided.
        """
        super().save(*args, **kwargs)
        if self.image:
            self.resize_image()


class Review(models.Model):
    """
    Represents a review submitted for a specific Ticket.
    Includes a rating, headline, and body.
    """
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='Note')
    headline = models.CharField(max_length=128, verbose_name='Titre')
    body = models.TextField(max_length=8192, blank=True, verbose_name='Commentaire')
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):
    """
    Represents a relationship where one user follows another.
    Ensures that a user cannot follow another user multiple times.
    """
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='following')
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE,
                                      related_name='followed_by')

    class Meta:
        """
        Meta class for UserFollows model.
        Ensures uniqueness for user-followed_user pairs.
        """
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('user', 'followed_user',)
