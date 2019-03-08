from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (1200,800)

class tabManager(TabbedPanel):
	pass
	
class EditLayout(StackLayout):
	pass
	
class ConfigLayout(StackLayout):
	pass
	
class tab(TabbedPanelHeader):
	pass

class flowideApp(App):
	layout=tabManager(do_default_tab=False)
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