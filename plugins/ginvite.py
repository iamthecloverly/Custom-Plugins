#Author: Box In A Box [TG: @Box-Boi ]

import math
from userge import Message, userge
from userge.utils import runcmd

@userge.on_cmd(
    "ginvite",
    about={
        "header": "GitHub Invite Tool",
        "description": "Invites Users To Private GitHub Repos!",
        "usage": " {tr}ginvite (github-username) (github-repo)",
        "examples": ["{tr}ginvite boxboi689 xiaomi_ginkgo_dump"],
    },
)
async def ginvite_(message: Message):
    await message.edit("**Inviting User To Mentioned Private Repo....**")
    reply = message.reply_to_message
    reply_id = reply.message_id if reply else None
    resource = message.input_str
    await message.edit(
        "<code>{}</code>".format((await runcmd("bash invite.sh " +'"'resource'"'))[0]),
        parse_mode="html",
    )
