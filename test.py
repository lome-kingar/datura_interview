import task


def test_word_count():
    expected = {'hello': 2, 'world': 2, 'this': 1, 'is': 1, 'a': 1, 'sample': 1, 'text': 1, 'file': 1, 'python': 1}
    actual = task.word_count('''Hello world!\nThis is a sample text file.\n Hello Python world.''')
    assert expected == actual
