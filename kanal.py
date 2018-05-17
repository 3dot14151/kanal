# -*- coding: utf-8 -*-

# НАЗВАНИЕ БОТА: Принимаем оплату через сайт
# ОПИСАНИЕ БОТА: Принимаем оплату через сайт
# АВТОР БОТА   : Купинов Вадим
# ТЕЛЕГРАММ АВТОРА : @Pi_3dot141 (https://t.me/Pi_3dot141)

import telebot
import sqlite3
import random
import time
import random

from telebot import types
from pyCoinPayments import CryptoPayments

API_KEY     = '966b22a978f7944c9d533d48a218c21a965aeddc752aa665aa3212f28c31de47'
API_SECRET  = '9B451aEcFafc37e7ee54b30f962f7282b4f089F993581d99cBb5e864c357c7ac'
IPN_URL     = 'www.3dot14.ru'


def print_massage (message,status):
    ### настройка цвета для вывода на экран
    c0  =  "\033[0;37m"  ## Белый
    c1  =  "\033[1;30m"  ## Черный
    c2  =  "\033[0;31m"  ## Красный
    c3  =  "\033[0;32m"  ## Зеленый
    c4  =  "\033[1;35m"  ## Magenta like Mimosa\033[1;m
    c5  =  "\033[1;33m"  ## Yellow like Yolk\033[1;m'
    c7  =  "\033[1;37m"  ## White
    c8  =  "\033[1;33m"  ## Yellow
    c9  =  "\033[1;32m"  ## Green
    c10 =  "\033[1;34m"  ## Blue
    c11 =  "\033[1;36m"  ## Cyan
    c12 =  "\033[1;31m"  ## Red
    c13 =  "\033[1;35m"  ## Magenta
    c14 =  "\033[1;30m"  ## Black
    c15 =  "\033[0;37m"  ## Darkwhite
    c16 =  "\033[0;33m"  ## Darkyellow
    c17 =  "\033[0;32m"  ## Darkgreen
    c18 =  "\033[0;34m"  ## Darkblue
    c19 =  "\033[0;36m"  ## Darkcyan
    c20 =  "\033[0;31m"  ## Darkred
    c21 =  "\033[0;35m"  ## Darkmagenta
    c22 =  "\033[0;30m"  ## Darkblack
    c23 =  "\033[0;0m"   ## Off
    name_program = 'courier'
    if status == '[s]':
        print ( c0+'[+] Старт программы: '+c8+message+c0)
    if status == '[+]':
        print ( c9+'[+] '+c0+message+c0)
    if status == '[!]':
        print (c12+'[!] '+c0+message+c0)

def load_staus (user_id):
    conn = sqlite3.connect("user.sqlite")
    cursor = conn.cursor()
    sql = "select id,user_id,status from user where user_id = '"+str(user_id)+"'"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        id,user_id,status = row
    return status

def load__FIO (user_id):
    conn = sqlite3.connect("user.sqlite")
    cursor = conn.cursor()
    sql = "select id,user_id,username,first_name,last_name from user where user_id = '"+str(user_id)+"'"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        id,user_id,username,first_name,last_name = row
    return username,first_name,last_name



def save_FIO    (user_id,username,first_name,last_name):
    conn = sqlite3.connect("user.sqlite")
    cursor = conn.cursor()
    sql = "UPDATE user SET username = '"+str(username)+"' WHERE user_id = '"+str(user_id)+"' "
    cursor.execute(sql)
    conn.commit()
    sql = "UPDATE user SET first_name = '"+str(first_name)+"' WHERE user_id = '"+str(user_id)+"' "
    cursor.execute(sql)
    conn.commit()
    sql = "UPDATE user SET last_name = '"+str(last_name)+"' WHERE user_id = '"+str(user_id)+"' "
    cursor.execute(sql)
    conn.commit()



