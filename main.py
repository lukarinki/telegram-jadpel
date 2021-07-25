import datetime
import requests
import schedule
import time
import os
from ini_token import API

#JADWAL PELAJARAN
jadwal_pelajaran = {
    #Sensor
}

# memperlihatkan Jam
jam = datetime.datetime.now().strftime("%X")
print (jam)
a = "hello world"

def test(x):
    print (x)

# while False:
#     jam = datetime.datetime.now().strftime("%Z")
#     print (jam)
#     if jam == "20:18:00":
#         senin1 = telegram_bot_sendtext(senin1)
#         print (senin1)

def telegram_bot_sendtext(bot_message):    
    bot_token = API
    bot_chatID = '-1001569089101'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()
    
#SENIN
schedule.every().monday.at("07:30").do(telegram_bot_sendtext, jadwal_pelajaran["senin1"]) #B. Jepang
schedule.every().monday.at("07:30").do(test, "! B.Jepang DONE !")

schedule.every().monday.at("09:00").do(telegram_bot_sendtext, jadwal_pelajaran["senin2"]) #Kimia
schedule.every().monday.at("09:00").do(test, "! Kimia DONE !")

schedule.every().monday.at("10:45").do(telegram_bot_sendtext, jadwal_pelajaran["senin3"]) #PKN
schedule.every().monday.at("10:45").do(test, "! PKN DONE !")

schedule.every().monday.at("11:30").do(telegram_bot_sendtext, jadwal_pelajaran["senin4"]) #B. Sunda
schedule.every().monday.at("11:30").do(test, "! B. Sunda DONE !")
#SELASA
schedule.every().tuesday.at("07:30").do(telegram_bot_sendtext, jadwal_pelajaran["selasa1"]) #B. Indonesia
schedule.every().tuesday.at("07:30").do(test, "! B. Indonesia DONE !")

schedule.every().tuesday.at("09:00").do(telegram_bot_sendtext, jadwal_pelajaran["selasa2"]) #MTK
schedule.every().tuesday.at("09:00").do(test, "! MTK DONE !")

schedule.every().tuesday.at("10:45").do(telegram_bot_sendtext, jadwal_pelajaran["selasa3"]) #AGAMA
schedule.every().tuesday.at("10:45").do(test, "! AGAMA DONE !")
#RABU
schedule.every().wednesday.at("07:30").do(telegram_bot_sendtext, jadwal_pelajaran["rabu1"]) #EC 1
schedule.every().wednesday.at("07:30").do(test, "! EC 1 DONE !")

schedule.every().wednesday.at("08:15").do(telegram_bot_sendtext, jadwal_pelajaran["rabu2"]) #PKWU
schedule.every().wednesday.at("08:15").do(test, "! PKWU DONE !")

schedule.every().wednesday.at("09:00").do(telegram_bot_sendtext, jadwal_pelajaran["rabu3"]) #Penjaskes
schedule.every().wednesday.at("09:00").do(test, "! Penjaskes DONE !")

schedule.every().wednesday.at("10:45").do(telegram_bot_sendtext, jadwal_pelajaran["rabu4"]) #MTK
schedule.every().wednesday.at("10:45").do(test, "! MTK DONE !")
#KAMIS
schedule.every().thursday.at("07:30").do(telegram_bot_sendtext, jadwal_pelajaran["kamis1"]) #Fisika
schedule.every().thursday.at("07:30").do(test, "! Fisika DONE !")

schedule.every().thursday.at("09:00").do(telegram_bot_sendtext, jadwal_pelajaran["kamis2"]) #B. Inggris
schedule.every().thursday.at("09:00").do(test, "! B. Inggris DONE !")

schedule.every().thursday.at("09:45").do(telegram_bot_sendtext, jadwal_pelajaran["kamis3"]) #Sejarah
schedule.every().thursday.at("09:45").do(test, "! Sejarah DONE !")

schedule.every().thursday.at("10:45").do(telegram_bot_sendtext, jadwal_pelajaran["kamis4"]) #B. Inggris
schedule.every().thursday.at("10:45").do(test, "! B. Inggris DONE !")

#JUMAT
schedule.every().friday.at("07:30").do(telegram_bot_sendtext, jadwal_pelajaran["jumat1"]) #Biologi 
schedule.every().friday.at("07:30").do(test, "! Biologi DONE !")

schedule.every().friday.at("09:00").do(telegram_bot_sendtext, jadwal_pelajaran["jumat2"]) #BP 1
schedule.every().friday.at("09:00").do(test, "! BP 1 DONE !")

schedule.every().friday.at("09:45").do(telegram_bot_sendtext, jadwal_pelajaran["jumat3"]) #Seni
schedule.every().friday.at("09:45").do(test, "! Seni DONE !")


#schedule.every().sunday.at("11:16").do(test('hola')) #testing
#test("hola")
# schedule.every().hour.at(":19").do(telegram_bot_sendtext)
# print(senin1)
# senin1 = telegram_bot_sendtext(senin1)


while True:
    schedule.run_pending()
    time.sleep(1)

# https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
