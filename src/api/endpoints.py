from logging import getLogger, Logger

import random
import textwrap
import requests

from fastapi import APIRouter, Query, Form
from fastapi.responses import JSONResponse

from core import slack
from src.core import cshcalendar

logger: Logger = getLogger(__name__)
router: APIRouter = APIRouter()



@router.get("/calendar")
def get_calendar() -> JSONResponse:
	"""
	Returns calendar data.
	"""

	pass


@router.get("/announcement")
def get_announcement() -> JSONResponse:
	"""
	Returns announcement data.
	"""

	pass


@router.get("/harold")
def get_harold() -> JSONResponse:
	"""
	Returns harold data.
	"""

	pass


@router.post("/slack/message_actions")
async def message_actions(payload: str = Form(...)):
	"""
	Handles slack message action.
	"""


	pass


@router.get("/showerthoughts")
def showerthoughts() -> JSONResponse:
	"""
	Returns a random shower thought from the Reddit API.

	Returns:
		JSONResponse: A JSON response containing a random shower thought.
	"""
	
	response: dict = {"data": "No shower thoughts found."}

	try:
		logger.info("Fetching shower thoughts from Reddit API...")

		reddit_data: requests.Response = requests.get(
			"https://www.reddit.com/r/showerthoughts/top.json",
			headers={"User-agent": "Showerthoughtbot 0.1"},
		)

		if len(reddit_data.json()["data"]["children"]) == 0:
			logger.warning("No shower thoughts found in Reddit API response.")
			return JSONResponse(response)
		
		shower_thought: str = textwrap.fill(
			(random.choice(reddit_data.json()["data"]["children"])["data"]["title"]), 50
		)

		response["data"] = shower_thought
	except Exception as e:
		logger.error(f"Error fetching shower thoughts: {e}")
	
	return JSONResponse(response)
