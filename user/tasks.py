from django.conf import settings
from django.template.loader import render_to_string

from betterself_backend.celery import app
from common.mail import send_mail


@app.task(queue='heleot_main')
def new_subscribe_list_mail(recipients):
    title = 'Welcome on BetterSelf!'
    msg_html = render_to_string('new_subscribe_mail.html')
    msg_html = msg_html.strip().replace('\n', '')
    send_mail(title, title, settings.EMAIL_HOST_USER, recipients, html_message=msg_html)
