# Generated by Django 4.1.3 on 2023-07-26 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0010_rename_realcamera_products_rearcamera'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='SimilarImage1',
            field=models.ImageField(blank=True, null=True, upload_to='SimilarPartsImages_1/'),
        ),
        migrations.AddField(
            model_name='products',
            name='SimilarImage2',
            field=models.ImageField(blank=True, null=True, upload_to='SimilarPartsImages_2/'),
        ),
        migrations.AddField(
            model_name='products',
            name='SimilarImage3',
            field=models.ImageField(blank=True, null=True, upload_to='SimilarPartsImages_3/'),
        ),
        migrations.AddField(
            model_name='products',
            name='SimilarImage4',
            field=models.ImageField(blank=True, null=True, upload_to='SimilarPartsImages_4/'),
        ),
        migrations.AddField(
            model_name='products',
            name='SimilarImage5',
            field=models.ImageField(blank=True, null=True, upload_to='SimilarPartsImages_5/'),
        ),
        migrations.AddField(
            model_name='products',
            name='SimilarImage6',
            field=models.ImageField(blank=True, null=True, upload_to='SimilarPartsImages_6/'),
        ),
        migrations.AddField(
            model_name='products',
            name='SimilarImage7',
            field=models.ImageField(blank=True, null=True, upload_to='SimilarPartsImages_7/'),
        ),
        migrations.AddField(
            model_name='products',
            name='SimilarImage8',
            field=models.ImageField(blank=True, null=True, upload_to='SimilarPartsImages_8/'),
        ),
        migrations.AddField(
            model_name='products',
            name='SimilarImage9',
            field=models.ImageField(blank=True, null=True, upload_to='SimilarPartsImages_9/'),
        ),
    ]
