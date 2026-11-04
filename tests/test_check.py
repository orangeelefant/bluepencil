"""Tests for scripts/check.py. Standard library only: python3 -m unittest discover tests"""
import contextlib
import io
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import check  # noqa: E402

CASES = [
    ("sv", "Vi levererar alltid skräddarsydda lösningar.", {"absolute", "stock-phrase"}),
    ("sv", "Priset är 99.00 kr för 1 timmar.", {"decimal-point", "plural-error"}),
    ("sv", "## Vill du veta mer?\n\nVi bygger samarbeten, inte engångsuppdrag.", {"question-heading", "not-x-but-y"}),
    ("en", "We always deliver seamless results.", {"absolute", "stock-phrase"}),
    ("en", "Don't hesitate to call. Let's dive into the details.", {"conditional-cta", "warm-up"}),
    ("en", "## Need a website?\n\nWe build partnerships, not projects.", {"question-heading", "not-x-but-y"}),
]


def categories(text, lang):
    return {h[0] for h in check.check(text, lang=lang)[0]}


class CheckTest(unittest.TestCase):
    def test_categories(self):
        for lang, text, expected in CASES:
            with self.subTest(lang=lang, text=text):
                self.assertEqual(categories(text, lang), expected)

    def test_guess_language(self):
        self.assertEqual(check.guess_language(CASES[0][1]), "sv")
        self.assertEqual(check.guess_language(CASES[3][1]), "en")


class CompareTest(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.slop = self._write("slop.md", "Vi levererar alltid skräddarsydda lösningar.\n")
        self.plain = self._write("plain.md", "Vi målar fasader och tak i Västra Götaland.\n")

    def tearDown(self):
        self.dir.cleanup()

    def _write(self, name, text):
        path = os.path.join(self.dir.name, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return path

    def _compare(self, original, proposal):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = check.compare(original, proposal, lang="sv")
        return code, out.getvalue()

    def test_pass_when_hits_drop(self):
        code, out = self._compare(self.slop, self.plain)
        self.assertEqual(code, 0)
        self.assertIn("PASS", out)

    def test_fail_when_hits_rise(self):
        code, out = self._compare(self.plain, self.slop)
        self.assertEqual(code, 1)
        self.assertIn("FAIL\tabsolute\t0 -> 1", out)


if __name__ == "__main__":
    unittest.main()
