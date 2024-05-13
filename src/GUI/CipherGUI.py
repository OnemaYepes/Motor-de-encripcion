import sys
sys.path.append("src")
from CipherEngine.CipherEngine import CipherEngine, EmptyTextError, EmptyKeyError, KeyCharacterError, LongerKeyError

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

Window.clearcolor = '#181818'

class CipherApp(App):
    def build(self):
        
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        self.title_label = Label(text="Motor de Encripción",
                                 font_name = 'Calibri',
                                 font_size=50,
                                 color = '00FF00'
                                 )
        self.layout.add_widget(self.title_label)

        self.menu_label = Label(text="Seleccione una opción:",
                                font_size=20,
                                bold = True,
                                color = '00FF00')
        self.layout.add_widget(self.menu_label)

        self.encrypt_button = Button(text="Encriptar texto",
                                     color = '#181818',
                                     font_size = 22,
                                     bold = True,
                                     size_hint = (1,0.5),
                                     background_color = '00FF00',
                                     background_normal = '',
                                     on_press=self.encrypt_text)
        self.layout.add_widget(self.encrypt_button)

        self.decrypt_button = Button(text="Desencriptar texto",
                                     color = '#181818',
                                     font_size = 22,
                                     bold = True,
                                     size_hint = (1,0.5),
                                     background_color = '#FF7000',
                                     background_normal = '',
                                     on_press=self.decrypt_text)
        self.layout.add_widget(self.decrypt_button)

        return self.layout

    def encrypt_text(self, instance):
        self.layout.clear_widgets()

        self.label = Label(text="Ingrese el Texto a Encriptar:",
                           font_size=20,
                           size_hint=(1,0.3),
                           bold = True,
                           color = '00FF00')
        self.layout.add_widget(self.label)

        self.text_input = TextInput(font_size=20,
                                    background_color = '00FF00',
                                    background_normal='',
                                    size_hint=(1,0.5),
                                    multiline=True)
        self.layout.add_widget(self.text_input)

        self.label = Label(text="Ingrese la Clave de Encriptación:",
                           font_size=20,
                           size_hint=(1,0.3),
                           bold = True,
                           color = '00FF00')
        self.layout.add_widget(self.label)

        self.key_input = TextInput(font_size=20,
                                    background_color = '00FF00',
                                    background_normal='',
                                    size_hint=(1,0.5),
                                    multiline=False)
        self.layout.add_widget(self.key_input)

        self.result = TextInput(hint_text="Aquí saldrá el resultado",
                                    font_size=25,
                                    foreground_color = '#D5FF00',
                                    hint_text_color = "#D5FF00",
                                    readonly=True,
                                    halign='center',
                                    background_color = '#201c1c',
                                    size_hint=(1,0.5),
                                    multiline=True
                                    )
        self.layout.add_widget(self.result)

        self.encrypt_button = Button(text="Encriptar",
                                     color = '00FF00',
                                     font_size = 22,
                                     bold = True,
                                     size_hint = (1,0.5),
                                     background_color = '#395539',
                                     background_normal = '',
                                     on_press=self.encrypt)
        self.layout.add_widget(self.encrypt_button)

        self.back_button = Button(text="[u]Volver al menú principal[/u]",
                                     color = "#BC68FF",
                                     background_color = '#181818',
                                     background_normal = '',
                                     markup=True,
                                     size_hint = (1,0.2),
                                     on_press=self.back_to_main_menu)
        self.layout.add_widget(self.back_button)

    def decrypt_text(self, instance):
        self.layout.clear_widgets()

        self.label = Label(text="Ingrese el Texto Encriptado:",
                           font_size=20,
                           size_hint=(1,0.3),
                           bold = True,
                           color = '#FF7000')
        self.layout.add_widget(self.label)

        self.text_input = TextInput(font_size=20,
                                    background_color = '#FF7000',
                                    background_normal='',
                                    size_hint=(1,0.5),
                                    multiline=True)
        self.layout.add_widget(self.text_input)

        self.label = Label(text="Ingrese la Clave para Desencriptar:",
                           font_size=20,
                           size_hint=(1,0.3),
                           bold = True,
                           color = '#FF7000')
        self.layout.add_widget(self.label)

        self.key_input = TextInput(font_size=20,
                                    background_color = '#FF7000',
                                    background_normal='',
                                    size_hint=(1,0.5),
                                    multiline=False)
        self.layout.add_widget(self.key_input)

        self.result = TextInput(hint_text="Aquí saldrá el resultado",
                                font_size=25,
                                foreground_color = '#D5FF00',
                                hint_text_color = "#D5FF00",
                                readonly=True,
                                halign='center',
                                background_color = '#201c1c',
                                size_hint=(1,0.5),
                                multiline=True
                                )
        self.layout.add_widget(self.result)

        self.encrypt_button = Button(text="Desencriptar",
                                     color = '#FF7000',
                                     font_size = 22,
                                     bold = True,
                                     size_hint = (1,0.5),
                                     background_color = '#6F3000',
                                     background_normal = '',
                                     on_press=self.decrypt)
        self.layout.add_widget(self.encrypt_button)

        self.back_button = Button(text="[u]Volver al menú principal[/u]",
                                     color = "#BC68FF",
                                     background_color = '#181818',
                                     background_normal = '',
                                     markup=True,
                                     size_hint = (1,0.2),
                                     on_press=self.back_to_main_menu)
        self.layout.add_widget(self.back_button)

    def encrypt(self, instance):
        text = self.text_input.text
        key = self.key_input.text
        try:
            encrypted_text = CipherEngine.EncryptText(text, key)
            self.result.text = f"Texto encriptado:\n{encrypted_text}"
        except (EmptyTextError, EmptyKeyError, KeyCharacterError, LongerKeyError) as e:
            self.result.text = "Error: " + str(e)
        except Exception as e:
            self.result.text = "Error inesperado: " + str(e)

    def decrypt(self, instance):
        encrypted_text = self.text_input.text
        key = self.key_input.text
        try:
            decrypted_text = CipherEngine.DecryptText(str(encrypted_text), str(key))
            self.result.text = f"Texto desencriptado:\n{decrypted_text}"
        except (EmptyTextError, EmptyKeyError, KeyCharacterError, LongerKeyError) as e:
            self.result.text = "Error: " + str(e)
        except Exception as e:
            self.result.text = "Error inesperado: " + str(e)

    def back_to_main_menu(self, instance):
        self.layout.clear_widgets()

        title_label = Label(text="Motor de Encripción",
                            font_name='Calibri',
                            font_size=50,
                            color='00FF00')
        self.layout.add_widget(title_label)

        menu_label = Label(text="Seleccione una opción:",
                          font_size=20, bold=True,
                          color='00FF00')
        self.layout.add_widget(menu_label)

        encrypt_button = Button(text="Encriptar texto",
                                color='#181818',
                                font_size=22,
                                bold=True,
                                size_hint=(1, 0.5),
                                background_color='00FF00',
                                background_normal='',
                                on_press=self.encrypt_text)
        self.layout.add_widget(encrypt_button)

        decrypt_button = Button(text="Desencriptar texto",
                                color='#181818',
                                font_size=22,
                                bold=True,
                                size_hint=(1, 0.5),
                                background_color='#FF7000',
                                background_normal='',
                                on_press=self.decrypt_text)
        self.layout.add_widget(decrypt_button)

if __name__ == "__main__":
    CipherApp().run()