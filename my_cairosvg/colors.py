# This file is part of CairoSVG
# Copyright © 2010-2018 Kozea
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with CairoSVG.  If not, see <http://www.gnu.org/licenses/>.

"""
SVG colors.

"""

import re
# TODO Start my code
import os
import pandas as pd
import numpy as np
home = os.environ['HOME']
# TODO End code

COLORS = {
    'aliceblue': (240 / 255, 248 / 255, 255 / 255, 1),
    'antiquewhite': (250 / 255, 235 / 255, 215 / 255, 1),
    'aqua': (0 / 255, 255 / 255, 255 / 255, 1),
    'aquamarine': (127 / 255, 255 / 255, 212 / 255, 1),
    'azure': (240 / 255, 255 / 255, 255 / 255, 1),
    'beige': (245 / 255, 245 / 255, 220 / 255, 1),
    'bisque': (255 / 255, 228 / 255, 196 / 255, 1),
    'black': (0 / 255, 0 / 255, 0 / 255, 1),
    'blanchedalmond': (255 / 255, 235 / 255, 205 / 255, 1),
    'blue': (0 / 255, 0 / 255, 255 / 255, 1),
    'blueviolet': (138 / 255, 43 / 255, 226 / 255, 1),
    'brown': (165 / 255, 42 / 255, 42 / 255, 1),
    'burlywood': (222 / 255, 184 / 255, 135 / 255, 1),
    'cadetblue': (95 / 255, 158 / 255, 160 / 255, 1),
    'chartreuse': (127 / 255, 255 / 255, 0 / 255, 1),
    'chocolate': (210 / 255, 105 / 255, 30 / 255, 1),
    'coral': (255 / 255, 127 / 255, 80 / 255, 1),
    'cornflowerblue': (100 / 255, 149 / 255, 237 / 255, 1),
    'cornsilk': (255 / 255, 248 / 255, 220 / 255, 1),
    'crimson': (220 / 255, 20 / 255, 60 / 255, 1),
    'cyan': (0 / 255, 255 / 255, 255 / 255, 1),
    'darkblue': (0 / 255, 0 / 255, 139 / 255, 1),
    'darkcyan': (0 / 255, 139 / 255, 139 / 255, 1),
    'darkgoldenrod': (184 / 255, 134 / 255, 11 / 255, 1),
    'darkgray': (169 / 255, 169 / 255, 169 / 255, 1),
    'darkgreen': (0 / 255, 100 / 255, 0 / 255, 1),
    'darkgrey': (169 / 255, 169 / 255, 169 / 255, 1),
    'darkkhaki': (189 / 255, 183 / 255, 107 / 255, 1),
    'darkmagenta': (139 / 255, 0 / 255, 139 / 255, 1),
    'darkolivegreen': (85 / 255, 107 / 255, 47 / 255, 1),
    'darkorange': (255 / 255, 140 / 255, 0 / 255, 1),
    'darkorchid': (153 / 255, 50 / 255, 204 / 255, 1),
    'darkred': (139 / 255, 0 / 255, 0 / 255, 1),
    'darksalmon': (233 / 255, 150 / 255, 122 / 255, 1),
    'darkseagreen': (143 / 255, 188 / 255, 143 / 255, 1),
    'darkslateblue': (72 / 255, 61 / 255, 139 / 255, 1),
    'darkslategray': (47 / 255, 79 / 255, 79 / 255, 1),
    'darkslategrey': (47 / 255, 79 / 255, 79 / 255, 1),
    'darkturquoise': (0 / 255, 206 / 255, 209 / 255, 1),
    'darkviolet': (148 / 255, 0 / 255, 211 / 255, 1),
    'deeppink': (255 / 255, 20 / 255, 147 / 255, 1),
    'deepskyblue': (0 / 255, 191 / 255, 255 / 255, 1),
    'dimgray': (105 / 255, 105 / 255, 105 / 255, 1),
    'dimgrey': (105 / 255, 105 / 255, 105 / 255, 1),
    'dodgerblue': (30 / 255, 144 / 255, 255 / 255, 1),
    'firebrick': (178 / 255, 34 / 255, 34 / 255, 1),
    'floralwhite': (255 / 255, 250 / 255, 240 / 255, 1),
    'forestgreen': (34 / 255, 139 / 255, 34 / 255, 1),
    'fuchsia': (255 / 255, 0 / 255, 255 / 255, 1),
    'gainsboro': (220 / 255, 220 / 255, 220 / 255, 1),
    'ghostwhite': (248 / 255, 248 / 255, 255 / 255, 1),
    'gold': (255 / 255, 215 / 255, 0 / 255, 1),
    'goldenrod': (218 / 255, 165 / 255, 32 / 255, 1),
    'gray': (128 / 255, 128 / 255, 128 / 255, 1),
    'grey': (128 / 255, 128 / 255, 128 / 255, 1),
    'green': (0 / 255, 128 / 255, 0 / 255, 1),
    'greenyellow': (173 / 255, 255 / 255, 47 / 255, 1),
    'honeydew': (240 / 255, 255 / 255, 240 / 255, 1),
    'hotpink': (255 / 255, 105 / 255, 180 / 255, 1),
    'indianred': (205 / 255, 92 / 255, 92 / 255, 1),
    'indigo': (75 / 255, 0 / 255, 130 / 255, 1),
    'ivory': (255 / 255, 255 / 255, 240 / 255, 1),
    'khaki': (240 / 255, 230 / 255, 140 / 255, 1),
    'lavender': (230 / 255, 230 / 255, 250 / 255, 1),
    'lavenderblush': (255 / 255, 240 / 255, 245 / 255, 1),
    'lawngreen': (124 / 255, 252 / 255, 0 / 255, 1),
    'lemonchiffon': (255 / 255, 250 / 255, 205 / 255, 1),
    'lightblue': (173 / 255, 216 / 255, 230 / 255, 1),
    'lightcoral': (240 / 255, 128 / 255, 128 / 255, 1),
    'lightcyan': (224 / 255, 255 / 255, 255 / 255, 1),
    'lightgoldenrodyellow': (250 / 255, 250 / 255, 210 / 255, 1),
    'lightgray': (211 / 255, 211 / 255, 211 / 255, 1),
    'lightgreen': (144 / 255, 238 / 255, 144 / 255, 1),
    'lightgrey': (211 / 255, 211 / 255, 211 / 255, 1),
    'lightpink': (255 / 255, 182 / 255, 193 / 255, 1),
    'lightsalmon': (255 / 255, 160 / 255, 122 / 255, 1),
    'lightseagreen': (32 / 255, 178 / 255, 170 / 255, 1),
    'lightskyblue': (135 / 255, 206 / 255, 250 / 255, 1),
    'lightslategray': (119 / 255, 136 / 255, 153 / 255, 1),
    'lightslategrey': (119 / 255, 136 / 255, 153 / 255, 1),
    'lightsteelblue': (176 / 255, 196 / 255, 222 / 255, 1),
    'lightyellow': (255 / 255, 255 / 255, 224 / 255, 1),
    'lime': (0 / 255, 255 / 255, 0 / 255, 1),
    'limegreen': (50 / 255, 205 / 255, 50 / 255, 1),
    'linen': (250 / 255, 240 / 255, 230 / 255, 1),
    'magenta': (255 / 255, 0 / 255, 255 / 255, 1),
    'maroon': (128 / 255, 0 / 255, 0 / 255, 1),
    'mediumaquamarine': (102 / 255, 205 / 255, 170 / 255, 1),
    'mediumblue': (0 / 255, 0 / 255, 205 / 255, 1),
    'mediumorchid': (186 / 255, 85 / 255, 211 / 255, 1),
    'mediumpurple': (147 / 255, 112 / 255, 219 / 255, 1),
    'mediumseagreen': (60 / 255, 179 / 255, 113 / 255, 1),
    'mediumslateblue': (123 / 255, 104 / 255, 238 / 255, 1),
    'mediumspringgreen': (0 / 255, 250 / 255, 154 / 255, 1),
    'mediumturquoise': (72 / 255, 209 / 255, 204 / 255, 1),
    'mediumvioletred': (199 / 255, 21 / 255, 133 / 255, 1),
    'midnightblue': (25 / 255, 25 / 255, 112 / 255, 1),
    'mintcream': (245 / 255, 255 / 255, 250 / 255, 1),
    'mistyrose': (255 / 255, 228 / 255, 225 / 255, 1),
    'moccasin': (255 / 255, 228 / 255, 181 / 255, 1),
    'navajowhite': (255 / 255, 222 / 255, 173 / 255, 1),
    'navy': (0 / 255, 0 / 255, 128 / 255, 1),
    'oldlace': (253 / 255, 245 / 255, 230 / 255, 1),
    'olive': (128 / 255, 128 / 255, 0 / 255, 1),
    'olivedrab': (107 / 255, 142 / 255, 35 / 255, 1),
    'orange': (255 / 255, 165 / 255, 0 / 255, 1),
    'orangered': (255 / 255, 69 / 255, 0 / 255, 1),
    'orchid': (218 / 255, 112 / 255, 214 / 255, 1),
    'palegoldenrod': (238 / 255, 232 / 255, 170 / 255, 1),
    'palegreen': (152 / 255, 251 / 255, 152 / 255, 1),
    'paleturquoise': (175 / 255, 238 / 255, 238 / 255, 1),
    'palevioletred': (219 / 255, 112 / 255, 147 / 255, 1),
    'papayawhip': (255 / 255, 239 / 255, 213 / 255, 1),
    'peachpuff': (255 / 255, 218 / 255, 185 / 255, 1),
    'peru': (205 / 255, 133 / 255, 63 / 255, 1),
    'pink': (255 / 255, 192 / 255, 203 / 255, 1),
    'plum': (221 / 255, 160 / 255, 221 / 255, 1),
    'powderblue': (176 / 255, 224 / 255, 230 / 255, 1),
    'purple': (128 / 255, 0 / 255, 128 / 255, 1),
    'red': (255 / 255, 0 / 255, 0 / 255, 1),
    'rosybrown': (188 / 255, 143 / 255, 143 / 255, 1),
    'royalblue': (65 / 255, 105 / 255, 225 / 255, 1),
    'saddlebrown': (139 / 255, 69 / 255, 19 / 255, 1),
    'salmon': (250 / 255, 128 / 255, 114 / 255, 1),
    'sandybrown': (244 / 255, 164 / 255, 96 / 255, 1),
    'seagreen': (46 / 255, 139 / 255, 87 / 255, 1),
    'seashell': (255 / 255, 245 / 255, 238 / 255, 1),
    'sienna': (160 / 255, 82 / 255, 45 / 255, 1),
    'silver': (192 / 255, 192 / 255, 192 / 255, 1),
    'skyblue': (135 / 255, 206 / 255, 235 / 255, 1),
    'slateblue': (106 / 255, 90 / 255, 205 / 255, 1),
    'slategray': (112 / 255, 128 / 255, 144 / 255, 1),
    'slategrey': (112 / 255, 128 / 255, 144 / 255, 1),
    'snow': (255 / 255, 250 / 255, 250 / 255, 1),
    'springgreen': (0 / 255, 255 / 255, 127 / 255, 1),
    'steelblue': (70 / 255, 130 / 255, 180 / 255, 1),
    'tan': (210 / 255, 180 / 255, 140 / 255, 1),
    'teal': (0 / 255, 128 / 255, 128 / 255, 1),
    'thistle': (216 / 255, 191 / 255, 216 / 255, 1),
    'tomato': (255 / 255, 99 / 255, 71 / 255, 1),
    'turquoise': (64 / 255, 224 / 255, 208 / 255, 1),
    'violet': (238 / 255, 130 / 255, 238 / 255, 1),
    'wheat': (245 / 255, 222 / 255, 179 / 255, 1),
    'white': (255 / 255, 255 / 255, 255 / 255, 1),
    'whitesmoke': (245 / 255, 245 / 255, 245 / 255, 1),
    'yellow': (255 / 255, 255 / 255, 0 / 255, 1),
    'yellowgreen': (154 / 255, 205 / 255, 50 / 255, 1),

    'activeborder': (0, 0, 1, 1),
    'activecaption': (0, 0, 1, 1),
    'appworkspace': (1, 1, 1, 1),
    'background': (1, 1, 1, 1),
    'buttonface': (0, 0, 0, 1),
    'buttonhighlight': (0.8, 0.8, 0.8, 1),
    'buttonshadow': (0.2, 0.2, 0.2, 1),
    'buttontext': (0, 0, 0, 1),
    'captiontext': (0, 0, 0, 1),
    'graytext': (0.2, 0.2, 0.2, 1),
    'highlight': (0, 0, 1, 1),
    'highlighttext': (0.8, 0.8, 0.8, 1),
    'inactiveborder': (0.2, 0.2, 0.2, 1),
    'inactivecaption': (0.8, 0.8, 0.8, 1),
    'inactivecaptiontext': (0.2, 0.2, 0.2, 1),
    'infobackground': (0.8, 0.8, 0.8, 1),
    'infotext': (0, 0, 0, 1),
    'menu': (0.8, 0.8, 0.8, 1),
    'menutext': (0.2, 0.2, 0.2, 1),
    'scrollbar': (0.8, 0.8, 0.8, 1),
    'threeddarkshadow': (0.2, 0.2, 0.2, 1),
    'threedface': (0.8, 0.8, 0.8, 1),
    'threedhighlight': (1, 1, 1, 1),
    'threedlightshadow': (0.2, 0.2, 0.2, 1),
    'threedshadow': (0.2, 0.2, 0.2, 1),
    'window': (0.8, 0.8, 0.8, 1),
    'windowframe': (0.8, 0.8, 0.8, 1),
    'windowtext': (0, 0, 0, 1),

    'none': (0, 0, 0, 0),
    'transparent': (0, 0, 0, 0),
}

