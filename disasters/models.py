
# from django.db import models
# from .utils import translate_text


# class DisasterType(models.Model):
#     name = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name


# class Disaster(models.Model):
#     name = models.CharField(max_length=200)
#     event_date = models.DateField()
#     description_english = models.TextField()
#     description_french = models.TextField(blank=True)  # Allow blank for initial generation
#     disaster_type = models.ForeignKey(DisasterType, on_delete=models.CASCADE)


#     def save(self, *args, **kwargs):
#         # Generate French description if it's blank and English description is provided
#         if not self.description_french and self.description_english:
#             self.description_french = f"{translate_text(self.description_english, target_language='fr')} (Auto-Translated)"
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ['-event_date']



    

from django.db import models
from .utils import translate_text  # Ensure this import is correct


class Province(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class City(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
    



class DisasterType(models.Model):
    en_name = models.CharField(max_length=100)
    fr_name = models.CharField(max_length=100)

    def __str__(self):
        return self.en_name
    

    class Meta:
        verbose_name = "Disaster Type"
        verbose_name_plural = "Disaster Types"
    
    

class Disaster(models.Model):
    name = models.CharField(max_length=200)
    event_date = models.DateField()
    description_english = models.TextField()
    description_french = models.TextField(blank=True)
    disaster_type = models.ForeignKey(DisasterType, on_delete=models.CASCADE)

    fatalities = models.PositiveIntegerField(default=0)
    injuries = models.PositiveIntegerField(default=0)
    affected = models.PositiveIntegerField(default=0)
    evacuated = models.PositiveIntegerField(default=0)
    cost = models.PositiveIntegerField(default=0)
    payments = models.PositiveIntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()

    source = models.TextField()
    comments = models.TextField()

    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)



    def save(self, *args, **kwargs):
        if not self.description_french and self.description_english:
            self.description_french = f"{translate_text(self.description_english, target_language='fr')} (Auto-Translated)"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-event_date']
