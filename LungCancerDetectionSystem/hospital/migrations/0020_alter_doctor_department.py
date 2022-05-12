# Generated by Django 3.2.9 on 2022-05-09 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0019_alter_doctor_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Pulmonologists', 'Pulmonologists'), ('Dermatologists', 'Dermatologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')], default='Cardiologist', max_length=50),
        ),
    ]