def save_status (user_id,username,status):
    label = 'no'
    conn = sqlite3.connect("user.sqlite")
    cursor = conn.cursor()
    sql = "select id,user_id from user where user_id = '"+str(user_id)+"'"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        id,user_id = row
        label = 'yes'
    if label == 'no':
        cursor = conn.cursor()
        a = [str(user_id),str(username),'','','','','','','','','100',status]
        cursor.execute("INSERT INTO user (user_id,username,name,first_name,last_name,setting01,setting02,setting03,setting04,setting05,setting06,status)VALUES (?,?,?,?,?,?,?,?,?,?,?,?);",a)
        conn.commit()
    else:
        sql = "UPDATE user SET status = '"+str(status)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()

def save_param (user_id,nom,znak):
    conn = sqlite3.connect("user.sqlite")
    cursor = conn.cursor()
    if nom == 1:
        sql = "UPDATE user SET setting01 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 2:
        sql = "UPDATE user SET setting02 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 3:
        sql = "UPDATE user SET setting03 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 4:
        sql = "UPDATE user SET setting04 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 5:
        sql = "UPDATE user SET setting05 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 6:
        sql = "UPDATE user SET setting06 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()

def load_param (user_id,nom):
    conn = sqlite3.connect("user.sqlite")
    cursor = conn.cursor()
    sql = "select id,user_id,setting01,setting02,setting03,setting04,setting05,setting06 from user where user_id = '"+str(user_id)+"'"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        id,user_id,setting01,setting02,setting03,setting04,setting05,setting06 = row
        if nom == 1:
            return setting01
        if nom == 2:
            return setting02
        if nom == 3:
            return setting03
        if nom == 4:
            return setting04
        if nom == 5:
            return setting05
        if nom == 6:
            return setting06


def logsystem (name,title,user_id):
    conn = sqlite3.connect("log.sqlite")
    cursor = conn.cursor()
    timestamp = int(time.time())
    print_massage ('Протокол: USER: ('+str(user_id)+'),ИМ-('+str(name)+'),ЗН-('+str(title)+'),ВР-('+str(timestamp)+')','[+]')
    a = [name,title,user_id,timestamp]
    cursor.execute("INSERT INTO log (name,TITLE,user_id,DT)VALUES (?,?,?,?);",a)
    conn.commit()

if __name__ == "__main__":
    token = '484307717:AAHiXSSTcltwzK-RWcK6mS-fheh9qM-ZXEQ'
    bot   = telebot.TeleBot(token)
    print_massage (' @SecretKanal_bot','[s]')
    print_massage ('Ver 1.0.0, Аvtor: @Pi_3dot141 (https://t.me/Pi_3dot141)','[s]')


def menu_main ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Личный кабинет')
    markup.row('Админка')
    return markup


def menu_send_A ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Меню')
    markup.row('Отправить группе A','Отмена')
    return markup

def menu_send_B ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Меню')
    markup.row('Отправить группе B','Отмена')
    return markup

def menu_balans ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Меню')
    markup.row('Пополнить','Вывести')
    return markup


def menu_ls ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Главное меню')
    markup.row('Тест','Регистрация')
    markup.row('Мои каналы','Счет','Статистика')
    return markup

def menu_my_kanal ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Главное меню')
    markup.row('Список','Добавить')
    return markup

def menu_schet ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Главное меню')
    markup.row('Пополнить')
    return markup

def menu_list ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Главное меню')
    markup.row('Функция 1')
    return markup

def menu_test ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Главное меню')
    markup.row('Личный кабинет')
    markup.row('Функция 2')
    return markup

def menu_admin ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Главное меню')
    markup.row('Пользователи','Статистика')
    return markup

def menu_users ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Главное меню')
    markup.row('Список','Добавить','Поиск')
    return markup

def menu_user1 ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Главное меню')
    markup.row('List-user')
    return markup

def menu_user2 ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Главное меню')
    markup.row('user')
    return markup

def menu_listuser ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Главное меню')
    markup.row('Удалить')
    return markup

