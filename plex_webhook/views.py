from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from discord_webhook import DiscordWebhook
from django.conf import settings
import urllib


def send_plex_webhook_to_discord_webhook(data):
    print(json.dumps(data))
    message = f'{data["Server"]["title"]} '

    event = data["event"]
    if event == "media.resume":
        message += f"{data['Account']['title']} resumed {data['Metadata']['grandparentTitle']} - ||{data['Metadata']['title']}||(S{data['Metadata']['parentIndex']}E{data['Metadata']['index']})"
    elif event == "media.pause":
        message += f"{data['Account']['title']} paused {data['Metadata']['grandparentTitle']} - ||{data['Metadata']['title']}||(S{data['Metadata']['parentIndex']}E{data['Metadata']['index']})"
    elif event == "media.play":
        message += f"{data['Account']['title']} started {data['Metadata']['grandparentTitle']} - ||{data['Metadata']['title']}||(S{data['Metadata']['parentIndex']}E{data['Metadata']['index']})"
    elif event == "media.stop":
        message += f"{data['Account']['title']} stopped {data['Metadata']['grandparentTitle']} - ||{data['Metadata']['title']}||(S{data['Metadata']['parentIndex']}E{data['Metadata']['index']})"
    else:
        print(f"Unknown event: {event}")
        print(json.dumps(data))
        return

    webhook = DiscordWebhook(
        url=settings.DISCORD_WEBHOOK_URL,
        content=message,
    )
    webhook.execute()


@csrf_exempt
def plex_webhook(request):
    # If it's not a post, return a 405
    if request.method != "POST":
        print(f"{request.method} request to plex_webhook")
        return HttpResponse(status=405)

    data = json.loads(request.POST["payload"])

    # Send the data to the discord webhook
    send_plex_webhook_to_discord_webhook(data)

    # Return the data
    return HttpResponse(json.dumps(data))
