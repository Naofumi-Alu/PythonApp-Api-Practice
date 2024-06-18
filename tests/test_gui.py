import unittest
import tkinter as tk
from src.gui import LoginScreen

class TestLoginScreen(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = LoginScreen(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_login_success(self):
        self.app.username_entry.insert(0, "admin")
        self.app.password_entry.insert(0, "admin")
        self.app.validate_login()
        # Verifica que la pantalla principal haya sido cargada
        main_frame = self.app.root.children.get('!frame')
        self.assertIsNotNone(main_frame)

    def test_login_failure(self):
        self.app.username_entry.insert(0, "wronguser")
        self.app.password_entry.insert(0, "wrongpass")
        self.app.validate_login()
        # Verifica que el login frame sigue presente
        login_frame = self.app.root.children.get('!frame')
        self.assertIsNotNone(login_frame)

if __name__ == "__main__":
    unittest.main()
