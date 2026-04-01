from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyMedicalApp(App):
    def build(self):
        # This is a layout that stacks things vertically
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # Adding a Title
        self.label = Label(text="Welcome to My App", font_size='30sp')
        
        # Adding a Button
        btn = Button(text="Click Me!", size_hint=(1, 0.5), background_color=(0, 0.7, 0.9, 1))
        btn.bind(on_press=self.on_button_click)
        
        layout.add_widget(self.label)
        layout.add_widget(btn)
        
        return layout

    def on_button_click(self, instance):
        self.label.text = "You clicked the button! It works!"

if __name__ == '__main__':
    MyMedicalApp().run()