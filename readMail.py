from gtts import gTTS
import imaplib
import email

user = 'tryagainpraba@gmail.com'
password = 'jangancobacoba'
url = 'imap.gmail.com'
con = imaplib.IMAP4_SSL(url)
con.login(user, password)


def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)


def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    return data


def get_email(num):
    result, data = con.fetch(num, 'RFC822')
    return data


def save_speech():
    con.select('INBOX')
    result, data = con.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()

    latest_email_id = bytes(id_list[-1])

    msgs = (get_email(latest_email_id))

    body = get_body(email.message_from_bytes(msgs[0][1])).decode("utf-8")
    # print(body)
    tts = gTTS(body, lang='id')
    tts.save('speech.mp3')

    # result, data = con.fetch(b'3', 'RFC822')
    # raw = email.message_from_bytes(data[0][1])
    # print(search('FROM', 'verify@twitter.com', con))
    # print(get_body(raw))
    # print(get_email(search('FROM','verify@github.com',con)))
