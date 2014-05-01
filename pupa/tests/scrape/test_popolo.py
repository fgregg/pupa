import pytest
from pupa.scrape import Person, Organization, Membership
from validictory import ValidationError


def test_basic_invalid_person():
    """ Test that we can create an invalid person, and validation will fail """
    bob = Person("Bob B. Johnson")
    bob.add_source(url='foo')
    bob.validate()

    bob.name = None

    with pytest.raises(ValidationError):
        bob.validate()


def test_str():
    """ test __str__ method """
    assert str(Person("Bob B. Johnson")) == "Bob B. Johnson"


def test_magic_methods():
    """ Test the magic methods work """
    bob = Person("John Q. Public, Esq.",
                 gender="male", image="http://example.com/john.jpg",
                 summary="Some person")
    bob.add_source(url='foo')
    bob.validate()

    bob.add_name("Thiston", note="What my friends call me")

    assert bob.other_names == [
        {"name": "Thiston",
         "note": "What my friends call me"}
    ]

    bob.add_name("Johnseph Q. Publico",
                 note="Birth name",
                 start_date="1920-01",
                 end_date="1949-12-31")

    assert bob.other_names == [
        {"name": "Thiston",
         "note": "What my friends call me"},
        {"name": "Johnseph Q. Publico",
         "note": "Birth name",
         "start_date": "1920-01",
         "end_date": "1949-12-31"}
    ]


def test_basic_invalid_organization():
    """ Make sure we can make an invalid orga """
    orga = Organization("name")
    orga.add_source(url='foo')
    orga.validate()

    orga.name = None

    with pytest.raises(ValidationError):
        orga.validate()


def test_add_post():
    """ Test that we can hack posts in on the fly'"""
    orga = Organization("name")
    orga.add_source(url='foo')
    orga.validate()

    orga.add_post("Human Readable Name", "Chef")

    assert orga._related[0].role == "Chef"
    assert orga._related[0].label == "Human Readable Name"

    with pytest.raises(TypeError):
        orga.add_identifier("id10t", foo="bar")

    orga.add_identifier("id10t")
    orga.add_identifier("l0l", scheme="kruft")

    assert orga.identifiers[-1]['scheme'] == "kruft"
    assert orga.identifiers[0]['identifier'] == "id10t"
    assert not hasattr(orga.identifiers[0], "scheme")


def test_basic_invalid_membership():
    """ Make sure that we can create an invalid membership and break """
    membership = Membership("person_id", "orga_id")
    membership.validate()

    membership.person_id = 33
    with pytest.raises(ValueError):
        membership.validate()