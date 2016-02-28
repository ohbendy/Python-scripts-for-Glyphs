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
		
	def foregroundFlat(self):
		scale = self.getScale()
		HandleSize = Glyphs.defaults["GSHandleSize"]
		if HandleSize == 0:
			textSize = 9+scale*6;
		elif HandleSize == 2:
			textSize = 13+scale*6;
		else:
			textSize = 11+scale*6;
		if scale < 1:
			textSize *= pow(scale, 0.1)
		
		layer = self.activeLayer()
		position = self.activePosition()
		
		master = layer.associatedFontMaster()
		masterName = master.name
		
		thisGlyph = layer.parent
		if thisGlyph.unicode:
			glyph = thisGlyph.string
		else:
			glyph = thisGlyph.name
		textToDisplay = masterName + " : " + glyph
		
		if layer.width < 1:
			textX = layer.bounds.origin.x + (0.5 * layer.bounds.size.width)
		else:
			textX = layer.width / 2
		textY = max((layer.bounds.origin.y + layer.bounds.size.height), master.ascender)
		
		textX = position.x + (textX * scale)
		textY = position.y + (textY * scale) + 35
		
		self.drawBadge(
			textToDisplay,
			NSPoint(textX, textY),
			fontSize = textSize,
			align = GSBottomCenter,
			backgroundColor = NSColor.colorWithCalibratedRed_green_blue_alpha_(0.55 , 0.51 , 0.48, 0.2),
			visibleRect = True
		)
	
	def drawBadge(self, text, drawPoint, fontSize = 12.0, fontColor=NSColor.colorWithCalibratedRed_green_blue_alpha_(0.22 , 0.82 , 0.72, 0.6), backgroundColor = None, align = GSBottomLeft, visibleRect = False, active = False):
		glyphEditView = self.controller.graphicView()
		if visibleRect:
			visibleRect = glyphEditView.visibleRect()
		else:
			visibleRect = NSMakeRect(-10000000, -10000000, 20000000, 20000000)
		
		glyphEditView.drawBadge_size_color_backgroundColor_atPoint_alignment_visibleInRect_active_(text, fontSize, fontColor, backgroundColor, drawPoint, align, visibleRect, active)
	
	def ___background(self, layer):
		
		currentScale = self.getScale()
		rectSize = (20 + currentScale * 4) / currentScale
		rectOrigin = NSPoint(self.textX - 0.5 * rectSize, self.textY - 0.05 * rectSize)
		rectSize = NSSize(rectSize, rectSize)
		rect = NSRect(rectOrigin, rectSize)
		NSColor.colorWithCalibratedRed_green_blue_alpha_(0.55 , 0.51 , 0.48, 0.2).set()
		NSBezierPath.bezierPathWithOvalInRect_(rect).fill()
		print "__rect", rect