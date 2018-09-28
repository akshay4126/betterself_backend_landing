from django.core.mail import send_mail as django_send_mail


def send_mail(subject, message, from_email, recipient_list, fail_silently=False,
              auth_user=None, auth_password=None, connection=None, html_message=None):
    django_send_mail(
        subject, message, from_email, recipient_list, fail_silently,
        auth_user, auth_password, connection, html_message
    )
