"""
Compatibility patches for running this Django 5.0.1 codebase on Python 3.14.

Django 5.0.1 predates Python 3.14 and relies on a `copy.copy(super())` trick
in a couple of places that Python 3.14 changed the internals of `super`
proxy objects enough to break. Rather than editing Django's installed
source (which would be silently undone on every `pip install`/reinstall),
we monkeypatch the specific broken methods here, at app startup, with a
version-independent equivalent that produces identical results.

Safe to remove once this project upgrades to a Django version with native
Python 3.14 support (Django 5.2+ / 6.0+ fixed this upstream).
"""
import sys


def _safe_context_copy(self):
    """
    Drop-in replacement for django.template.context.BaseContext.__copy__.

    Original implementation:
        def __copy__(self):
            duplicate = copy(super())
            duplicate.dicts = self.dicts[:]
            return duplicate

    `copy(super())` relied on CPython internals of `super` proxy objects
    that changed in Python 3.14, raising:
        AttributeError: 'super' object has no attribute 'dicts' and no
        __dict__ for setting new attributes

    This does the same thing (a shallow copy of the instance, with `dicts`
    independently copied so mutating one doesn't affect the other) without
    going through `super()` at all.
    """
    duplicate = self.__class__.__new__(self.__class__)
    duplicate.__dict__.update(self.__dict__)
    duplicate.dicts = self.dicts[:]
    return duplicate


def apply():
    if sys.version_info < (3, 14):
        return

    from django.template.context import BaseContext
    BaseContext.__copy__ = _safe_context_copy
