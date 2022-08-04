from core.templatetags import register
from django.template.defaultfilters import stringfilter


@register.filter(name="first_words")
@stringfilter
def first_n_words(value, arg):
    sentence = value.split(" ")
    trunc_sentence = sentence[:arg]
    return " ".join(trunc_sentence)
