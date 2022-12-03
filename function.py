# def heading_two(text):
#     '''
#     This is html h2 tag
#     :param text:any kind of string
#     :return: h2
#     '''
#     html = f' <h2>{text}</h2>'
#     return html
#
# data = heading_two('This is Md Rashedul')
# print(data)
# data = heading_two('This is also Md Rashedul')
# print(data)

def html_tag(text, html_tag):
    """
    retun for html tag.
    :param text: text
    :param html_tag:
    :return: html tag
    """
    html = f'<{html_tag}>{text}</{html_tag}>'
    return html


print(html_tag('thcvc cf fbbffbfbb','h2'))
