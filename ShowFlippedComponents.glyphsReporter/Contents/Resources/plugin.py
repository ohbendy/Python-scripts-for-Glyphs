# encoding: utf-8

###########################################################################################################
#
#
#	Reporter Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################


from GlyphsApp.plugins import *

class ShowFlippedComponents(ReporterPlugin):

	def settings(self):
		self.menuName = Glyphs.localize({'en': u'Flipped Components'})
		
	def foreground(self, layer):
		Controller = self.controller.view().window().windowController()
		if Controller.SpaceKey():
			return
		if Controller.toolDrawDelegate().isKindOfClass_(NSClassFromString("GlyphsToolText")):
			return
		if layer.components:
			for component in layer.components:
				thisTransformation = component.transform
				if thisTransformation [0] < 0.0 or thisTransformation [3] < 0.0:
					if component.componentLayer().anchors:
						NSColor.colorWithCalibratedRed_green_blue_alpha_(
							0.75 , 0.71 , 0.68, 0.6
						).set()
						component.bezierPath.fill()
						NSColor.colorWithCalibratedRed_green_blue_alpha_(
							1.0 , 0.35 , 0.0, 0.75
						).set()
						bezierpath = component.bezierPath
						bezierpath.setLineWidth_(6)
						bezierpath.stroke()
						textX=component.bounds.origin.x+0.5*component.bounds.size.width
						textY=component.bounds.origin.y+0.5*component.bounds.size.height
						currentScale = self.getScale()
						textSize = 8.0 + currentScale*6
						self.drawTextAtPoint(
							"Component has flipped anchors",
							NSPoint(textX,textY),
							fontSize=textSize,
							align = "center",
							fontColor=NSColor.colorWithCalibratedRed_green_blue_alpha_(
								0.55 , 0.51 , 0.48, 0.5
							),
						)
					else:
						NSColor.colorWithCalibratedRed_green_blue_alpha_(
							0.75 , 0.71 , 0.68, 0.6
						).set()
						component.bezierPath.fill()
						NSColor.colorWithCalibratedRed_green_blue_alpha_(
							0.9 , 0.0 , 0.3, 0.65
						).set()
						#scale = self.getScale()
						bezierpath = component.bezierPath
						bezierpath.setLineWidth_(6)
						bezierpath.stroke()
						textX=component.bounds.origin.x+0.5*component.bounds.size.width
						textY=component.bounds.origin.y+0.5*component.bounds.size.height
						currentScale = self.getScale()
						textSize = 8.0 + currentScale*6
						self.drawTextAtPoint(
							"Flipped component",
							NSPoint(textX,textY),
							fontSize=textSize,
							align = "center",
							fontColor=NSColor.colorWithCalibratedRed_green_blue_alpha_(
								0.55 , 0.51 , 0.48, 0.5
							),
						)
	def preview(self, layer):
		NSColor.blackColor().set()
		if layer.paths:
			layer.bezierPath.fill()
		if layer.components:
			for component in layer.components:
				component.bezierPath.fill()