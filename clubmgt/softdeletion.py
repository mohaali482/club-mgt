from django.utils import timezone


def regenerate_field_for_soft_deletion(obj, field_name):
    timestamp = timezone.now().timestamp()
    slug_suffix = f'-deleted_at-{timestamp}'
    new_slug = getattr(obj, field_name)

    return new_slug + slug_suffix
