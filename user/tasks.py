from django.conf import settings
from django.template.loader import render_to_string

from betterself_backend.celery import app
from common.mail import send_mail
from user.models import ContactForm


@app.task(queue='betterself_main')
def new_subscribe_list_mail(recipients):
    title = 'Welcome on BetterSelf!'
    msg_html = render_to_string('new_subscribe_mail.html')
    msg_html = msg_html.strip().replace('\n', '')
    send_mail(title, title, settings.EMAIL_HOST_USER, recipients, html_message=msg_html)


@app.task(queue='betterself_main')
def contact_us_admin_mail(contact_form_id):
    contact_form = ContactForm.objects.get(pk=contact_form_id)

    title = 'New \'Contact Us\' request'
    recipients = [settings.ADMIN_EMAIL]
    msg_html = render_to_string('contact_us_admin_mail.html', contact_form.__dict__)
    msg_html = msg_html.strip().replace('\n', '')
    send_mail(title, title, settings.EMAIL_HOST_USER, recipients, html_message=msg_html)
