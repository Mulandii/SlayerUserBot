from slayerbot import CMD_HELP
from slayerbot.utils import slayer_on_cmd, sudo_cmd


@slayer.on(sudo_cmd(pattern="ahelp ?(.*)", allow_sudo=True))
@slayer.on(slayer_on_cmd(pattern="ahelp ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(f"Here is some help for the {CMD_HELP[args]}")
        else:
            await event.edit(
                f"Help string for {args} not found! Type `.help` to see valid module names."
            )
    else:
        string = ""
        for i in CMD_HELP.values():
            string += f"`{str(i[0])}`, "
        string = string[:-2]
        await event.edit(
            "Please specify which module you want help for!\n\n" f"{string}"
        )
