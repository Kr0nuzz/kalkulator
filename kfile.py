from time import sleep
import os

def pilihan():
	print '''
    __ __      ____                     
   / //_/_____/ __ \____  __  __________
  / ,<  / ___/ / / / __ \/ / / /_  /_  /
 / /| |/ /  / /_/ / / / / /_/ / / /_/ /_
/_/ |_/_/   \____/_/ /_/\__,_/ /___/___/
            '''
	sleep(0.7)
	print " Tools	: kalkulator "
	sleep(0.7)
	print " Author	: Kr0nuzz "
	sleep(0.7)
	print " Github	: https://github.com/Kr0nuzz"
	sleep(0.7)
	print "\n"
	print " [1] Tools kalkulator"
	sleep(0.7)
	print " [2] exit"
	p = input("masukkan pilihan>>")
	if p == 1:
		pass
	elif p == 2:
		exit
pilihan()

def kuntal():
	kal = input("masukkan nomor>>")
	print "mau diapakan?"
	sleep(0.7)
	print "[1] ditambah"
	sleep(0.7)
	print "[2] dikurang"
	sleep(0.7)
	print "[3] dikali"
	sleep(0.7)
	print "[4] dibagi"
	kol = input("mau diapakan?")
	ki = input("dengan?")
	if kol == 1:
		print "maka hasil dari", kal, "+", ki, "adalah", kal+ki
	elif kol == 2:
		print "maka hasil dari", kal, "-", ki, "adalah", kal-ki
	elif kol == 3:
		print "maka hasil dari", kal, "x", ki, "adalah", kal*ki
	elif kol == 4:
		print "maka hasil dari", kal, ":", ki, "adalah", kal/ki
	else:
		print "salah memasukkan input"
kuntal()
p = raw_input("tekan enter untuk mengulang")
os.system('clear')

	
while True:
	pilihan()
	kuntal()
	lol = raw_input("tekan enter untuk mengulang")
	os.system('clear')


