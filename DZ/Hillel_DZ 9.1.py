def popular_words(text, words):
    text_1 = text.lower().split()
    my_list = {el: text_1.count(el) for el in words}
    return my_list


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')