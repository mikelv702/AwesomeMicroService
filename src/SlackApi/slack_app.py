import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import logging

from .slack_events import update_home_tab, message_logger, app_mention_handler
from .slack_actions import button_ack
logging.basicConfig(level=logging.INFO)


app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)
app.event("app_home_opened")(update_home_tab)
app.event(event="app_mention",middleware=[message_logger])(app_mention_handler)
app.action("button_abc")(button_ack)

# Ready? Start your app!
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
