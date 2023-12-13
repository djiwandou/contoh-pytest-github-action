from src.genap import genap
def test_genap_salah():
    assert not genap(5)

def test_genap_benar():
    assert genap(8)
 