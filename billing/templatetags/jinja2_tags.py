from jinja2 import nodes
from jinja2.ext import Extension
 
from django import template
from django.template.loader import render_to_string
 

register = template.Library()
 
 
class MerchantExtension(Extension):
 
    tags = {'render_integration'}
 
    def parse(self, parser):
        stream = parser.stream
