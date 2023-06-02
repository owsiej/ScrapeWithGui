def set_dpi():
    try:
        import ctypes

        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass
