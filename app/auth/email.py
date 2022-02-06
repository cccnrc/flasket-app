from flask import render_template, current_app
from app.email import send_email, send_email_local

def send_password_reset_email(user):
    token = user.get_jwt_token()
    SUBJECT = '[Flasket] Reset Your Password'
    RECIPIENTS = [user.email]
    TEMPLATE_TXT = 'email/reset_password.txt'
    TEMPLATE_HTML = 'email/reset_password.html'
    ### if running in local use my SMTP server, otherwise use AWS SES
    if current_app.config['LOCAL_DEVELOPMENT']:
        send_email_local(SUBJECT,
                           sender=current_app.config['ADMINS'][0],
                           recipients=RECIPIENTS,
                           text_body=render_template(TEMPLATE_TXT, user=user, token=token),
                           html_body=render_template(TEMPLATE_HTML, user=user, token=token))
    else:
        send_email(SUBJECT,
                       recipients=RECIPIENTS,
                       text_body=render_template(TEMPLATE_TXT, user=user, token=token),
                       html_body=render_template(TEMPLATE_HTML, user=user, token=token))

def send_activation_email(user):
    token = user.get_jwt_token()
    SUBJECT = '[Flasket] Confirm Your Mail'
    RECIPIENTS = [user.email]
    TEMPLATE_TXT = 'email/activate.txt'
    TEMPLATE_HTML = 'email/activate.html'
    ### if running in local use my SMTP server, otherwise use AWS SES
    if current_app.config['LOCAL_DEVELOPMENT']:
        send_email_local(SUBJECT,
                           sender=current_app.config['ADMINS'][0],
                           recipients = RECIPIENTS,
                           text_body=render_template(TEMPLATE_TXT, user=user, token=token),
                           html_body=render_template(TEMPLATE_HTML, user=user, token=token))
    else:
        send_email(SUBJECT,
                        recipients=RECIPIENTS,
                        text_body=render_template(TEMPLATE_TXT, user=user, token=token),
                        html_body=render_template(TEMPLATE_HTML, user=user, token=token))
