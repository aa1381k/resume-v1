from django import template

register = template.Library()


@register.filter(name='mul')
def mul(value):
    return int(value) * 20


@register.filter(name='filter_image')
def filter_image(images, image_id):
    return images.filter(post_id=image_id)


@register.filter(name='thumbnail_image')
def thumbnail_image(images, image_id):
    return images.filter(post_id=image_id).filter(image_id=0).first().post_image