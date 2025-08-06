# test dosyaları test_ ile başlamalı.
# test fonksiyon test_ ile başlamalı.
# test sonuçları "assert" keywordu ile tanımlanmalı
from main import toplama
import pytest

# decorator, annotation
@pytest.mark.parametrize(
        "a,b,expected",
        [
            #a b expected
            (1,2,3),
            (5,5,10),
            (3,5,8)
        ]
) #Aynı testi istediğim kadar farklı parametre ile çalıştırmaya.
def test_toplama(a,b,expected):
    result = toplama(a,b)
    assert result == expected

@pytest.mark.skip(reason="Bu test bu sprintte devre dışı bırakılmıştır.") # Testi atlamak.
def test_cikarma():
    assert 5-3 == 2