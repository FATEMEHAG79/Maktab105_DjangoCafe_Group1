from django.db import migrations


def create_category(apps, schema_editor):
    category = apps.get_model("coffeeshop","Category")
    category.objects.create(name="hot drinks",image="media/cover/Hot_Drinks_Logo.jpg")


class Migration(migrations.Migration):
    dependencies = [
        ("coffeeshop","0005_alter_category_image_alter_category_name")
    ]
    operations = [
        migrations.RunPython(create_category),
    ]
