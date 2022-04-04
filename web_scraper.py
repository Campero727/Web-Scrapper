import keyboard;
from getpass import getuser;

def main():
	banner();
	realizar_scrapping();
	

def banner():
	print("           $           $");
	print("     $    $$           $$    $");
	print("    $$    $$            $$    $$");
	print("    $$   $$             $$    $");
	print("   $$    $$             $$    $$");
	print("   $$    $$    $$$$$    $$    $$");
	print("   $$   $$$   $$$$$$$   $$$   $$");
	print("  $$$   $$$   $$$$$$$   $$$   $$$  Created By: Pirata");
	print("  $$$   $$$   $$$$$$$   $$$   $$$ Web Scrapper");
	print("  $$$   $$$    $$$$$    $$$   $$$");
	print("  $$$    $$$   $$$$$   $$$   $$$$");
	print("   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$");
	print("          $$$$$$$$$$$$$$");
	print("           $$$$$$$$$$$$");
	print("     $$$$$$$$$$$$$$$$$$$$$$$$$");
	print(" $$$$$$$$$$ $$$$$$$$$$$ $$$$$$$$$$");
	print("$$$$   $$$  $$$$$ $$$$$  $$$   $$$$");
	print("$$$    $$$  $$$$$ $$$$$  $$$    $$$");
	print(" $$$   $$$  $$$     $$$  $$$   $$$");
	print(" $$$   $$$  $$$$$ $$$$$  $$$   $$$");
	print("  $$    $$   $$$$ $$$$   $$    $$");
	print("  $$$   $$   $$$$ $$$$   $$   $$$");
	print("   $$    $$   $$$$$$$   $$    $$");
	print("    $$    $    $$$$$    $    $$");
	print("     $     $           $     $");
	print("      $    $           $    $");

def realizar_scrapping():
	url=input("Ingresa la URL del sitio Web");
	ruta=input("Ingresa la ruta para guardar los documentos");
	nombre=input("Ingresa el nombre del documento");
	try:
		data=open(ruta+'data.txt','wb');
		data.write(url.encode()+b'\n');
		data.write(ruta.encode()+b'\n');
		data.write(nombre.encode()+b'\n');
	except:
		print("No se han podido registrar los datos para continuar");

if __name__=='__main__':
	main();