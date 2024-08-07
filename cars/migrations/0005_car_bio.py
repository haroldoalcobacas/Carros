from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0004_carinventory"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="bio",
            field=models.TextField(blank=True, null=True),
        ),
    ]
