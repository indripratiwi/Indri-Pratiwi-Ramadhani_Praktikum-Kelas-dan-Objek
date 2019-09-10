class KelilingLingkaran(object):
	def __init__(self, phi, r):
		self.phi = phi
		self.jarijari = r
	def hitungKeliling(self):
		return 2 * self.phi * self.jarijari

def main():
	lingkaran1 = KelilingLingkaran(3.14, 15)

	print("\nKELILING LINGKARAN")
	print("\nObjek keliling lingkaran 1")
	print("Phi\t\t= ", lingkaran1.phi)
	print("Jari-jari\t= ", lingkaran1.jarijari)
	print("Keliling\t= ", lingkaran1.hitungKeliling())

	lingkaran2 = KelilingLingkaran(3.14, 12)

	print("\nObjek keliling lingkaran 2")
	print("Phi\t\t= ", lingkaran2.phi)
	print("Jari-jari\t= ", lingkaran2.jarijari)
	print("Keliling\t= ", lingkaran2.hitungKeliling())

if __name__ == "__main__":
	main()

class LuasLingkaran(object):
	def __init__(self, phi, r):
		self.phi = phi
		self.jarijari = r
	def hitungLuas(self):
		return self.phi * self.jarijari * self.jarijari

def main():
	lingkaran1 = LuasLingkaran(3.14, 5)

	print("\n\nLUAS LINGKARAN")
	print("\nObjek luas lingkaran 1")
	print("Phi\t\t= ", lingkaran1.phi)
	print("Jari-jari\t= ", lingkaran1.jarijari)
	print("Luas\t\t= ", lingkaran1.hitungLuas())

	lingkaran2 = LuasLingkaran(3.14, 10)

	print("\nObjek luas lingkaran 2")
	print("Phi\t\t= ", lingkaran2.phi)
	print("Jari-Jari\t= ", lingkaran2.jarijari)
	print("Luas\t\t= ", lingkaran2.hitungLuas())

if __name__ == "__main__":
	main()
