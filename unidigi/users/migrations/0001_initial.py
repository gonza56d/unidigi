# Generated by Django 3.2 on 2021-05-06 06:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import unidigi.users.models.users


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='date and time when created')),
                ('modified', models.DateTimeField(auto_now_add=True, verbose_name='date and time when last modified')),
                ('username', models.CharField(error_messages={'unique': 'Username already in use'}, max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='Only lowercase letters and numbers allowed', regex='[a0-z9]')], verbose_name="user's username as unique identifier")),
                ('email', models.EmailField(error_messages={'unique': 'Email already in use'}, max_length=254, unique=True, verbose_name="user's email")),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
            managers=[
                ('objects', unidigi.users.models.users.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='date and time when created')),
                ('modified', models.DateTimeField(auto_now_add=True, verbose_name='date and time when last modified')),
                ('role', models.CharField(choices=[('T', 'Teacher'), ('S', 'Student')], max_length=1, verbose_name='profile role type')),
                ('first_name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Only letters allowed', regex='[aA-zZ]')], verbose_name="user's first names")),
                ('last_name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Only letters allowed', regex='[aA-zZ]')], verbose_name="user's last names")),
                ('birthday', models.DateField(blank=True, null=True, verbose_name="user's birthday")),
                ('picture', models.ImageField(blank=True, upload_to='profiles', verbose_name="user's profile picture")),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]