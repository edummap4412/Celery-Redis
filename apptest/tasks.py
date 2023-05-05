from celery import shared_task
import time

from django.core.mail import send_mail


@shared_task(queue='default')
def slow_task():
    print('Started task, processing...')
    time.sleep(120)
    print('Finished Task')
    return True
slow_task.delay()


@shared_task(queue='default') # trocar o nome da exchange
def send_emails(subject, message, recipient_list):
    send_mail(
        subject=subject,
        message=message,
        from_email='qualqueremail@email.com',
        recipient_list = recipient_list,
        fail_silently=False,
    )
