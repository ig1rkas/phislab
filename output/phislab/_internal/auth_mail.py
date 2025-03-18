import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_auth_mail(user_mail: str, key: str) -> None: 
    print(key)
    # Настройки
    smtp_server = 'smtp.mail.ru'
    smtp_port = 587
    email_from = 'phislab@mail.ru' # Ваш email
    email_password = 'HVCyNvXts94YfrWz6Kes' # Ваш пароль

    # Создаем сообщение
    subject = 'Ваш код подтверждения для регистрации в учетную запись Phislab'
    body = f"""
    Чтобы завершить регистрацию, введите следующий код:
    {key}
    """

    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = user_mail
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Устанавливаем соединение с сервером
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Используем TLS
        server.login(email_from, email_password)  # Логинимся на почте
        server.send_message(msg)  # Отправляем сообщение
        print("Сообщение успешно отправлено!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        server.quit()  # Закрываем соединение


