from python_template.main import hello_world


async def test_hello_world():
    assert await hello_world() == "Hello, World!"
