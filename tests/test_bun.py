from praktikum.bun import Bun
from data import name_bun, price_bun


class TestBun:

    def test_get_name_bun(self):
        bun = Bun(name_bun, price_bun)
        assert bun.get_name() == name_bun

    def test_get_price_bun(self):
        bun = Bun(name_bun, price_bun)
        assert bun.get_price() == price_bun
