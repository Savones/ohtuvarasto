import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    # laajennus

    def test_negatiivinen_tilavuus_asettaa_nollaksi(self):
        varasto = Varasto(-1)
        self.assertEqual(varasto.tilavuus, 0.0)
    
    def test_saldo_negatiivinen_nollataan(self):
        varasto = Varasto(10, -1)
        self.assertEqual(varasto.saldo, 0.0)
    
    def test_alkusaldo_tilavuutta_suurempi_asettaa_tilavuudeksi(self):
        varasto = Varasto(10, 20)
        self.assertEqual(varasto.saldo, 10)
    
    def test_lisaaminen_alle_nolla_maaralla_palauttaa_none(self):
        self.assertEqual(self.varasto.lisaa_varastoon(-1), None)
    
    def test_lisays_ei_mahdu_varastoon(self):
        self.varasto.lisaa_varastoon(11)
        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)
    
    def test_palauttaa_nolla_jos_ottaa_alle_nolla_maaralla(self):
        self.assertEqual(self.varasto.ota_varastosta(-1), 0.0)
    
    def test_ottaminen_saldoa_suuremmalla_palauttaa_saldon(self):
        self.assertEqual(self.varasto.ota_varastosta(10), 0.0)
    
    def test_str_palauttaa_oikean_arvon(self):
        self.assertEqual(str(self.varasto), f"saldo = {self.varasto.saldo}, vielä tila {self.varasto.paljonko_mahtuu()}")