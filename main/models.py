from django.db import models

"""
Talaba(ism, guruh, kurs, kitob_soni)
Muallif(ism, jins, tugilgan_sana, kitoblar_soni, tirik)
Kitob(nom, janr, sahifa, muallif(FK))
Kutubxonachi(ism, ish_vaqti)
Record(talaba(FK), kitob(FK), kutubxonachi(FK), olingan_sana, qaytardi(default=False), qaytarish_sana). 
"""


class Talaba(models.Model):
    ism = models.CharField(max_length=255)
    guruh = models.CharField(max_length=20)
    kurs = models.PositiveSmallIntegerField(default=1)
    kitob_soni = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.ism


class Mualif (models.Model):
    JINS_CHOICES = (
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
    )

    ism = models.CharField(max_length=255)
    jins = models.CharField(max_length=20, choices=JINS_CHOICES, default='Erkak')
    tugilgan_sana = models.DateField(blank=True, null=True)
    kitob_soni = models.PositiveSmallIntegerField(blank=True, null=True)
    tirik = models.BooleanField(default=False)

    def __str__(self):
        return self.ism


class Kitob(models.Model):
    JANR_CHOICES = (
        ('Badiiy', 'Badiiy'),
        ('Ilmiy', 'Ilmiy'),
        ('Roman', 'Roman'),
        ('Doston', 'Doston'),
        ('She\'r', 'She\'r'),
        ('Ertak', 'Ertak'),
        ('Hikoya', 'Hikoya'),
    )

    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=40, choices=JANR_CHOICES, default='Badiiy')
    sahifa = models.PositiveSmallIntegerField()
    muallif = models.ForeignKey(Mualif, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.muallif}: {self.nom}"


class Kutubxonachi(models.Model):
    ISH_VAQTI_CHOICES = (
        ('08:00 - 12:30', '08:00 - 12:30'),
        ('12:30 - 20:00', '12:30 - 20:00'),
        ('20:00 - 02:00', '20:00 - 02:00'),
    )

    ism = models.CharField(max_length=255)
    ish_vaqti = models.CharField(max_length=40, choices=ISH_VAQTI_CHOICES)

    def __str__(self):
        return self.ism


class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    kutubxonachi = models.ForeignKey(Kutubxonachi, on_delete=models.CASCADE)
    olingan_sana = models.DateField(auto_now_add=True)
    qaytardi = models.BooleanField(default=False)
    qaytargan_sana = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.talaba}: {self.kitob}"