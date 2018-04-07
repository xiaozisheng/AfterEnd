from django.db import models


class Awards(models.Model):
    a_id = models.AutoField(primary_key=True)
    a_name = models.CharField(max_length=255)
    a_context_url = models.CharField(max_length=255)
    a_video_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'awards'


class Importantdate(models.Model):
    id_important = models.AutoField(primary_key=True)
    id_pm_year = models.IntegerField()
    id_type = models.IntegerField()
    id_name = models.CharField(max_length=55)
    id_date = models.CharField(max_length=55)
    id_weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'importantdate'


class KeynoteSpeech(models.Model):
    ks_id = models.AutoField(primary_key=True)
    ks_datetime = models.DateTimeField()
    ks_awards = models.IntegerField()
    ks_p_code = models.IntegerField()
    ks_name = models.CharField(max_length=255)
    ks_human_info = models.TextField()
    ks_subsidiary_organ = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'keynote_speech'


class OrganizingCommittee(models.Model):
    oc_id = models.AutoField(primary_key=True)
    oc_start_year = models.TextField()  # This field type is a guess.
    oc_end_year = models.TextField()  # This field type is a guess.
    oc_post = models.IntegerField()
    oc_name = models.CharField(max_length=255)
    oc_subsidiary_organ = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'organizing_committee'


class Pastmeeting(models.Model):
    pm_id = models.AutoField(primary_key=True)
    pm_year = models.TextField()  # This field type is a guess.
    pm_location = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pastmeeting'


class Paper(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_code = models.CharField(max_length=255)
    p_awards = models.IntegerField()
    p_examination_questions = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'papaer'


class Seminar(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=255)
    s_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'seminar'
