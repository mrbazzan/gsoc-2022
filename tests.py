import unittest
import subprocess


class TestCommands(unittest.TestCase):
    def test_vigenere_encrypt(self):
        result = subprocess.run(
            ['transpose', 'vigenere', 'transfer10,100', '-c', '--key', 'Hell'],
            capture_output=True
        )
        self.assertIn(b'=XN[<LR_Yux}Xu', result.stdout)

    def test_vigenere_decrypt(self):
        result = subprocess.run(
            ['transpose', 'vigenere', '=XN[<LR_Yux}Xu', '-d', '--key', 'Hell'],
            capture_output=True
        )
        self.assertIn(b'transfer10,100', result.stdout)

    def test_rail_fence_encrypt(self):
        result = subprocess.run(
            ['transpose', 'rail_fence', "WE ARE DISCOVERED. RUN AT ONCE. AT ONCE........", '-c', '--rail', '6'],
            capture_output=True
        )
        self.assertIn(b"WVTC EOEAONE. ACRNNO.. RSEUCT.. EIDREA.. D...", result.stdout)


if __name__ == "__main__":
    unittest.main()
