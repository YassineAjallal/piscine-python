
def ft_filter(func: any, iterable: any):
    "recode the filter function"
    for it in [ita for ita in iterable if func(ita)]:
        yield it
