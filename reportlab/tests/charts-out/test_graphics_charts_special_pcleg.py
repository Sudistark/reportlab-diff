#Autogenerated by ReportLab guiedit do not edit
from reportlab.graphics.shapes import _DrawingEditorMixin, Drawing, Group, Rect, Wedge, String, Polygon
from reportlab.lib.colors import Color, CMYKColor, PCMYKColor

class ExplodedDrawing_Drawing(_DrawingEditorMixin,Drawing):
	def __init__(self,width=300,height=150,*args,**kw):
		Drawing.__init__(self,width,height,*args,**kw)
		self.transform = (1,0,0,1,0,0)
		self.add(Rect(0,0,300,150,rx=0,ry=0,fillColor=None,fillOpacity=None,strokeColor=Color(1,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Wedge(50,50,50,50.86957,90,yradius=50,annular=False,fillColor=Color(0,.545098,.545098,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=0,strokeLineCap=0,strokeLineJoin=1,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Wedge(50,50,50,-39.13043,50.86957,yradius=50,annular=False,fillColor=Color(.541176,.168627,.886275,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=0,strokeLineCap=0,strokeLineJoin=1,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Wedge(50,50,50,-105.6522,-39.13043,yradius=50,annular=False,fillColor=Color(0,0,1,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=0,strokeLineCap=0,strokeLineJoin=1,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Wedge(50,50,50,-270,-105.6522,yradius=50,annular=False,fillColor=Color(0,1,1,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=0,strokeLineCap=0,strokeLineJoin=1,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Rect(186.9238,42,20,5,rx=0,ry=0,fillColor=Color(1,0,0,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(String(145,40.70117,'röt',textAnchor='start',fontName='Vera',fontSize=10,fillColor=Color(0,0,0,1)))
		self.add(Rect(186.9238,28,20,5,rx=0,ry=0,fillColor=Color(0,0,1,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(String(145,26.70117,'blue',textAnchor='start',fontName='Vera',fontSize=10,fillColor=Color(0,0,0,1)))
		self.add(Rect(186.9238,14,20,5,rx=0,ry=0,fillColor=Color(0,.501961,0,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(String(145,12.70117,'green',textAnchor='start',fontName='Vera',fontSize=10,fillColor=Color(0,0,0,1)))
		self.add(Rect(261.9238,42,20,5,rx=0,ry=0,fillColor=Color(1,.752941,.796078,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(String(220,40.70117,'pink',textAnchor='start',fontName='Vera',fontSize=10,fillColor=Color(0,0,0,1)))
		self.add(Rect(261.9238,28,20,5,rx=0,ry=0,fillColor=Color(1,1,0,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(String(220,26.70117,'yellow',textAnchor='start',fontName='Vera',fontSize=10,fillColor=Color(0,0,0,1)))
		self.add(Polygon(points=[294.1667,2.5,294.1667,4.166667,292.5,4.166667,292.5,5.833333,294.1667,5.833333,294.1667,7.5,295.8333,7.5,295.8333,5.833333,297.5,5.833333,297.5,4.166667,295.8333,4.166667,295.8333,2.5],fillColor=Color(1,0,0,1),fillOpacity=None,strokeColor=Color(1,1,0,1),strokeWidth=.1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))


if __name__=="__main__": #NORUNTESTS
	ExplodedDrawing_Drawing().save(formats=['pdf'],outDir='.',fnRoot=None)
