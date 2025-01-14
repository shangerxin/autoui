from autoinsight import Button, Wait, WindowOS, ComboBox


if __name__ == '__main__':
    window = WindowOS()
    control_panel = window.launchApp("control panel")
    control_panel.setCurrent()
    Button("Power Options").click()
    Wait(3)
    Button("Change plan settings").click()
    # 1 2 3 5 10 15 20 25 30 45 1 hours
    ComboBox("Turn off the display on battery").select("15 minutes")
    Button("Save changes").click()
    Wait(3)
    control_panel.close()
