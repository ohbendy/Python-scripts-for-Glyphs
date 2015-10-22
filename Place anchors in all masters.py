#MenuTitle: Add anchors to above mark glyphs
# -*- coding: utf-8 -*-
"""Adds _top anchors to all layers of selected glyphs."""

import GlyphsApp

thisFont = Glyphs.font

# This script will add _top attachment anchors to selected mark glyphs at the ( x,y ) coordinates in each master named.
# Adapt master names, anchor names and anchor positions as required.
# Add other anchors under each master, no problem.

for glyph in [l.parent for l in thisFont.selectedLayers]:

			# LIGHT master first:
	for master in thisFont.masters:
		if master.name == 'Light':
				id = master.id
				break
	layer = glyph.layers[id]
			
			# add _top anchor:
	_topAnchor = GSAnchor.alloc().init()
	_topAnchor.name = "_top"
	layer.addAnchor_(_topAnchor)

			# set its position:
	position = ( -300, 600 )
	_topAnchor.setPosition_( position )
			
			# REGULAR master next:
	for master in thisFont.masters:
		if master.name == 'Regular':
				id = master.id
				break
	layer = glyph.layers[id]
			
			# add _top anchor:
	_topAnchor = GSAnchor.alloc().init()
	_topAnchor.name = "_top"
	layer.addAnchor_(_topAnchor)

			# set its position:
	position = ( -315, 610 )
	_topAnchor.setPosition_( position )
	
			# BOLD master next:
	for master in thisFont.masters:
		if master.name == 'Bold':
				id = master.id
				break
	layer = glyph.layers[id]
			
			# add _top anchor:
	_topAnchor = GSAnchor.alloc().init()
	_topAnchor.name = "_top"
	layer.addAnchor_(_topAnchor)

			# set its position:
	position = ( -320, 620 )
	_topAnchor.setPosition_( position )
	
			# LIGHTCONDENSED master next:
	for master in thisFont.masters:
		if master.name == 'Light Condensed':
				id = master.id
				break
	layer = glyph.layers[id]
			
			# add _top anchor:
	_topAnchor = GSAnchor.alloc().init()
	_topAnchor.name = "_top"
	layer.addAnchor_(_topAnchor)

			# set its position:
	position = ( -250, 600 )
	_topAnchor.setPosition_( position )
	
				# CONDENSED master next:
	for master in thisFont.masters:
		if master.name == 'Condensed':
				id = master.id
				break
	layer = glyph.layers[id]
			
			# add _top anchor:
	_topAnchor = GSAnchor.alloc().init()
	_topAnchor.name = "_top"
	layer.addAnchor_(_topAnchor)

			# set its position:
	position = ( -255, 610 )
	_topAnchor.setPosition_( position )
	
			# BOLDCONDENSED master next:
	for master in thisFont.masters:
		if master.name == 'Bold Condensed':
				id = master.id
				break
	layer = glyph.layers[id]
			
			# add _top anchor:
	_topAnchor = GSAnchor.alloc().init()
	_topAnchor.name = "_top"
	layer.addAnchor_(_topAnchor)

			# set its position:
	position = ( -260, 620 )
	_topAnchor.setPosition_( position )