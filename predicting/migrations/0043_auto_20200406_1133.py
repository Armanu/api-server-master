# Generated by Django 3.0.4 on 2020-04-06 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('predicting', '0042_symptom_professional'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Is returned in API requests.', max_length=256, verbose_name='Name')),
                ('label', models.CharField(max_length=256, verbose_name='Label')),
            ],
            options={
                'verbose_name': 'Disease Type',
                'verbose_name_plural': 'Disease Types',
            },
        ),
        migrations.AddField(
            model_name='disease',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='predicting.DiseaseType'),
        ),
    ]
