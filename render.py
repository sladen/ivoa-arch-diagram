#!/usr/bin/env python2.7
# Pragmatic generator for International Virtual Observatory Association
# Architecture diagrams previously derived manually from:
# http://wiki.ivoa.net/internal/IVOA/VOArchitectureDiscussion/VOArchitecture.ppt
# Original Author: Christophe Arviset

import matplotlib
import matplotlib.pyplot as plt
import io

MEDIABOX_PSPOINT = (720., 540.) # 10 inch * 7.5 inch == 254mm * 190.5 mm
MEDIABOX_INCHES = [dimension / 72. for dimension in MEDIABOX_PSPOINT]
CENTRE = 356.436

def x(position, index=0): return position / MEDIABOX_PSPOINT[index]
def y(position, index=1): return position / MEDIABOX_PSPOINT[index]

def main():
    # generate + set size
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(*MEDIABOX_INCHES)

    font = matplotlib.font_manager.FontProperties()
    font.set_family('Arial')
    font.set_weight('bold')
    font.set_size(18)
    fig.text(x(22.680), y(503.280),
             'LEVEL 0',
             fontproperties=font,
             color='red')
    fig.text(x(CENTRE), y(452.284),
             'USER LAYER',
             fontproperties=font,
             horizontalalignment='center')
    fig.text(x(CENTRE), y(389.884),
             'USING',
             fontproperties=font,
             horizontalalignment='center')
    fig.text(x(CENTRE), y(250),
             'VO\nCORE',
             fontproperties=font,
             horizontalalignment='center')
    fig.text(x(CENTRE), y(123.384),
             'SHARING',
             fontproperties=font,
             horizontalalignment='center')
    fig.text(x(CENTRE), y(55.884),
             'RESOURCE LAYER',
             fontproperties=font,
             horizontalalignment='center')

    # left and right
    fig.text(x(130), y(260),
             '\n'.join('FINDING'),
             fontproperties=font,
             horizontalalignment='center',
             verticalalignment='center')
    # righthand side is slightly shifted up
    fig.text(x(584), y(260+(321.884-316.300)),
             '\n'.join('GETTING'),
             fontproperties=font,
             horizontalalignment='center',
             verticalalignment='center')
             



    font.set_size(12)
    fig.text(x(176.490), y(521.418),
             'USERS',
             fontproperties=font,
             color='black')
    fig.text(x(475.604), y(495.518),
             'COMPUTERS',
             fontproperties=font,
             color='black')
    fig.text(x(296.413), y(22.118),
             'PROVIDERS',
             fontproperties=font,
             color='black')

    font.set_size(10)
    fig.text(x(58.149), y(29.478),
             '20100525',
             fontproperties=font,
             color='black')
    fig.text(x(37.684), y(17.478),
             'IVOA Architecture',
             fontproperties=font,
             color='black')

    # boxes
    # 1pt solid black
    # x=82.100, y=417.400, w=550.000, h=51.100
    fig.patches.extend([matplotlib.patches.Rectangle(
                (x(82.1), y(417.400)), x(550), y(51.1),
                fill=False, edgecolor='black', zorder=1000, linewidth=1,
                transform=fig.transFigure,
                figure=fig)])
    fig.patches.extend([matplotlib.patches.Rectangle(
                (x(82.1), y(105.6)), x(550), y(311.8),
                fill=False, edgecolor='black', zorder=1000, linewidth=0.736,
                transform=fig.transFigure,
                figure=fig)])
    fig.patches.extend([matplotlib.patches.Rectangle(
                (x(82.100), y(54.5)), x(550), y(51.1),
                fill=False, edgecolor='black', zorder=1000, linewidth=0.736,
                transform=fig.transFigure,
                figure=fig)])

    # The four crossing dotted lines are four dashed rectangles...
    # dotted lines: linewidth=0.700
    # 1x = 2.9pt/3.0pt, 2x = 8.2pt
    # [3.0]..2.2..[3.0]..2.2..[3.0]..2.2
    # top
    fig.patches.extend([matplotlib.patches.Rectangle(
                (x(82.100), y(372)), x(550), y(45.3),
                fill=False, edgecolor='black', zorder=990, linewidth=0.700,
                linestyle='dashed', transform=fig.transFigure,
                figure=fig)])
    # bottom
    fig.patches.extend([matplotlib.patches.Rectangle(
                (x(82.100), y(105.6)), x(550), y(45.3),
                fill=False, edgecolor='black', zorder=990, linewidth=0.700,
                linestyle='dashed', transform=fig.transFigure,
                figure=fig)])
    # left
    fig.patches.extend([matplotlib.patches.Rectangle(
                (x(82.1), y(105.6)), x(96.4), y(311.8),
                fill=False, edgecolor='black', zorder=990, linewidth=0.700,
                linestyle='dashed', transform=fig.transFigure,
                figure=fig)])
    # right
    fig.patches.extend([matplotlib.patches.Rectangle(
                (x(535.7), y(105.6)), x(96.4), y(311.8),
                fill=False, edgecolor='black', zorder=990, linewidth=0.700,
                linestyle='dashed', transform=fig.transFigure,
                figure=fig)])




    # output
    with open('foobar.pdf', 'wb') as pdf:
        f = io.BytesIO()
        fig.savefig(f, format='pdf')
        f.seek(0)
        f.seek(0)
        pdfstream = f.getvalue()
        pdf.write(pdfstream)

if __name__=='__main__':
    main()
