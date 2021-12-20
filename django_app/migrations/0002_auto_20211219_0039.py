# Generated by Django 3.1.3 on 2021-12-19 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chambre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('town', models.DateTimeField()),
                ('landlord', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('room', models.IntegerField(max_length=50)),
                ('tenant', models.IntegerField(max_length=50)),
                ('landlord', models.IntegerField(max_length=50)),
                ('nbr_persons', models.IntegerField(max_length=50)),
                ('in_date', models.DateTimeField(max_length=50)),
                ('out_date', models.DateTimeField(max_length=50)),
                ('total_price', models.FloatField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('identifiant', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mail_adresse', models.EmailField(max_length=50)),
                ('birth_date', models.DateTimeField()),
                ('gender', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ville',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.FloatField()),
                ('chambre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.chambre')),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.AddField(
            model_name='chambre',
            name='reservation',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='django_app.reservation'),
        ),
        migrations.CreateModel(
            name='locateur',
            fields=[
                ('utilisateur_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_app.utilisateur')),
                ('benefits', models.FloatField()),
                ('chambre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.chambre')),
            ],
            bases=('django_app.utilisateur',),
        ),
        migrations.CreateModel(
            name='locataire',
            fields=[
                ('utilisateur_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_app.utilisateur')),
                ('balance', models.FloatField()),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.reservation')),
            ],
            bases=('django_app.utilisateur',),
        ),
    ]