def menu_user3 ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Главное меню')
    markup.row('Пополнить счет')
    return markup



def money (amount,currency1,currency2):
    post_params = {'amount' : amount,'currency1' : 'USD','currency2' : currency2 }
    client = CryptoPayments(API_KEY, API_SECRET, IPN_URL)
    transaction = client.createTransaction(post_params)
    message_out = '<b>Сумма пополнения:</b>'+str(transaction.amount)+' '+currency2+'\n'
    message_out = message_out + '<b>Адресс кошелька: </b>'+str(transaction.address)+'\n'
    message_out = message_out + '<b>Ссылка информирования:</b> '+str(transaction.status_url)
    return message_out
    ##bot.send_message(user_id,message_out,parse_mode='HTML')

def sale (user_id):
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    keyboard.add(types.InlineKeyboardButton(text='Bitcoin', callback_data='Bitcoin'),types.InlineKeyboardButton(text='Litecoin', callback_data='Litecoin'),types.InlineKeyboardButton(text='Dogecoin', callback_data='Dogecoin'))
    message_out = 'Выберите вид Валюты'
    keyboard.add(types.InlineKeyboardButton(text='Ether', callback_data='Ether'),types.InlineKeyboardButton(text='Classic', callback_data='Classic'),types.InlineKeyboardButton(text='VERGE', callback_data='VERGE'))
    keyboard.add(types.InlineKeyboardButton(text='NEO', callback_data='NEO'),types.InlineKeyboardButton(text='Qtum', callback_data='Qtum'),types.InlineKeyboardButton(text='NEM', callback_data='NEM'))
    keyboard.add(types.InlineKeyboardButton(text='Monero', callback_data='Monero'))
    bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=keyboard)


def send_m (sim,user_id):
        message_out = 'Отправка сообщения группе '+sim
        markup = menu_main ()
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)
        conn = sqlite3.connect("user.sqlite")
        cursor = conn.cursor()
        sql = "select id,user_id,status from user where 1=1 "
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            id_v,user_id_v,status_v = row
            grup = load_param (user_id_v,1)
            if grup == sim:


                label_send = ''
                try:
                    message_out = load_param (user_id,3)
                    bot.send_message(user_id_v,message_out,parse_mode='HTML')
                    label_send = 'Сообщение отправлено: '
                except:
                    pass
                    label_send = 'Сообщение не отправлено: '


                username_v,first_name_v,last_name_v = load__FIO (user_id_v)

                message_out = label_send + str(user_id_v)+'\nЛогин: '+username_v+'\nИмя: '+first_name_v+'\nФамилия: '+last_name_v
                bot.send_message(user_id,message_out,parse_mode='HTML')




