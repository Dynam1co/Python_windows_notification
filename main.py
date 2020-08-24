from win10toast import ToastNotifier

if __name__ == "__main__":
    toaster = ToastNotifier()

    toaster.show_toast(
        "Hello World!!!",
        "Notificación de 10 segundos con Python",
        icon_path="python_icon.ico",
        duration=10
    )
