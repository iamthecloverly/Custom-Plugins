#Author: Box In A Box [TG: @Box-Boi ]

import math
from userge import Message, userge
from userge.utils import runcmd

@userge.on_cmd(
    "dump",
    about={
        "header": "Android Firmware Dumping Tool",
        "description": "Dumps Android Firmwares To GitHub Publicly!",
        "usage": " {tr}dump (firmware link)",
        "examples": ["{tr}dump http://bigota.d.miui.com/V11.0.2.0.NCFCNXM/mido_images_V11.0.2.0.NCFCNXM_20191107.0000.00_7.0_cn_07679911aa.tgz"],
    },
)
async def dump_(message: Message):
    await message.edit("**Dumping File Publicly To GitHub, Dump Will Be Found On @boxdumps**")
    reply = message.reply_to_message
    reply_id = reply.message_id if reply else None
    resource = message.input_str
    await message.edit(
        "<code>{}</code>".format((await runcmd("bash dump.sh " + resource))[0]),
        parse_mode="html",
    )
