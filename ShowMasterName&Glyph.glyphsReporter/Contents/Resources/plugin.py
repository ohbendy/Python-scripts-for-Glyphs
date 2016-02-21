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
		textSize = 10 + currentScale * 4
		masterName = layer.associatedFontMaster().name
		self.drawTextAtPoint(
			masterName, 
			NSPoint(self.textX, self.textY + ((16 + currentScale * 6) / currentScale)),
			fontSize=textSize,
			align = "bottomcenter",
			fontColor=NSColor.colorWithCalibratedRed_green_blue_alpha_(0.1 , 0.7 , 0.5, 0.5)
		)
		
		thisGlyph = layer.parent
		if thisGlyph.unicode:
			textToDisplay = thisGlyph.string
		else:
			textToDisplay = thisGlyph.name
		
		self.drawTextAtPoint(
			textToDisplay,
			NSPoint(self.textX, self.textY),
			fontSize=textSize * 1.3,
			align = "bottomcenter",
			fontColor=NSColor.colorWithCalibratedRed_green_blue_alpha_(0.1 , 0.8 , 0.7, 0.8)
		)
		
	def background(self, layer):
		if layer.width < 1:
			self.textX = (layer.bounds.origin.x + (0.5 * layer.bounds.size.width))
		else:
			self.textX = (layer.width / 2)
		self.textY = max((layer.bounds.origin.y + layer.bounds.size.height), layer.glyphMetrics()[1])
		
		currentScale = self.getScale()
		rectSize = (20 + currentScale * 4) / currentScale
		rectOrigin = NSPoint(self.textX - 0.5 * rectSize, self.textY - 0.05 * rectSize)
		rectSize = NSSize(rectSize, rectSize)
		rect = NSRect(rectOrigin, rectSize)
		NSColor.colorWithCalibratedRed_green_blue_alpha_(0.55 , 0.51 , 0.48, 0.2).set()
		NSBezierPath.bezierPathWithOvalInRect_(rect).fill()
		print "__rect", rect