from pasien import Pasien

class RawatInap(Pasien):
  def __init__ (self, namaLengkap, umur, beratBadan, tinggiBadan, kamar):
    self.namaLengkap = namaLengkap
    self.umur = int(umur)
    self.beratBadan = float(beratBadan)
    self.tinggiBadan = float(tinggiBadan)
    self.kamar = int(kamar)

  def __str__ (self):
    return f"RawatInap(namaLengkap:{self.namaLengkap}, umur:{self.umur}, beratBadan:{self.beratBadan}, tinggiBadan:{self.tinggiBadan}, kamar:{self.kamar})"