RGBA = re.compile(r'rgba\([ \n\r\t]*(.+?)[ \n\r\t]*\)')
RGB = re.compile(r'rgb\([ \n\r\t]*(.+?)[ \n\r\t]*\)')
HEX_RRGGBB = re.compile('#[0-9a-f]{6}')
HEX_RGB = re.compile('#[0-9a-f]{3}')


# TODO (Start my code)
def get_id2ix():
    """
        Return dictionary to convert structure_id into smaller number
        amenable to be cast into 24 bit.
    """
    metadata_path = os.path.join(home, 'git/brain/metadata')
    ont1_path = os.path.join(metadata_path, 'onthology_id_1.pkl')
    assert os.path.isfile(ont1_path)
    df = pd.read_pickle(ont1_path)
    structure_ids = df['id'].unique()
#     print("Found {} structures".format(len(structure_ids)))
#     print("0 in structure id? {}".format(0 in structure_ids))
#     ix_2_id = {ix+1:structure_id for ix, structure_id in enumerate(structure_ids)}
    id_2_ix = {structure_id:ix+1 for ix, structure_id in enumerate(structure_ids)}
    return id_2_ix


def pad_to(binary_number, num_bits):
    """
        Pad `binary_number` to the left until is `num_bits` long.
    """
    num_padding_zeros = num_bits - len(binary_number)
    assert num_padding_zeros >= 0
    prefix = '0' * num_padding_zeros
    binary_number_padded = prefix + binary_number
    return binary_number_padded


