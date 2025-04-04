# tgfilestream - A Telegram bot that can stream Telegram files to users over HTTP.
# Copyright (C) 2019 Tulir Asokan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import sys
import os
import argparse

from yarl import URL

from dotenv import load_dotenv

parser = argparse.ArgumentParser(description="A Telegram bot that can stream Telegram files to users over HTTP.")
parser.add_argument("--api-id", type=int, help="Your Telegram API ID")
parser.add_argument("--api-hash", type=str, help="Your Telegram API Hash")
parser.add_argument("--bot-token", type=str, help="Your Telegram Bot Token")
parser.add_argument("--env", type=str, default=".env", help="Path to the environment file (default: .env)")
parser.add_argument("--host", type=str, help="Override the host address")
parser.add_argument("--port", type=int, help="Override the port number")
parser.add_argument("--debug", action="store_true", help="Enable debug mode")
args = parser.parse_args()

load_dotenv(args.env)

try:
    port = args.port or int(os.environ.get("PORT", "8080"))
except ValueError:
    port = -1
if not 1 <= port <= 65535:
    print("Please make sure the PORT environment variable is an integer between 1 and 65535")
    sys.exit(1)

try:
    api_id = args.api_id or int(os.environ["TG_API_ID"])
    api_hash = args.api_hash or os.environ["TG_API_HASH"]
except (KeyError, ValueError):
    print("Please set the TG_API_ID and TG_API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

trust_headers = bool(os.environ.get("TRUST_FORWARD_HEADERS"))
host = args.host or os.environ.get("HOST", "localhost")
public_url = URL(os.environ.get("PUBLIC_URL", f"http://{host}:{port}"))

session_name = os.environ.get("TG_SESSION_NAME", "tgfilestream")

log_config = os.environ.get("LOG_CONFIG")
debug = args.debug or bool(os.environ.get("DEBUG"))

try:
    # The per-user ongoing request limit
    request_limit = int(os.environ.get("REQUEST_LIMIT", "5"))
except ValueError:
    print("Please make sure the REQUEST_LIMIT environment variable is an integer")
    sys.exit(1)

try:
    # The per-DC connection limit
    connection_limit = int(os.environ.get("CONNECTION_LIMIT", "20"))
except ValueError:
    print("Please make sure the CONNECTION_LIMIT environment variable is an integer")
    sys.exit(1)


start_message = os.environ.get("TG_START_MESG", "Send an image or file to get a link to download it")
group_chat_message = os.environ.get("TG_G_C_MESG", "Sorry. But, I only work in private.")

tg_bot_token = args.bot_token or os.environ.get("TG_BOT_FATHER_TOKEN", None)
