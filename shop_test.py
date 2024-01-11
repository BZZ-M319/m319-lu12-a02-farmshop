import shop
from article import Article


def test_class():
    """
    tests the class definition
    """
    article = Article('Kuhfladen', 99.45, 7)
    content = article.__repr__()
    assert content == 'Article(name=\'Kuhfladen\', price=99.45, stock=7)'


def test_list(monkeypatch, capsys):
    """
    tests the list of articles
    """
    inputs = iter(['Ei', '0.75', '30', 'Käse', '45.95', '7', 'Ei', '-4', 'Käse', '-1', 'Exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    article_list = shop.main().__repr__()
    assert article_list == '[Article(name=\'Ei\', price=0.75, stock=26), Article(name=\'Käse\', price=45.95, stock=6)]'


def test_output(monkeypatch, capsys):
    """
    tests the output
    """
    inputs = iter(['Ei', '0.75', '30', 'Käse', '45.95', '7', 'Ei', '-4', 'Käse', '-1', 'Exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    shop.main()
    captured = capsys.readouterr()
    assert captured.out == 'Bestand     : 30\nBestand     : 7\n'
