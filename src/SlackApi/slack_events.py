


def message_logger(message, logger, next):
    logger.info("MESSAGE LOGGER")
    logger.info(message)
    next()


def update_home_tab(client, event, logger):
    try:
        client.views_publish(
            user_id=event["user"],
            view={
                "type": "home",
                "callback_id": "home_view",
                "blocks":[
                    {
                        "type": "section",
                        "text":{
                            "type": "mrkdwn",
                            "text": "Here's your home view!",
                        }
                    },
                    {"type": "divider"},
                    {"type": "section", "text": {"type": "mrkdwn", "text": "Here is a button that will do things"}},
                    {"type":"actions",
                     "elements":[
                         {"type": "button",
                          "action_id": "button_abc",
                          "text":{
                              "type":"plain_text",
                              "text":"Click Me"
                          }}
                     ]}

                ]
            }
        )
    except Exception as e:
        logger.exception(f"Error publishing home tab: {e}")


def app_mention_handler(body, say, logger):
    logger.info(body)
    user = body.get("event").get("user")
    logger.info(user)
    say(f"Hello <@{user}>, seems like you need something from me!")

