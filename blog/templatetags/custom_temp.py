# custom_filters.py
from collections import Counter as cntr
from django import template
import json

register = template.Library()

@register.filter
def ranger(value):
    return range(value)

@register.filter
def breakr(value,n):
    nv = value.split(",")
    return n[(3*int(nv[0]))+int(nv[1])]

@register.filter
def combine(value,n):
    return f"{value},{n}"

@register.filter
def lenn(value):
    if len(value) % 3 == 0:
        return (len(value) // 3), 3-len(value) % 3
    else:
        return (len(value) // 3)+1, len(value) % 3

@register.filter
def index1(value,n):
    return value[n]

@register.filter
def neg(value):
    return value -1

@register.filter
def pos(value):
    return value +1

@register.filter
def summ(value):
    return value[:130] + "..."

# @register.filter
# def Marking(value):
#     """Split a string into a list of paragraphs."""
#     count = cntr(value[:3])
#     if count["#"]: return count["#"]
#     if count["-"]: return 10+count["-"]
#     if count["$"]: return 20+count["$"]
#     if count["~"]: return 30+ int(value[1:3])

# @register.filter
# def first_nchars(value,n):
#     return value[:n]

# @register.filter
# def last_nchars(value,n):
#     return value[n:]

# @register.filter
# def title_case(value):
#     return str(value).title()

@register.filter(name='attr')
def attr(value, arg):
    attrs = {}
    for pair in arg.split(';'):
        try:
            key, value = pair.split(':')
            attrs[key] = value
        except ValueError:
            pass
    return value.as_widget(attrs=attrs)

@register.filter(name='add_class')
def add_class(value, arg):
    css_classes = value.field.widget.attrs.get('class', '').split()
    css_classes.append(arg)
    value.field.widget.attrs['class'] = ' '.join(css_classes)
    return value

# @register.filter
# def makelister(value):
#     return value.split("\n")

# @register.filter
# def mjson(value):
#     li = []
#     for i in list(value.values()):
#         ly = []
#         for k,j in i.items():
#             ly.append(str(k)+":"+str(j)+"/j")
#         li.append("".join(ly)+"/p")
#     return json.dumps(li)

# @register.filter
# def Maker(value):
#     """Split a string into a list of paragraphs."""
#     l = ""

#     for v in value:
#         if "#" in v:
#             v = v.replace("#", "")
#         if "-" in v:
#             v = v.replace("-", "")
#         if "$" in v:
#             v = v.replace("$", "")
#         if "~" in v:
#             v = v.replace("~", "")
#         l+= v

#     return l

# @register.filter
# def catego(value):
#     """Split a string into a list of paragraphs."""
#     return [i["name"] for i in value.values()]

# @register.filter
# def catego_split(r):
#     h = [[],[]]
#     for j in range(2):
#         for i in range(len(r)):
#             if i%2==j:
#                 h[j].append(r[i])
#     # for i in range(len(r)):
#     #     if i%2==1:
#     #         h[1].append(r[i])
    
#     if len(h[0]) > len(h[1]):
#         h[1].append(None)
#     else:
#         h[0].append(None)
#     return h

# @register.filter
# def img_list(value):
#     return value[0] if len(value) > 0 else False

# @register.filter
# def img_n(value, n):
#     return value[n-30]

# @register.filter
# def Str_n(value,n):
#     for t, l in enumerate(n):
#         if l.image.url == value:
#             return t