class Pasien:
  def __init__(self, namaLengkap, umur, beratBadan, tinggiBadan):
    self.namaLengkap = namaLengkap
    self.umur = int(umur)
    self.beratBadan = float(beratBadan)
    self.tinggiBadan = float(tinggiBadan)

  def __str__ (self):
    return f"Pasien(namaLengkap:{self.namaLengkap}, umur:{self.umur}, beratBadan:{self.beratBadan}, tinggiBadan:{self.tinggiBadan})"