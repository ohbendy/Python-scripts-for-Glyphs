#MenuTitle: Report Flipped Components
# -*- coding: utf-8 -*-
__doc__="""
Opens a new tab showing glyphs that contain flipped components.
"""
import GlyphsApp
Glyphs.clearLog()
Glyphs.showMacroWindow()
currentFont = Glyphs.font
listOfAffectedGlyphs = [] # make a new empty list

print "Flipped components:" 
for thisGlyph in currentFont.glyphs:
	componentsOnLayers = {}
	for thisLayer in thisGlyph.layers:
		for thisComponent in thisLayer.components:
			thisTransformation = thisComponent.transform
			if thisTransformation [0] < 0.0 or thisTransformation [3] < 0.0:
				componentKey = str(thisComponent.componentName)
				dictKeys = componentsOnLayers.keys()
				if not componentKey in dictKeys:
					componentsOnLayers[componentKey] = [thisLayer.name]
				else:
					componentsOnLayers[componentKey].append(thisLayer.name)
					
				if not thisGlyph.name in listOfAffectedGlyphs:
					listOfAffectedGlyphs.append(thisGlyph.name)
	
	if componentsOnLayers:
		print "Glyph %s:" % thisGlyph.name
		for componentName in componentsOnLayers.keys():
			print "   Component %s on layers: %s" % ( componentName, ", ".join(componentsOnLayers[componentName]) )
		print

print "Done."

if listOfAffectedGlyphs: # Checks object is not zero.
	tabstring = "/"+"/".join(listOfAffectedGlyphs) #puts slashes between glyph names and creates one big string and puts a slash in front of first glyph.
	currentFont.newTab(tabstring)
	# brings macro window to front and clears its log:

else:
	Message("Don't worry", "No flipped components.", OKButton="All goodie")