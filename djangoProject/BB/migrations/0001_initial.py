# Generated by Django 3.2.4 on 2021-07-24 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('text', models.CharField(max_length=3500)),
                ('Likes', models.IntegerField(default=0)),
                ('Dislikes', models.IntegerField(default=0)),
                ('Category', models.CharField(choices=[('Танки', 'Танки'), ('Хиллы', 'Хиллы'), ('ДД', 'ДД'), ('Торговцы', 'Торговцы'), ('Гилдмастеры', 'Гилдмастеры'), ('Квестгиверы', 'Квестгиверы'), ('Кузнецы', 'Кузнецы'), ('Кожевники', 'Кожевники'), ('Зельевары', 'Зельевары'), ('Мастера заклинаний', 'Мастера заклинаний')], max_length=20)),
                ('filesForWeb', models.ImageField(blank=True, default='', upload_to='images/')),
                ('whoDisliked', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='whoDisliked', to=settings.AUTH_USER_MODEL)),
                ('whoLiked', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='whoLiked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1500)),
                ('msgFrom', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fromPerson', to=settings.AUTH_USER_MODEL)),
                ('msgTo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='toPerson', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
