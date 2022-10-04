def saludar(lang):
	def saludar_es():
		print ("HOLA")
	def saludar_en():
		print ("HI")
	def saludar_fr():
		print ("SALUTED")

	def saludar_pol():
		print("SOY POLACO")
	lang_func = {"es":saludar_es,"en":saludar_en,"fr":saludar_fr
	,"pol":saludar_pol}
	return lang_func[lang]


f = saludar("pol")
f()
