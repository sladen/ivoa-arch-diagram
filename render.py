#!/usr/bin/env python2.7

import matplotlib
import matplotlib.pyplot as plt
import io

MEDIABOX_PSPOINT = (720., 540.)
MEDIABOX_INCHES = [dimension / 72. for dimension in MEDIABOX_PSPOINT]

def x(position): return position / MEDIABOX_PSPOINT[0]
def y(position): return position / MEDIABOX_PSPOINT[1]

def main():
    # generate + set size
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(*MEDIABOX_INCHES)

    font = matplotlib.font_manager.FontProperties()
    font.set_family('Arial')
    font.set_weight('bold')
    font.set_size(18)
    fig.text(x(22.680), y(503.280),
             'LEVEL 1',
             fontproperties=font,
             color='red')
    fig.text(x(301.622), y(452.284),
             'USER LAYER',
             fontproperties=font)

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
