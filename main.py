from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.graphics import Color,Line,Rectangle
from kivy.uix.widget import Widget

from os import listdir

Window.size = (1200,800)

kv_path = './widgets/'
for kv in listdir(kv_path):
	if(kv[-3:]==".kv"):
		with open(kv_path+kv, encoding='utf8') as archivoWidget: 	#Se abre el archivo para poder leer acentos y caracteres UTF-8,
			Builder.load_string(archivoWidget.read())				#si se abre con la herramienta de Kivy estos no se visualizan.

class TabManager(TabbedPanel):
	pass
	
	
class picker(Widget):
	touched=False
	line=None
	points=[]
	def __init__(self,**kwargs):
		super(picker,self).__init__(**kwargs)
		self.size_hint=(None,None)
		self.bind(pos=self.update_canvas)
		self.bind(size=self.update_canvas)
		self.update_canvas()
	def update_canvas(self,*args):
		self.canvas.clear()
		with self.canvas:
			Color(0,0,1,1)
			Rectangle(pos=self.pos,size=self.size)
			
	def on_touch_down(self,touch):
		if(self.collide_point(touch.pos[0], touch.pos[1])):
			self.touched=True
			with self.canvas:
				self.points=[self.pos[0],self.pos[1],touch.pos[0],touch.pos[1]]
				self.line=Line(points=self.points,width=2)
	def on_touch_up(self,touch):
			self.touched=False
		
	def on_touch_move(self,touch):
		if(self.touched):
			print("blu",touch.pos)
			self.points[2]=touch.pos[0]
			self.points[3]=touch.pos[1]
			self.line.points=self.points
	
class box(Widget):
	def __init__(self,**kwargs):
		super(box,self).__init__(**kwargs)
		self.size_hint=(None,None)
		self.bind(pos=self.update_canvas)
		self.bind(size=self.update_canvas)
		self.update_canvas()
		self.add_widget(picker(pos=self.pos,size=(20,10)))
		
	def update_canvas(self,*args):
		self.canvas.clear()
		with self.canvas:
			Color(1,0,0,1)
			Rectangle(pos=self.pos,size=self.size)

class EditLayout(FloatLayout):
	xd=True
	def on_touch_down(self,touch):
		if(self.xd):
			if(self.collide_point(touch.pos[0], touch.pos[1])):
				self.add_widget(box(pos=touch.pos,size=(30,30)))
			self.xd=False
		super(EditLayout, self).on_touch_down(touch) 
	
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