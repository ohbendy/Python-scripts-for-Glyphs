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

class ShowMasterNameAndGlyph(ReporterPlugin):

	def settings(self):
		self.menuName = Glyphs.localize({'en': u'Master Name & Glyph'})
		
	def foreground(self, layer):
		currentScale = self.getScale()
		textSize = 12.0 + currentScale*6
		masterName = layer.associatedFontMaster().name
		if layer.width <1:
			textX = (layer.bounds.origin.x+(0.5*layer.bounds.size.width))
		else:
			textX = (layer.width/2)
		textY = (layer.bounds.origin.y+layer.bounds.size.height)+84
		self.drawTextAtPoint(
			masterName, 
			NSPoint(textX, textY),
			fontSize=textSize,
			align = "bottomcenter",
			fontColor=NSColor.colorWithCalibratedRed_green_blue_alpha_(
				0.1 , 0.7 , 0.5, 0.5
			),
		)
		
		thisGlyph = layer.parent
		if thisGlyph.unicode:
			textToDisplay = thisGlyph.string
		else:
			textToDisplay = thisGlyph.name
		
		self.drawTextAtPoint(
			textToDisplay,
			NSPoint(textX,textY-19),
			fontSize=textSize*1.3,
			align = "center",
			fontColor=NSColor.colorWithCalibratedRed_green_blue_alpha_(
				0.1 , 0.8 , 0.7, 0.8
			),
		)
		
	def background (self, layer):
		if layer.bounds:
			if layer.width <1:
				centerX = (layer.bounds.origin.x+(0.5*layer.bounds.size.width))
			else:
				centerX = (layer.width/2)
			centerY = (layer.bounds.origin.y+layer.bounds.size.height)+64
			currentScale = self.getScale()
			rectSize = 1/4*currentScale+24
			rectOrigin = NSPoint(centerX-0.5*rectSize, centerY-0.5*rectSize)
			rectSize = NSSize(
				rectSize,
				rectSize
			)
			rect = NSRect(rectOrigin, rectSize)
			NSColor.colorWithCalibratedRed_green_blue_alpha_(
				0.55 , 0.51 , 0.48, 0.2
			).set()
			NSBezierPath.bezierPathWithOvalInRect_(rect).fill()