@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if 1==1:
        username   = message.from_user.username
        first_name = message.from_user.first_name
        last_name  = message.from_user.last_name
        user_id    = message.from_user.id
        date       = message.date
        message_in = message.text
        logsystem  ('message',str(message_in),str(user_id))
        save_status (user_id,username,'start')
        save_FIO    (user_id,username,first_name,last_name)

        #save_param (user_id,1,'')
        #save_param (user_id,2,'')
        #save_param (user_id,3,'')
        #save_param (user_id,4,'')
        #save_param (user_id,5,'')
        ##message_out = 'Добрый день! \n'+first_name+','+last_name+','+username+'\n'
        message_out = 'Добрый день! \n'
        message_out = message_out + 'Вы подписались на новости компании'
        markup = menu_main ()
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    user_id    = message.from_user.id
    message_in = message.text
    username   = message.from_user.username
    first_name = message.from_user.first_name
    last_name  = message.from_user.last_name
    date       = message.date
    logsystem  ('message',str(message_in),str(user_id))
    status     = load_staus (user_id)


    if 'Пополнить' == message_in:
        markup = menu_schet ()
        message_out = 'Ваш баланс'
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)
        sale (user_id)



    if 'Пользователи' == message_in:
        markup = menu_users ()

        message_out = 'Список пользователей'
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)
        conn = sqlite3.connect("user.sqlite")

        cursor = conn.cursor()
        sql = "select id,user_id,status from user where 1=1 "
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            id_v,user_id_v,status_v = row
            grup = load_param (user_id_v,1)

            username_v,first_name_v,last_name_v = load__FIO (user_id)
            message_out = 'Пользователь с id: '+str(user_id_v)+'\nЛогин: '+username_v+'\nИмя: '+first_name_v+'\nФамилия: '+last_name_v+'\n'

            labelm = ''
            if grup == 'B':
                message_out = message_out + ' в группе B'
                labelm = 'B'
                keyboard = types.InlineKeyboardMarkup(row_width=1)
                keyboard.add(types.InlineKeyboardButton(text='Перевести в группу Нет группы', callback_data='goB_'+str(user_id_v)))
                bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=keyboard)
            if grup == 'A':
                labelm = 'A'
                message_out = message_out + ' в группе A'
                keyboard = types.InlineKeyboardMarkup(row_width=1)
                keyboard.add(types.InlineKeyboardButton(text='Перевести в группу  B', callback_data='goA_'+str(user_id_v)))
                bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=keyboard)

            if labelm == '':
                message_out = message_out + ' в группе Нет группы'
                keyboard = types.InlineKeyboardMarkup(row_width=1)
                keyboard.add(types.InlineKeyboardButton(text='Перевести в группу A', callback_data='goNo_'+str(user_id_v)))
                bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=keyboard)



    if 'Мои каналы' == message_in:
        markup = menu_my_kanal ()
        message_out = 'Мои каналы'
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)

    if 'Счет' == message_in:
        markup = menu_schet ()
        message_out = 'Счет'
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)

    if 'Статистика' == message_in:
        markup = menu_ls ()
        message_out = 'Статистика'
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)


    if 'Регистрация' == message_in:
        markup = menu_ls ()
        message_out = 'Регистрация'
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)

    if 'Личный кабинет' == message_in:
        markup = menu_ls ()
        message_out = 'Личный кабинет'
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)

    if 'Тест' == message_in:
        markup = menu_test ()
        message_out = 'Тест'
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)

    if 'Админка' == message_in:
        markup = menu_admin ()
        message_out = 'Админка'
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)

    if 'Список' == message_in:
        markup = menu_list ()
        message_out = 'Список'
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)




    if 'Отправить группе B' == message_in:
        send_m ('B',user_id)

    if 'Отправить группе A' == message_in:
        send_m ('A',user_id)

    if 'Отмена' == message_in:
        message_out = 'Отмена сообщения'
        markup = menu_main ()
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)


    if 'Главное меню' == message_in:
        message_out = 'Главное меню'
        markup = menu_main ()
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)



    if status.find ('testA') != -1:
        message_out = 'Получено новое сообщение группы A'
        markup = menu_send_A ()
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)
        save_status (user_id,username,'')
        save_param (user_id,3,message_in)

    if status.find ('testB') != -1:
        message_out = 'Получено новое сообщение для группы B'
        markup = menu_send_B ()
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)
        save_status (user_id,username,'')
        save_param (user_id,3,message_in)

    if '=> Группа A' == message_in:
        message_out = 'Введите сообшение для отправки группе A'
        markup = menu_main ()
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)
        save_status (user_id,username,'testA')
        label = 'yes'

    if '=> Группа B' == message_in:
        message_out = 'Введите сообшение для отправки группе B'
        markup = menu_main ()
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)
        save_status (user_id,username,'testB')
        label = 'yes'

    if message_in == 'Админка2':
        message_out = 'Список пользователей'
        bot.send_message(user_id,message_out,parse_mode='HTML')
        conn = sqlite3.connect("user.sqlite")

        cursor = conn.cursor()
        sql = "select id,user_id,status from user where 1=1 "
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            id_v,user_id_v,status_v = row
            grup = load_param (user_id_v,1)

            username_v,first_name_v,last_name_v = load__FIO (user_id)
            message_out = 'Пользователь с id: '+str(user_id_v)+'\nЛогин: '+username_v+'\nИмя: '+first_name_v+'\nФамилия: '+last_name_v+'\n'

            labelm = ''
            if grup == 'B':
                message_out = message_out + ' в группе B'
                labelm = 'B'
                keyboard = types.InlineKeyboardMarkup(row_width=1)
                keyboard.add(types.InlineKeyboardButton(text='Перевести в группу Нет группы', callback_data='goB_'+str(user_id_v)))
                bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=keyboard)

            if grup == 'A':
                labelm = 'A'
                message_out = message_out + ' в группе A'
                keyboard = types.InlineKeyboardMarkup(row_width=1)
                keyboard.add(types.InlineKeyboardButton(text='Перевести в группу  B', callback_data='goA_'+str(user_id_v)))
                bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=keyboard)

            if labelm == '':
                message_out = message_out + ' в группе Нет группы'
                keyboard = types.InlineKeyboardMarkup(row_width=1)
                keyboard.add(types.InlineKeyboardButton(text='Перевести в группу A', callback_data='goNo_'+str(user_id_v)))
                bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=keyboard)


    if message_in == 'Оплата':
        message_out = 'Ваш баланс составляет:\nПодписка действует до'
        bot.send_message(user_id,message_out,parse_mode='HTML')
        save_status (user_id,username,'q01')
        sale (user_id)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
   if call.message:
        user_id = call.message.chat.id
        if call.data.find ("goA") != -1:
            find_user_id = call.data.replace('goA_','')
            save_param (find_user_id,1,'B')
            message_out = 'Пользователь с id: '+str(find_user_id)+' Переведен в группу B: '
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            keyboard.add(types.InlineKeyboardButton(text='Перевести в группу Нет группы', callback_data='goB_'+str(find_user_id)))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,reply_markup=keyboard,parse_mode='HTML')

        if call.data.find ("goB") != -1:
            find_user_id = call.data.replace('goB_','')
            save_param (find_user_id,1,'No')
            message_out = 'Пользователь с id: '+str(find_user_id)+' Переведен в группу  Нет группы '
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            keyboard.add(types.InlineKeyboardButton(text='Перевести в группу A', callback_data='goNo_'+str(find_user_id)))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,reply_markup=keyboard,parse_mode='HTML')


        if call.data.find ("goNo") != -1:
            find_user_id = call.data.replace('goNo_','')
            save_param (find_user_id,1,'A')
            message_out = 'Пользователь с id: '+str(find_user_id)+' Переведен в группу A: '
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            keyboard.add(types.InlineKeyboardButton(text='Перевести в группу B', callback_data='goA_'+str(find_user_id)))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,reply_markup=keyboard,parse_mode='HTML')


        if call.data.find ('Bitcoin') != -1:
            message_out = money (10,'USD','BTC')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')
        if call.data.find ('Litecoin') != -1:
            message_out = money (10,'USD','LTC')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')
        if call.data.find ('Dogecoin') != -1:
            message_out = money (10,'USD','DOGE')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')
        if call.data.find ('Ether' ) != -1:
            message_out = money (10,'USD','ETC')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')
        if call.data.find ('Classic') != -1:
            message_out = money (10,'USD','ETC')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')
        if call.data.find ('NEO' ) != -1:
            message_out = money (10,'USD','NEO')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')
        if call.data.find ('Qtum') != -1:
            message_out = money (10,'USD','QTUM')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')
        if call.data.find ('NEM') != -1:
            message_out = money (10,'USD','XEM')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')
        if call.data.find ('Monero') != -1:
            message_out = money (10,'USD','XMR')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')
        if call.data.find ('VERGE') != -1:
            message_out = money (10,'USD','XVG')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')




bot.polling()











