import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_lataa_rahaa_lisaa_saldoa(self):
        self.maksukortti.lataa_rahaa(2500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 35.0)

    def test_ota_rahaa_vahentaa_saldoa_kun_rahat_riittavat(self):
        self.maksukortti.ota_rahaa(100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 9)

    def test_ota_rahaa_ei_muuta_saldoa_kun_rahat_eivat_riita(self):
        self.maksukortti.ota_rahaa(1100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_ota_rahaa_palauttaa_tosi_kun_rahat_riittavat(self):
        self.assertTrue(self.maksukortti.ota_rahaa(100))

    def test_ota_rahaa_palauttaa_epatosi_kun_rahat_eivat_riita(self):
        self.assertFalse(self.maksukortti.ota_rahaa(1100))

    def test_maksukortti_tulostuu_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")