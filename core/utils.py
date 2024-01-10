import html, re

def markdown_parser(text):

    # Escape special characters to avoid html injections
    text = html.escape(text)

    #Keep track of spaces (doing it first to avoid problems with other matkdowns)
    text = text.replace(' ', '&nbsp;')

    # Add greentext markdown, now searching for the escaped version of >
    text = re.sub(r'(^|\n)&gt;([^\n]*)', r'\1<span class ="greentxt">&gt;\2</span>', text)
    
    # Go to new line
    text = text.replace('\n', '<br>')

    # Add bold markdown with [b]*words*[/b]
    text = text.replace('[b]', '<b>').replace('[/b]', '</b>')

    # Add italic markdown with [i]*words*[/i]
    text = text.replace('[i]', '<i>').replace('[/i]', '</i>')

    # Add spoiler markdown with [sp]*words*[/sp]
    text = text.replace('[sp]', '<span class="spoiler">').replace('[/sp]', '</span>')

    return text