# v2 - Legitimate
def extract_bold_texts(html_text):
    res = []
    curr_str = ''
    while len(html_text) > 0:
        if html_text.startswith('<b>'):
            html_text = html_text[3:]
            curr_str = html_text.split('</b>')[0]
            html_text = html_text[len(curr_str):]
        elif html_text.startswith('</b>'):
            html_text = html_text[4:]
            res.append(curr_str)
            curr_str = ''
        # Just in case the last <b> has no closure.
        elif len(html_text) > 3:
            html_text = html_text[1:]
        else:
            break

    return res


print(extract_bold_texts('<b>ABC</b> abc <b>def 123 </b><b></b>0000'))
print(extract_bold_texts('A piece of text without tags.'))

# v1 method
import re


def extract_bold_texts_v1(html_text):
    return re.findall("<b>(.*?)</b>", html_text)


print(extract_bold_texts_v1('<b>ABC</b> abc <b>def 123 </b><b></b>0000'))
print(extract_bold_texts_v1('A piece of text without tags.'))