def from_id_to_rgb(structure_id):
    """
        Convert `structure_id` into a RGB number.
    """
    # Get converter for structure id
    id2ix = get_id2ix()
    if structure_id == 0:
        return (0, 0, 0)
    else:
        compressed_id = id2ix[structure_id]
    # convert to binary
    id_binary = bin(compressed_id)
    # take out '0b'
    id_binary = id_binary[2:]
    assert len(id_binary) <= 24
    # convert to 24 bit
    id_binary_24 = pad_to(id_binary, 24)
    assert len(id_binary_24) == 24
    # get RGB coordinates (8 bit each)
    r = int(id_binary_24[0:8], 2)
    g = int(id_binary_24[8:16], 2)
    b = int(id_binary_24[16:24], 2)
    assert (r, g, b) != (0, 0, 0)
    return (r, g, b)


def get_ix2id():
    """
        Return dictionary to convert id used in images back to structure id
    """
    metadata_path = os.path.join(home, 'git/brain/metadata')
    ont1_path = os.path.join(metadata_path, 'onthology_id_1.pkl')
    assert os.path.isfile(ont1_path)
    df = pd.read_pickle(ont1_path)
    structure_ids = df['id'].unique()
    ix_2_id = {ix+1:structure_id for ix, structure_id in enumerate(structure_ids)}
    return ix_2_id


