from django.apps import apps

# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import migrations, transaction


# user_model = get_user_model()
def forwards(apps, schema_editor):
    try:
        OldModel = apps.get_model("oc_lettings_site", "Profile")
    except LookupError:
        # The old app isn't installed.
        return

    NewModel = apps.get_model("profiles", "Profile")
    NewModel.objects.bulk_create(
        NewModel(favorite_city=old_object.favorite_city, user=old_object.user) for old_object in OldModel.objects.all()
    )


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial_profile"),
    ]

    if apps.is_installed("oc_lettings_site"):
        dependencies.append(("oc_lettings_site", "0002_auto_20231225_1557"))

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
