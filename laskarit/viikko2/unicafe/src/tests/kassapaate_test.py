import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_konstruktori_asettaa_myydyt_oikein(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_syo_maukkaasti_kateisella_kasvattaa_saldoa_kun_rahat_riittavat(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004)

    def test_syo_edullisesti_kateisella_kasvattaa_saldoa_kun_rahat_riittavat(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)

    def test_syo_maukkaasti_kateisella_palauttaa_rahat_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_syo_edullisesti_kateisella_palauttaa_rahat_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)
    
    def test_syo_maukkaasti_kateisella_kasvattaa_myytyja(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_syo_edullisesti_kateisella_kasvattaa_myytyja(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kateisella_ei_muuta_rahamaaraa_kun_rahat_eivat_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(50)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_syo_maukkaasti_kateisella_ei_muuta_rahamaaraa_kun_rahat_eivat_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(50)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_syo_edullisesti_kateisella_palauttaa_kaikki_rahat_kun_rahat_eivat_riita(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(50), 50)

    def test_syo_maukkaasti_kateisella_palauttaa_kaikki_rahat_kun_rahat_eivat_riita(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(50), 50)

    def test_syo_maukkaasti_kateisella_ei_muuta_myytyja_kun_rahat_eivat_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(50)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_edullisesti_kateisella_ei_muuta_myytyja_kun_rahat_eivat_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(50)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_edullisesti_kortilla_vahentaa_saldoa_kun_rahat_riittavat(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.6)

    def test_syo_maukkaasti_kortilla_vahentaa_saldoa_kun_rahat_riittavat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo_euroina(), 6)

    def test_syo_edullisesti_kortilla_palauttaa_tosi_kun_rahat_riittavat(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))

    def test_syo_maukkaasti_kortilla_palauttaa_tosi_kun_rahat_riittavat(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
    
    def test_syo_edullisesti_kortilla_kasvattaa_myytyja_kun_rahat_riittavat(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukkaasti_kortilla_kasvattaa_myytyja_kun_rahat_riittavat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_edullisesti_kortilla_ei_vahenna_saldoa_kun_rahat_eivat_riita(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo_euroina(), 1)

    def test_syo_maukkaasti_kortilla_ei_vahenna_saldoa_kun_rahat_eivat_riita(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo_euroina(), 1)

    def test_syo_edullisesti_kortilla_ei_kasvata_myytyja_kun_rahat_eivat_riita(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_syo_maukkaasti_kortilla_ei_kasvata_myytyja_kun_rahat_eivat_riita(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_edullisesti_kortilla_palauttaa_epatosi_kun_rahat_eivat_riita(self):
        kortti = Maksukortti(100)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(kortti))

    def test_syo_maukkaasti_kortilla_palauttaa_epatosi_kun_rahat_eivat_riita(self):
        kortti = Maksukortti(100)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(kortti))
    
    def test_kortilla_ostaminen_ei_muuta_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_lataa_rahaa_kortille_kasvattaa_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1001)

    def test_lataa_rahaa_kortille_kasvattaa_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 11)

    def test_lataa_rahaa_kortille_ei_tee_mitaan_kun_summa_on_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)