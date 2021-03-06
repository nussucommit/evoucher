# Generated by Django 3.1 on 2021-04-08 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '__first__'),
        ('voucher', '0001_initial'),
        ('faculty', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='InFaculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculty_to_student', to='faculty.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='InOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_to_student', to='organization.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Redeems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('nusnet_id', models.CharField(max_length=16, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('year', models.PositiveIntegerField()),
                ('faculties', models.ManyToManyField(related_name='students_faculties', through='student.InFaculty', to='faculty.Faculty')),
                ('organizations', models.ManyToManyField(related_name='students_organizations', through='student.InOrganization', to='organization.Organization')),
                ('vouchers', models.ManyToManyField(related_name='students_vouchers', through='student.Redeems', to='voucher.Voucher')),
            ],
        ),
        migrations.AddField(
            model_name='redeems',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_to_voucher', to='student.student'),
        ),
        migrations.AddField(
            model_name='redeems',
            name='voucher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voucher_to_student', to='voucher.voucher'),
        ),
        migrations.AddField(
            model_name='inorganization',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_to_organization', to='student.student'),
        ),
        migrations.AddField(
            model_name='infaculty',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_to_faculty', to='student.student'),
        ),
        migrations.AlterUniqueTogether(
            name='redeems',
            unique_together={('voucher', 'student')},
        ),
        migrations.AlterUniqueTogether(
            name='inorganization',
            unique_together={('organization', 'student')},
        ),
        migrations.AlterUniqueTogether(
            name='infaculty',
            unique_together={('faculty', 'student')},
        ),
    ]
