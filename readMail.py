from gtts import gTTS
import imaplib
import email

# user dan password email
user = 'tryagainpraba@gmail.com'
password = 'jangancobacoba'

# access dan login gmail
url = 'imap.gmail.com'
con = imaplib.IMAP4_SSL(url)
con.login(user, password)


# mendapatkan body dari email
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)


# mendapatkan email dengan id/num
# 'RFC822' standar format apra internet text message
# mengembalikan email yang diinginkan
def get_email(num):
    result, data = con.fetch(num, 'RFC822')
    return data


def save_speech(self):
    con.select('INBOX')
    # mencari email yang belum terbaca
    result, data = con.search(None, 'UNSEEN')
    # mendapatkan id email terakhir belum terbaca
    mail_ids = data[0]
    print(mail_ids)
    if not mail_ids.decode("utf-8"):
        # jika tidak ada email belum terbaca, mengembalikan nilai 1
        return 1
    else:
        id_list = mail_ids.split()

        latest_email_id = bytes(id_list[-1])
        print(latest_email_id)

        # mendapatkan email dengan id email terakhir belum terbaca
        msgs = (get_email(latest_email_id))
        # mendapatkan body/pesan dari email
        body = get_body(email.message_from_bytes(msgs[0][1])).decode("utf-8")
        # mendapatkan email
        origin = email.message_from_string(msgs[0][1].decode("utf-8"))
        # membaca nama pengirim
        dari = gTTS('dari ' + origin['From'], lang='id')
        # membaca subjek email
        if not origin['Subject']:
            subjek = gTTS('subjek kosong', lang='id')
        else:
            subjek = gTTS('subjek ' + origin['Subject'], lang='id')
        # membaca pesan
        tts = gTTS('pesannya adalah ' + body, lang='id')
        # menyimpan gtts
        dari.save('dari.mp3')
        subjek.save('subjek.mp3')
        tts.save('speech.mp3')

        self.m_text1.AppendText(origin['From'])
        self.m_text2.AppendText(origin['Subject'])
        self.m_text3.AppendText(body)

        return 0
