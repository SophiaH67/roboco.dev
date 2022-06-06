from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from invites.decorators import create_invite_code


def send_invite_accepted_email(user, inviter):
    context = {
        "user": user,
        "inviter": inviter,
    }

    html_message = render_to_string("invites/invite_accepted_email_body.html", context)
    plain_message = strip_tags(html_message)

    send_mail(
        f"{inviter.username} has accepted your invitation",
        plain_message,
        "robosa@roboco.dev",
        [inviter.email],
        fail_silently=False,
        html_message=html_message,
    )


def send_user_registered_email(user):
    context = {
        "user": user,
    }

    html_message = render_to_string("invites/user_registered_email_body.html", context)
    plain_message = strip_tags(html_message)

    send_mail(
        f"Welcome to Roboco, {user.username}",
        plain_message,
        "robosa@roboco.dev",
        [user.email],
        fail_silently=False,
        html_message=html_message,
    )


def send_invite_email(inviter, email):
    context = {
        "invite_link": f"https://roboco.dev/register/?invite={create_invite_code(inviter, email)}",
        "inviter": inviter,
    }

    html_message = render_to_string("invites/invite_email_body.html", context)
    plain_message = strip_tags(html_message)

    send_mail(
        "Invitation to join",
        plain_message,
        "robosa@roboco.dev",
        [email],
        fail_silently=False,
        html_message=html_message,
    )
