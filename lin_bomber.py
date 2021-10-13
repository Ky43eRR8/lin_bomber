import requests
import services

green     = '\033[92m'
cyan      = '\033[95m'
bold      = '\033[1m'
underline = '\033[4m'
end       = '\033[0m'
red       = '\033[91m'

print(f"{green}{bold}\t\t{underline}[SMS BOMBER]{end}")

print()
print(f"{bold}coded by{end}", end="")
print(f"{green}{bold} >> {end}", end="")
print(f"{cyan}{bold}avencores{end}")

print(f"{bold}telegram{end}", end="")
print(f"{green}{bold} >> {end}", end="")
print(f"{cyan}{bold}@hzfnews{end}")
print()

print('Введите номер без префиксов или с префиксом (+7) (8)\nПример: 9006002255')
input_number = input(green + bold + ">> " + end)
print('Cколько смс отправить?')
sms = int(input(green + bold + ">> " + end))

print(f"Ты нуждаешься в{cyan} Tor {end}y/n? ")
is_tor = input(bold + green + ">> " + end)


def parse_number(number):
	msg = f"[*]Проверка номера - {green}{bold}OK{end}"
	if len(number) in (10, 11, 12):
		if number[0] == "8":
			number = number[1:]
			print(msg)
		elif number[:2] == "+7":
			number = number[2:]
			print(msg)
		elif int(len(number)) == 10 and number[0] == 9:
			print(msg)
	else:
		print(f"[*]Проверка номера - {red}{bold}Неправильный номер!{end}\nЭтот бомбер предназначен только для России, и если введенный вами номер принадлежит другой стране, то, увы, этот бомбер вам не подходит!")
		quit()
	return number
number = parse_number(input_number)

if str(is_tor) == "y":
        print(f"[*]Запуск {cyan}{bold}Tor{end}...")
        proxies = {
            'http': 'socks5://139.59.53.105:1080',
            'https': 'socks5://139.59.53.105:1080'
        }
        tor = requests.get('http://icanhazip.com/', proxies=proxies).text
        tor = (tor.replace('\n', ''))
        print(f"[*]launch {cyan}{bold}Tor{end} - {green}{bold}OK{end}")

services.attack(number, sms)
