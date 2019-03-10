from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.boxlayout import BoxLayout
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
	
class EditLayout(BoxLayout):
	def on_touch_down(self,touch):
		 print('The touch is at position', touch.pos)
	
class ConfigLayout(BoxLayout):
	pass
	
class Tab(TabbedPanelHeader):
	def __init__(self,**kwargs):
		super(Tab, self).__init__()
		self.text=kwargs.pop('title')
		self.content=kwargs.pop('content')
		tabber=kwargs.pop('tabber')
		tabber.add_widget(self)
		

class flowideApp(App):
	layout=TabManager()
	editLayout=EditLayout()
	configLayout=ConfigLayout()
	
	def build(self):
		Tab(title="Edit",tabber=self.layout,content=self.editLayout)
		Tab(title="Configuration",tabber=self.layout,content=self.configLayout)
		
		
		return self.layout
		
flowideApp().run()