from flask import render_template
from app import current_app
from app.email import send_email, send_email_local

def send_ticket_email(user, ticket, object = 'UPDATE'):
    RECIPIENTS = [user.email]
    if object == 'UPDATE':
        SUBJECT = '[Flasket] Ticket Update'
        TEMPLATE_TXT = 'email/ticket.txt'
        TEMPLATE_HTML = 'email/ticket.html'
    elif object == 'CLOSURE':
        SUBJECT = '[Flasket] Ticket Closure'
        TEMPLATE_TXT = 'email/ticket_closure.txt'
        TEMPLATE_HTML = 'email/ticket_closure.html'
    elif object == 'REOPEN':
        SUBJECT = '[Flasket] Ticket Reopen'
        TEMPLATE_TXT = 'email/ticket_reopen.txt'
        TEMPLATE_HTML = 'email/ticket_reopen.html'
    elif object == 'SUBMIT':
        SUBJECT = '[Flasket] Ticket Submitted'
        TEMPLATE_TXT = 'email/ticket_submit.txt'
        TEMPLATE_HTML = 'email/ticket_submit.html'
    if current_app.config['LOCAL_DEVELOPMENT']:
        send_email_local(SUBJECT,
                           sender=current_app.config['ADMINS'][0],
                           recipients=RECIPIENTS,
                           text_body=render_template(TEMPLATE_TXT, user=user, ticket=ticket),
                           html_body=render_template(TEMPLATE_HTML, user=user, ticket=ticket))
    else:
        send_email(SUBJECT,
                       recipients=RECIPIENTS,
                       text_body=render_template(TEMPLATE_TXT, user=user, ticket=ticket),
                       html_body=render_template(TEMPLATE_HTML, user=user, ticket=ticket))
