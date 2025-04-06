import os
import unittest
from astrometapy.readers import fits_reader

class TestFitsReader(unittest.TestCase):
    
    def setUp(self):
        # Create a temporary FITS file for testing.
        from astropy.io import fits
        self.test_file = "test.fits"
        hdu = fits.PrimaryHDU()
        hdu.header['RA'] = 123.45
        hdu.header['DEC'] = 67.89
        hdu.header['DATE-OBS'] = '2025-01-01'
        hdu.writeto(self.test_file, overwrite=True)
    
    def tearDown(self):
        # Clean up the temporary file.
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_load_fits_header(self):
        header = fits_reader.load_fits_header(self.test_file)
        self.assertIn('RA', header)
        self.assertIn('DEC', header)
        self.assertIn('DATE-OBS', header)
        self.assertEqual(header['RA'], 123.45)

if __name__ == "__main__":
    unittest.main()
