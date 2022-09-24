def is_ajax(request):
    """Checks for an AJAX request"""
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'

def get_objects_or_none(class_model, **kwargs):
    """Returns objects if exists or None if it doesn't exist"""
    try:
        return class_model.objects.filter(**kwargs)
    except(KeyError, class_model.DoesNotExist):
        return None
