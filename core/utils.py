import html, re

def markdown_parser(text, board_name, thread_id=None):
    #changing the order of these will break things<---
    print(text)
    if text is None:#shitty fix for empty posts...
        return ""
    # Escape special characters to avoid html injections
    text = html.escape(text)

    # Keep track of spaces(perhaps a bad idea?)
    text = text.replace(' ', '&nbsp;')

    # Add greentext markdown
    text = re.sub(r'(^|\n)&gt;([^\n]*)', r'\1<span class ="greentxt">&gt;\2</span>', text)

    #managing quotelinks:

    # Add hyperlink markdown with >>reply_id
    if thread_id is not None:
        # Case 1: Referenced post is the thread under which the thread is being made or another reply under the same thread
        text = re.sub(r'&gt;&gt;(\d+)', rf'<a class="hyperlink" href="/boards/{board_name}/thread/{thread_id}#p\1">&gt;&gt;\1</a>', text)
    else:
        # Case 2: Referenced post is (or is under) another thread inside the same board
        text = re.sub(r'&gt;&gt;(\d+)', rf'<a class="hyperlink" href="/boards/{board_name}/thread/\1">&gt;&gt;\1</a>', text)

    # Case 3: Referenced post is a thread/reply made in another board
    # Assuming the format is >>>/board_name/thread_id or >>board_name/thread_id#reply_id
    text = re.sub(r'&gt;&gt;&gt;/(\w+)/(\d+)(#p\d+)?', r'<a class="hyperlink" href="/boards/\1/thread/\2\3">&gt;&gt;\1/\2\3</a>', text)


    # Go to new line
    text = text.replace('\n', '<br>')

    # Add bold markdown with *words*
    text = re.sub(r'(?<!\*)\*(.*?)\*(?!\*)', r'<b>\1</b>', text)

    # Add italic markdown with _words_
    text = re.sub(r'(?<!_)_(.*?)(?<!\\)_(?!_)', r'<i>\1</i>', text)

    # Add spoiler markdown with ||words||
    text = re.sub(r'(?<!\\)\|\|(.*?)\|\|(?!\\)', r'<span class="spoiler">\1</span>', text)



    return text