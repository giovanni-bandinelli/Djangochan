import html,re

def markdown_parser(text):
    # Escape special characters to avoid html injections
    text = html.escape(text)

    #add greentext markdown with '>text line'(should wrap the whole text line in its span class, '>' has to be the first character in the line for this to work)
    #text = re.sub(r'(^|\n)>([^\n]*)', r'\1<span class="greentext">&gt;\2</span>', text)

    #go to new line
    text = text.replace('\n', '<br>')

    #keep track of spaces (perhaps not a good idea?)
    text = text.replace(' ', '&nbsp;')

    #add bold markdown with [b]*words*[/b]
    text = text.replace('[b]', '<b>').replace('[/b]', '</b>')

    #add italic markdown with [i]*words*[/i]
    text = text.replace('[i]', '<i>').replace('[/i]', '</i>')

    #add spoiler markdown with [sp]*words*[/sp]
    text = text.replace('[sp]', '<span class="spoiler">').replace('[/sp]', '</span>')

    

    return text