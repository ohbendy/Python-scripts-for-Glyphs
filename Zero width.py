#MenuTitle: Zero-width all layers
# -*- coding: utf-8 -*-
"""Adjusts widths of all layers to zero"""

import GlyphsApp
font = Glyphs.font
selectedLayers = font.selectedLayers

for gLayer in selectedLayers:
	glyph = gLayer.parent
	for layer in glyph.layers:
		layer.width = 0
