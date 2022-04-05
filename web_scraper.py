import keyboard;
from getpass import getuser;
import argparse;
import urllib.request

def main():
	banner();
	try:
		parser = argparse.ArgumentParser(description='Manual to this script')
		parser.add_argument('--url', type=str, default = None, help="Url para realizar el web Scrapping");
		parser.add_argument('--dir',type=str, default=None,help="Directorio Para Guardar los archivos");
		parser.add_argument('--fname',type=str, default=None, help="Nombre del archivo HTML y TXT");
		parser.add_argument('--etiqueta', type=str,default=None, help="Etiqueta a buscar");
		args = parser.parse_args()
		if args.url and args.dir:
			if args.fname:
				if args.etiqueta:
					web_scrapper(args.url,args.dir,args.fname,args.etiqueta);
				else:
					web_scrapper(args.url,args.dir,args.fname,"");
			else:
				web_scrapper(args.url,args.dir,'data',"");
				print("Los documentos se guardaran en "+args.dir+" con el nombre data");
		else:
			print("Ingresa los valores para comenzar con el Web Scrapping");
	except:
		print("");
	

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

def web_scrapper(url,directorio,fname,etiqueta):

	dir_html=str(directorio+fname+'.html');
	web=open(dir_html,'wb');
	consulta=urllib.request.urlopen(url);
	consulta=consulta.read();
	web.write(consulta); 
	web.close();
	print("Pagina Clonada En "+directorio);
	
	if etiqueta:
		dir_txt=str(directorio+fname+'.txt');
		txt=open(dir_txt,'wb');
		
		files=open(dir_html,'rb');
		inicio=str('<'+etiqueta+'>');
		fin=str('</'+etiqueta+'>');

		for l in files.readlines():
			l=str(l);
			if inicio in l:
				x=l.find(inicio);
				x=x+len(inicio);
				y=l.find(fin);
				#print(l[x:y]);
				txt.write((l[x:y]+'\n').encode());
		print("Documento de texto con el contenido de las etiqutas <"+etiqueta+'>'+' se encuentran en el directorio '+directorio);

if __name__=='__main__':
	main();