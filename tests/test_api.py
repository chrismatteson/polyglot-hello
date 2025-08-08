import json
import pathlib

import pytest

from polyglot_hello import (
    get_by_code,
    get_by_index,
    list_languages,
    random_greeting,
    say_hello,
    say_hello_world,
    search,
)


data_path = pathlib.Path(__file__).parents[1] / "src" / "polyglot_hello" / "data" / "greetings.json"


def test_dataset_min_size():
    data = json.loads(data_path.read_text(encoding="utf-8"))
    assert len(data) >= 200


def test_basic_resolution_by_code():
    assert say_hello_world("en").lower().startswith("hello")
    g = get_by_code("fr")
    assert g.name.lower().startswith("french")


def test_basic_resolution_by_name():
    hello_es = say_hello("Spanish")
    assert "hola" in hello_es.lower()


def test_resolution_by_index_and_bounds():
    langs = list_languages()
    _ = say_hello_world(0)
    with pytest.raises(IndexError):
        get_by_index(len(langs))


def test_random_and_search():
    g = random_greeting()
    assert isinstance(g.hello, str) and g.hello
    results = search("hola")
    assert any(r.name.lower().startswith("spanish") for r in results)


