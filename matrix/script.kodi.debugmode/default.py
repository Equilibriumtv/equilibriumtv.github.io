
from kodi_six import xbmc, xbmcaddon, xbmcgui


def run():
    op_names = ["1 - Toggle Debug", "2 - Log Uploader"]
    op = xbmcgui.Dialog().select("Select an option", op_names)
    if op == 0:
        xbmc.executebuiltin("ToggleDebug")
        xbmcgui.Dialog().notification(
                "Debug",
                "Toggle Debug",
                xbmcgui.NOTIFICATION_INFO,
                5000
            )
    elif op == 1:
        addon_log = 'script.kodi.loguploader'
        xbmc.executebuiltin('RunAddon({0})'.format(addon_log))      



if __name__ == '__main__':
    run()
