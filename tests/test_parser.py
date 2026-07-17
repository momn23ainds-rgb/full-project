
from app.parser import parse_markdown

def test_parser():
    md='# A\ntext\n## B\ntext'
    nodes=parse_markdown(md)
    assert len(nodes)==2