def from_rgb_to_id(r, g, b):
    """
        Convert RGB color back to structure_id.
    """
    if (r, g, b) == (0, 0, 0):
        return 0
    ix2id = get_ix2id()
    r_bin = pad_to(bin(r)[2:], 8)
    g_bin = pad_to(bin(g)[2:], 8)
    b_bin = pad_to(bin(b)[2:], 8)
    compressed_id = int(r_bin + g_bin + b_bin, 2)
    try:
        structure_id = ix2id[compressed_id]
    except:
        print(compressed_id, r_bin, g_bin, b_bin, r, g, b)
    return structure_id
# TODO (End my code)


def color(string, opacity=1):
    """Replace ``string`` representing a color by a RGBA tuple.

    See http://www.w3.org/TR/SVG/types.html#DataTypeColor

    """
    # TODO (Start my code)
    r, g, b = from_id_to_rgb(string)
    return (r, g, b, 255)
    # TODO (end my code)

    if not string:
        return (0, 0, 0, 0)

    string = string.strip().lower()

    if string in COLORS:
        r, g, b, a = COLORS[string]
        return (r, g, b, a * opacity)

    match = RGBA.search(string)
    if match:
        r, g, b, a = tuple(
            float(i.strip(' %')) / 100 if '%' in i else float(i) / 255
            for i in match.group(1).split(','))
        return (r, g, b, a * 255 * opacity)

    match = RGB.search(string)
    if match:
        r, g, b = tuple(
            float(i.strip(' %')) / 100 if '%' in i else float(i) / 255
            for i in match.group(1).split(','))
        return (r, g, b, opacity)

    match = HEX_RRGGBB.search(string)
    if match:
        plain_color = tuple(
            int(value, 16) / 255 for value in (
                string[1:3], string[3:5], string[5:7]))
        return plain_color + (opacity,)

    match = HEX_RGB.search(string)
    if match:
        plain_color = tuple(
            int(value, 16) / 15 for value in (
                string[1], string[2], string[3]))
        return plain_color + (opacity,)

    return (0, 0, 0, 1)
