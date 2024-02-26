from django import template


register = template.Library()

CURRENCIES_SYMBOLS = {
    'rub': '₽',
    'usd': '$',
}

words = ['Аршавин', 'Блог', 'Учител']


@register.filter()
def currency(value, code='rub'):
    postfix = CURRENCIES_SYMBOLS[code]
    return f'{value} {postfix}'


@register.filter()
def censor(text):
    for w in words:
        text = text.replace(w[1:], '*' * len(w[1:]))
    return text