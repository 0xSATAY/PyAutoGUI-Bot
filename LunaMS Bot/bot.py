import pyautogui
import time
from AutoHotPy import AutoHotPy

keep_run = False
maple_window_box = None
bloody_storm_duration = 7

def leftButton(autohotpy,event):
    """
    This function simulates a left click
    """
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_LEFT_BUTTON_DOWN
    autohotpy.sendToDefaultMouse(stroke)
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_LEFT_BUTTON_UP
    autohotpy.sendToDefaultMouse(stroke)

def active_window():
    '''
    Make maplelegends the active window
    '''
    print("Finding LunaMS Window...")
    try:
        maple_window = pyautogui.getWindowsWithTitle("Luna")[0]
        print("LunaMS Window Found...")
    except:
        print("Cannot Find LunaMS Window... Program Terminating")
        exit(1)


    if maple_window.isActive == False:
        pyautogui.click("taskbaricon.PNG")

    pyautogui.click(maple_window.box)



    print("LunaMS Window Activation Successful")

def get_window_coordinates():
    maple_window = pyautogui.getWindowsWithTitle("Luna")[0]
    return maple_window.box


def logout(maple_window_box):
    while True:
        if not pyautogui.locateOnScreen("escape_menu.PNG", region=maple_window_box):
            pyautogui.press("esc")
        time.sleep(1)
        if pyautogui.locateOnScreen("logout.PNG", region=maple_window_box):
            pyautogui.click("logout.PNG")

        if pyautogui.locateOnScreen("home_screen.PNG", region=maple_window_box):
            break

def bot(autohotpy, event):
    global keep_run

    for j in range(1):
        if keep_run:
            time.sleep(1)
            autohotpy.D.press()
            time.sleep(3)
            autohotpy.F.press()
            time.sleep(2)
        if keep_run:
            for i in range(10):
                start_time = time.time()
                while time.time()-start_time < bloody_storm_duration:
                    bloody_storm(autohotpy, event)
                    autohotpy.Z.press()
                autohotpy.sleep(1)
                start_time = time.time()
                while time.time()-start_time < 0.8:
                    if keep_run:
                        autohotpy.LEFT_ARROW.press()
                        autohotpy.Z.press()
                start_time = time.time()
                while time.time()-start_time < bloody_storm_duration:
                    bloody_storm(autohotpy, event)
                    autohotpy.Z.press()
                start_time = time.time()
                while time.time()-start_time < 0.8:
                    if keep_run:
                        autohotpy.RIGHT_ARROW.press()
                        autohotpy.Z.press()
        if keep_run:
            sell_full_eq(autohotpy, event)
            # time.sleep(3)
            # start_time = time.time()
            # while time.time()-start_time < 3:
            #     if keep_run:
            #         autohotpy.LEFT_ARROW.press()
            #         autohotpy.Z.press()
            # while time.time()-start_time < 0.8:
            #     if keep_run:
            #         autohotpy.RIGHT_ARROW.press()
            #         autohotpy.Z.press()

    if keep_run:
        autohotpy.run(bot, event)



def bloody_storm(autohotpy, event):
    global keep_run
    if keep_run:
        autohotpy.X.press()

def blade_fury(autohotpy,event):
    global keep_run
    if keep_run:
        autohotpy.V.press()

def exitAutoHotKey(autohotpy,event):
    """
    exit the program when you press ESC
    """
    global keep_run
    keep_run = False
    autohotpy.stop() #makes the program finish successfully. This is the right way to stop it


def enableDisableLoopAttack(autohotpy, event):
    global keep_run

    if keep_run:
        print("Bot Disabled")
        keep_run = False
    else:
        # let's enable it, and then we call it for the first time, so it starts running as soon as possible
        keep_run = True
        print("Bot Enabled")
        bot(autohotpy, event)


def sell_full_eq(autohotpy, event):
    global maple_window_box
    print("SELLING EQUIPS")
    autohotpy.DASH.press()
    if pyautogui.locateOnScreen("cashtabicon.PNG", region=maple_window_box):
        pyautogui.click("cashtabicon.PNG")
        time.sleep(1)
        if pyautogui.locateOnScreen("miumiuicon.PNG", region=maple_window_box):
            pyautogui.click("miumiuicon.PNG", clicks=2)
            time.sleep(2)
            autohotpy.moveMouseToPosition(pyautogui.locateOnScreen("equipstoreicon.PNG", region=maple_window_box).left+69,pyautogui.locateOnScreen("equipstoreicon.PNG", region=maple_window_box).top+38)
            time.sleep(1)
            start_time = time.time()
            while time.time()-start_time < 45:
                pyautogui.click(clicks=2)
                autohotpy.ENTER.press()
            time.sleep(2)
            if pyautogui.locateOnScreen("leaveshopbutton.PNG", region=maple_window_box):
                pyautogui.click("leaveshopbutton.PNG", clicks=1)
                time.sleep(1)
                clearbb(autohotpy, event)
                autohotpy.TAB.press()
    else:
        print("NOT FOUND")

def npc_sell_eq_from_fm(autohotpy, event):
    global maple_window_box
    print("NPC SELLING EQUIPS")
    pyautogui.press("enter")
    pyautogui.write("@fm")
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(10)
    pyautogui.press("enter")
    pyautogui.write("@npc")
    pyautogui.press("enter")
    time.sleep(1)
    for i in range(9):
        pyautogui.press("down")
        time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(1)
    for i in range(4):
        pyautogui.press("down")
        time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    for i in range(100):
        pyautogui.press("down")
    pyautogui.press("enter")
    time.sleep(1)
    clearbb(autohotpy, event)
    start_time = time.time()
    while time.time() - start_time < 1.5:
        autohotpy.LEFT_ARROW.press()
        autohotpy.Z.press()
    autohotpy.UP_ARROW.press()

def clearbb(autohotpy, event):
    pyautogui.press("enter")
    pyautogui.write("@clearbb")
    pyautogui.press("enter")
    pyautogui.press("enter")

#############################################################
# end of functions

#############################################################

if __name__ == '__main__':
    # pyautogui.displayMousePosition()
    auto = AutoHotPy()
    active_window() # Activates MapleLegends window
    maple_window_box = get_window_coordinates()
    hours = 3600
    auto.registerExit(auto.F12, exitAutoHotKey)
    auto.registerForKeyDown(auto.F1,enableDisableLoopAttack)
    auto.registerForKeyDown(auto.F2,sell_full_eq)
    auto.registerForKeyDown(auto.F3,npc_sell_eq_from_fm)
    auto.start()
