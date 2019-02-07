import json
def test_new_chart(client):
    """Start with a blank database."""
    rv = client.get('/', content_type='application/json')
    print(rv.data())
    assert rv.data() == {}