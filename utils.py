#!/usr/bin/env python3
"""
The utils module that defines the functionality
of reading and displaying hyperlinks from a specified
webpage.
"""
import re
import requests
import bs4

__author__ = 'Mariah Holder'
__version__ = 'Dec 2023'
__pylint__ = 'v1.8.3'

def page_hyperlinks(url):
    """
    Returns a string of a formatted HTML document that
    lists all of the hyperlinks in the given webpage.
    """
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, features='html.parser')
    html = _get_starting_html()
    website_regex = re.compile(r'^(http.+)/')

    for link in soup.find_all(href=True):
        if website_regex.match(link['href']):
            html += '<li>'
            html += link['href'].split('//')[1].split('/')[0]
            html += '</li>'

    html += _get_ending_html()
    return html

def _get_starting_html():
    html = '<!DOCTYPE html><html>'
    html += '<head><title>'
    html += 'Hyperlinks from given Page:'
    html += '</title></head>'
    html += '<body><p><h1>'
    html += 'Project 2 CS3280 Mariah Holder - Hyperlinks'
    html += '</h1></p><ul>'
    return html

def _get_ending_html():
    html = '</ul></body>'
    html += '</html>'
    return html
