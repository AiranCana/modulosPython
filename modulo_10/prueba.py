
def verif(lista: list[str], character: str) -> bool:
	if len(lista) != 0:
		x = lista.pop()
		if x == character:
			return True
		else:
			return False
	else:
		return False

def funtiones(hola: str) -> bool:
	if not isinstance(hola, str):
		return False
	lista: list[str]  = []
	tem = ''
	for n in range(hola):
		if n in ('{', '[', '('):
			lista.append(hola[n])
		if n == '}':
			if not verif(lista, "{"):
				return False
		if n == ')':
			if not verif(lista, "("):
				return False
		if n == ']':
			if not verif(lista, "["):
				return False
	if len(lista) == 0:
		return True
	else:
		return False