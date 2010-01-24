from django import template
from presentations.slideshare.models import Slideshare
register = template.Library()

@register.inclusion_tag('slideshare_embed.html')
def slideshare_embed(pres):
    return {'pres': pres}
#register.inclusion_tag('slideshare_embed.html')(slideshare_embed)

@register.simple_tag
def slideshare_test():
    return "This is a simple test tag"
# @register.tag(name="slideshare_embed")
# def do_slideshare_embed(parser, token):
#     """slideshare_embed template tag compiler"""
#     # Do something here
#     
#     return SlideshareEmbedNode()
#     
#     
# class SlideshareEmbedNode(template.Node):
#     """docstring for SlideshareEmbedNode"""
#     def __init__(self, arg):
#         super(SlideshareEmbedNode, self).__init__()
#         self.arg = arg
#         
#     def render(self, context):
#         """docstring for render"""
#         return "This is the output of the Slideshare_embed tag"
        