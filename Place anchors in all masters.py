#MenuTitle: Add anchors to above mark glyphs
# -*- coding: utf-8 -*-
"""Adds _top anchors to all layers of selected glyphs."""

import GlyphsApp

anchorDict = {
	"Light":   (-300, 600),
	"Regular": (-315, 610),
	"Bold":    (-320, 620),
	"Light Condensed": (-250, 600),
	"Condensed":       (-255, 610),
	"Bold Condensed":  (-260, 620)
}

# This script will add _top attachment anchors to selected mark glyphs at the ( x,y ) coordinates in each master named.
# Adapt master names, anchor names and anchor positions as required.
# Add other anchors under each master, no problem.

def addAnchorToLayer( thisLayer, anchorname="_top", anchorposition=(300,600) ):
	if thisLayer:
		newAnchor = GSAnchor.alloc().init()
		newAnchor.name = anchorname
		thisLayer.addAnchor_( newAnchor )
		newPosition = NSPoint( anchorposition[0], anchorposition[1])
		newAnchor.setPosition_( newPosition )

thisFont = Glyphs.font
allSelectedGlyphs = [l.parent for l in thisFont.selectedLayers]
allMasterNames = anchorDict.keys() # master names listed in anchorDict

# iterate through all layers of all selected glyphs:
for thisGlyph in allSelectedGlyphs:
	for thisLayer in thisGlyph.layers:
		# determine the master to which the layer belongs:
		masterID = thisLayer.associatedMasterId
		thisMasterName = thisFont.masters[masterID].name
		# if it is listed in anchorDict, add the anchor at the given position:
		if thisMasterName in allMasterNames:
			thisPositionXY = anchorDict[thisMasterName]
			thisPosition = NSPoint( thisPositionXY[0], thisPositionXY[1] )
			addAnchorToLayer( thisLayer, anchorposition=thisPosition )
