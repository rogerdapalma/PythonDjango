# Generated by Django 5.0.5 on 2024-05-28 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, help_text='* Campo obrigatório', max_length=100, unique=True, verbose_name='Nome da instituição *')),
                ('sigla', models.CharField(blank=True, help_text='Se houver sigla, por favor, informe.', max_length=10, null=True, verbose_name='Sigla')),
                ('pais', models.CharField(max_length=30, verbose_name='País da instituição *')),
                ('estado', models.CharField(max_length=30, verbose_name='Estado ou província *')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade *')),
                ('is_active', models.BooleanField(default=True, help_text='Se ativo, a instituição pode ser usada no sistema', verbose_name='Ativo')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Hash')),
            ],
            options={
                'verbose_name': 'instituição',
                'verbose_name_plural': 'instituições',
                'ordering': ['-is_active', 'pais', 'estado', 'cidade'],
            },
        ),
    ]