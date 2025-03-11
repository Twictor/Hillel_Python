import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    clean_text = ""
    in_tag = False

    for char in html:
        if char == '<':
            in_tag = True
        elif char == '>':
            in_tag = False
        elif not in_tag:
            clean_text += char

    clean_lines = [line.strip() for line in clean_text.split('\n') if line.strip()]
    final_text = '\n'.join(clean_lines)

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(final_text)


delete_html_tags('draft.html')
