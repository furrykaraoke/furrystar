from django.db import models

# Create your models here.


class Song(models.Model):
    title = models.CharField(max_length=255, unique=True, db_index=True)
    play_count = models.IntegerField(default=0)
    jezyk = models.CharField(max_length=30, default="Brak")
    def __str__(self):
        return f"{self.title} Ilość odtworzeń {self.play_count}"


class Rating(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='ratings')
    nick = models.CharField(max_length=60)
    # recenzja = models.CharField(max_length=255)
    value = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.song.title} Zaśpiewał {self.nick} i ocenił na  {self.value} "
