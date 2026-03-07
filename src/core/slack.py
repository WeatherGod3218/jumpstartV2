import json

from logging import getLogger, Logger

from slack_sdk.web.async_client import AsyncWebClient
from slack_sdk.errors import SlackApiError

from config import SLACK_API_TOKEN, SLACK_JUMPSTART_MESSAGE, SLACK_DM_TEMPLATE


logger: Logger = getLogger(__name__)

client: AsyncWebClient = AsyncWebClient(token=SLACK_API_TOKEN)

announcements: list[str] = []


async def gather_emojis() -> dict:

    logger.info("Gathering emojis from slack!")
    
    try:
        emoji_request: dict = await client.emoji_list()
        assert emoji_request.get("ok", False)

        return emoji_request.get("emoji", {})
    except Exception as e:
        logger.error(f"Error gathering emojis: {e}")
    
    return {}


async def request_upload_via_dm(user_id: str, announcement_text: str) -> None:

    logger.info("Requesting upload announcement permission!")

    try:
        message: dict = SLACK_DM_TEMPLATE.copy()
        
        message[0]["text"]["text"] += announcement_text
        message[1]["elements"][0]["value"] = {"text": announcement_text, "user": user_id}

        await client.chat_postMessage(channel=user_id, text=SLACK_JUMPSTART_MESSAGE, blocks=message)
    except Exception as e:
        logger.error(f"Error messaging user {user_id}: {e}")


def convert_user_response_to_bool(message: str) -> bool:

    user_response: bool = False

    try:
        message_data: dict = json.loads(message)

        user_response = message_data.get("actions", []).get(0, {}).get("action_id", "no_j") == "yes_j"
    except Exception as e:
        logger.error(f"Failed to parse data: {e}")

    return user_response


def get_announcement() -> str | None:
    return announcements.pop(0)


def add_announcement(announcement_text: str) -> None:
    announcements.append(announcement_text)