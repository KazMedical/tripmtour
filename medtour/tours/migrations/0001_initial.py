# Generated by Django 3.2.15 on 2023-02-10 09:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import medtour.tours.instances
import multiselectfield.db.fields
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20230210_1505'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название тура')),
                ('short_desc', models.CharField(blank=True, max_length=150, null=True, verbose_name='Короткое описание')),
                ('currency', models.IntegerField(blank=True, choices=[(0, 'USD'), (1, 'KZT'), (2, 'UZS'), (3, 'KGS'), (4, 'EUR')], default=1, null=True, verbose_name='Валюта')),
                ('BIN', models.CharField(blank=True, max_length=16, null=True)),
                ('IIK', models.CharField(blank=True, max_length=50, null=True)),
                ('BIK', models.CharField(blank=True, max_length=15, null=True)),
                ('requisites', models.CharField(blank=True, max_length=50, null=True, verbose_name='Для предоплаты (IBAN)')),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('is_moderated', models.BooleanField(db_index=True, default=False, verbose_name='Прошел модерацию')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('district', models.CharField(blank=True, max_length=50, null=True, verbose_name='Район')),
                ('street', models.CharField(blank=True, max_length=50, null=True, verbose_name='Улица')),
                ('home_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер дома')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя директора')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия директора')),
                ('email', models.EmailField(blank=True, help_text='Пожалуйста напишите ваш эмейл', max_length=254, null=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False, help_text='Отметьте, если удалён тур', verbose_name='Удалён?')),
                ('youtube_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ссылка на Youtube')),
                ('publicId', models.CharField(blank=True, max_length=200, null=True, verbose_name='CloudPayments Public ID')),
                ('slug', models.SlugField(blank=True, max_length=255, verbose_name='Слаг')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tours', to='users.organizationcategory', verbose_name='Категория')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tour_countries', to='users.country', verbose_name='Страна')),
                ('org', models.ForeignKey(help_text='Прикрепленная организация к туру', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tours', to='users.organization', verbose_name='Организация')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tour_regions', to='users.region', verbose_name='Регион')),
            ],
            options={
                'verbose_name': '* Тур',
                'verbose_name_plural': '* Туры',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TourShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя изображения')),
                ('photo', sorl.thumbnail.fields.ImageField(upload_to=medtour.tours.instances.get_shots_path, verbose_name='Изображение')),
                ('tour', models.ForeignKey(help_text='Прикрепленный тур', on_delete=django.db.models.deletion.CASCADE, related_name='tour_shots', to='tours.tour', verbose_name='Изображения тура')),
            ],
            options={
                'verbose_name': 'Изображения тура',
                'verbose_name_plural': 'Изображения туров',
            },
        ),
        migrations.CreateModel(
            name='TourPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=medtour.tours.instances.get_price_path)),
                ('tour', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='price_file', to='tours.tour')),
            ],
        ),
        migrations.CreateModel(
            name='TourPhones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15, verbose_name='Телефонный номер')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour_phones', to='tours.tour', verbose_name='Тур')),
            ],
            options={
                'verbose_name': 'Телефонный номер тура',
                'verbose_name_plural': 'Телефонные номера тура',
            },
        ),
        migrations.CreateModel(
            name='TourPaidServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('name', models.CharField(help_text='Наименование платной услуги', max_length=100, verbose_name='Название услуги')),
                ('description', models.TextField(blank=True, help_text='Описание конкретной услуги', null=True, verbose_name='Описание услуги')),
                ('price', models.IntegerField(help_text='Стоимость платной услуги', verbose_name='Стоимость услуги')),
                ('hide', models.BooleanField(default=False, verbose_name='Скрыть')),
                ('tour', models.ForeignKey(help_text='Прикрепленный тур', on_delete=django.db.models.deletion.CASCADE, related_name='services', to='tours.tour', verbose_name='Прикрепленный тур')),
            ],
            options={
                'verbose_name': '* Платная услуга тура',
                'verbose_name_plural': '* Платные услуги тура',
            },
        ),
        migrations.CreateModel(
            name='TourLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lon', models.FloatField(blank=True, null=True, verbose_name='Долгота')),
                ('lat', models.FloatField(blank=True, null=True, verbose_name='Широта')),
                ('tour', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='tours.tour')),
            ],
            options={
                'verbose_name': 'Локация тура',
                'verbose_name_plural': 'Локации тура',
            },
        ),
        migrations.CreateModel(
            name='TourBookingWeekDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', multiselectfield.db.fields.MultiSelectField(choices=[(0, 'YESTERDAY'), (1, 'MONDAY'), (2, 'TUESDAY'), (3, 'WEDNESDAY'), (4, 'THURSDAY'), (5, 'FRIDAY'), (6, 'SATURDAY')], default=[0, 1, 2, 3, 4, 5, 6], max_length=13)),
                ('tour', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tours.tour')),
            ],
            options={
                'verbose_name': 'День бронирования тура',
                'verbose_name_plural': 'Дни бронирований тура',
            },
        ),
        migrations.CreateModel(
            name='CommentTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Чистота')),
                ('service', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Сервис')),
                ('location', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Местоположение')),
                ('staff', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Чистота')),
                ('proportion', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Соотношение цена/качество')),
                ('text', models.TextField(validators=[django.core.validators.MinLengthValidator(20, message='Минимальная длина отзыва должна превышать 20 символа')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tours.tour')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Отзыв тура',
                'verbose_name_plural': 'Отзывы тура',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='AdditionalTitles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tour_titles', to='tours.tour')),
            ],
            options={
                'verbose_name': 'Заголовок дополнительной услуги',
                'verbose_name_plural': 'Заголовки дополнительных услуг',
            },
        ),
        migrations.CreateModel(
            name='AdditionalInfoTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_titles', to='tours.additionaltitles')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_titles', to='tours.tour')),
            ],
            options={
                'verbose_name': '* Заголовка бесплатных услуг',
                'verbose_name_plural': '* Заголовки бесплатных услуг',
            },
        ),
        migrations.CreateModel(
            name='AdditionalInfoServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=255, verbose_name='Наименование услуги')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_services', to='tours.additionalinfotitle')),
            ],
            options={
                'verbose_name': 'Бесплатная услуга',
                'verbose_name_plural': 'Бесплатные услуги тура',
            },
        ),
    ]
