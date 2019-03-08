from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.lang import Builder
from os import listdir

Window.size = (1200,800)

kv_path = './widgets/'
for kv in listdir(kv_path):
	if(kv[-3:]==".kv"):
		with open(kv_path+kv, encoding='utf8') as archivoWidget: 	#Se abre el archivo para poder leer acentos y caracteres UTF-8,
			Builder.load_string(archivoWidget.read())				#si se abre con la herramienta de Kivy estos no se visualizan.

class TabManager(TabbedPanel):
	pass
	
class EditLayout(StackLayout):
	pass
	
class ConfigLayout(StackLayout):
	pass
	
class tab(TabbedPanelHeader):
	pass

class flowideApp(App):
	layout=TabManager()
	editLayout=EditLayout()
	configLayout=ConfigLayout()
	
	def build(self):
		edit=TabbedPanelHeader(text="Edit")
		self.layout.add_widget(edit)
		edit.content=self.editLayout
		
		edit=TabbedPanelHeader(text="Configuration")
		self.layout.add_widget(edit)
		edit.content=self.editLayout
		
		return self.layout
		
flowideApp().run()