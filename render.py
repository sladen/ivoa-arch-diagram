#!/usr/bin/env python2.7
# Pragmatic generator for International Virtual Observatory Association
# Architecture diagrams previously derived manually from:
# http://wiki.ivoa.net/internal/IVOA/VOArchitectureDiscussion/VOArchitecture.ppt
# Original Author: Christophe Arviset

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf
import io
MEDIABOX_PSPOINT = (720., 540.) # 10 inch * 7.5 inch == 254mm * 190.5 mm
MEDIABOX_INCHES = [dimension / 72. for dimension in MEDIABOX_PSPOINT]
CENTRE = 356.436

def x(position, index=0): return position / MEDIABOX_PSPOINT[index]
def y(position, index=1): return position / MEDIABOX_PSPOINT[index]

# inspiration http://www.programcreek.com/python/example/76380/matplotlib.font_manager.findfont
# There seems to be a long-standing bug/issue that the matplotlib font cache in:
# ~/.matplotlib/fontList.cache is never updated, so fonts installed after the
# first-time executation of matplotlib will never be found.
# SVN revision 8712 appears to have been the fix for this,
# which calls adds a new internal _rebuild() method, that
# in-turn uses pickle_dump() of an object into the cache file.
# https://sourceforge.net/p/matplotlib/mailman/matplotlib-checkins/thread/E1Oy9DR-0000BP-Of%40sfp-svn-5.v30.ch3.sourceforge.com/#msg26202308
# http://matplotlib.svn.sourceforge.net/matplotlib/?rev=8712&view=rev
# One possibility to add a clean workaround; the other is just
# to manually run:
#   rm ~/.matplotlib/fontList.cache
# and then on the next run the now-missing cache will be rebuilt...
#

def find_matplotlib_font(**kw):
    prop = matplotlib.font_manager.FontProperties(**kw)
    path = matplotlib.font_manager.findfont(prop, fallback_to_default=False)
    font = matplotlib.font_manager.FontProperties(fname=path)
    # finding of fonts is based on the following
    # stretch -> condensed
    # variant -> small-caps
    # weight -> bold
    # slant -> italic
    # size -> relative size (textual) or PS point size (numeric)
    # however ... requesting the size/etc via findfont, doesn't cause the
    # size to be set it requires an explicit ".set_size(NN)"..
    if kw.has_key('style'): font.set_style(kw['style'])
    if kw.has_key('weight'): font.set_weight(kw['weight'])
    if kw.has_key('variant'): font.set_variant(kw['variant'])
    if kw.has_key('size'): font.set_size(kw['size'])
    if kw.has_key('stretch'): font.set_stretch(kw['stretch'])
    #print (font)
    return font

def main():
    ringbinder = matplotlib.backends.backend_pdf.PdfPages('foobar.pdf')
    render_ivoa_architecture_diagram(level=0, target=ringbinder)
    render_ivoa_architecture_diagram(level=1, target=ringbinder)
    render_ivoa_architecture_diagram(level=2, target=ringbinder)
    #render_ivoa_architecture_diagram(level = 1, target=ringbinder)
    #with open('foobar.pdf', 'wb') as diskfile:
        #ramfile = io.BytesIO()
        #ramfile.seek(0) # rewind to prepare for write at the beginning
        #if True:
        #    #with matplotlib.backends.backend_pdf.PdfPages('hello.pdf') as ringbinder:
        #   render_ivoa_architecture_diagram(level = 0, target=ringbinder)
        #    render_ivoa_architecture_diagram(level = 1, target=ringbinder)
        #ramfile.seek(0) # rewind to prepare for reading from the beginning
        #pdfstream = ramfile.getvalue() # extract the giant string
        #diskfile.write(pdfstream)
    ringbinder.close()
    import subprocess
    subprocess.call(['pdftk', 'VOArchitecture-export-as-PDF.pdf','multistamp','foobar.pdf','output','both.pdf'])


def render_ivoa_architecture_diagram(level=1, target=None):
    matplotlib.rcParams['font.family'] = 'Arial'
    # Only available on newer versions, otherwise needs
    # passing explicitly to '.savefig(..., transparent=True)'
    if 'savefig.transparent' in matplotlib.rcParams.keys():
        matplotlib.rcParams['savefig.transparent'] = True

    # generate + set size
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(*MEDIABOX_INCHES)

    font = find_matplotlib_font(family='Arial', style='normal', variant='normal', weight='bold', size=18)
    fig.text(x(22.680), y(503.280),
             'LEVEL {:d}'.format(level),
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

    font = find_matplotlib_font(family='Arial', style='normal', variant='normal', weight='bold', size=18)
    # left and right
    if level == 0:
        left_text = '\n'.join('FINDING')
    elif 1 <= level <= 2:
        offset = {1: 0, 2: 74}[level]
        left_text = '\n'.join('REGISTRY')
        fig.text(x(129.5 - offset), y(264.5),
             left_text,
             fontproperties=font,
             horizontalalignment='center',
             linespacing=1.31,
             color='pink',
             verticalalignment='center')

    # righthand side is slightly shifted up
    if level == 0:
        fig.text(x(584), y(260+5),
                 '\n'.join('GETTING'),
                 linespacing=1.33,
                 fontproperties=font,
                 horizontalalignment='center',
                 verticalalignment='center')
    elif 1 <= level <= 2:
        offset = {1: 0, 2: 646-572.}[level]
        fig.text(x(572 + offset), y(260),
                 '\n'.join('DATA ACCESS'),
                 fontproperties=font,
                 linespacing=1.33,
                 horizontalalignment='center',
                 verticalalignment='center')
        fig.text(x(601 + offset), y(260),
                 '\n'.join('PROTOCOLS'),
                 fontproperties=font,
                 linespacing=1.33,
                 horizontalalignment='center',
                 verticalalignment='center')

    # italics
    if 1 <= level <= 2:
        font2 = find_matplotlib_font(family='Arial', style='italic', variant='normal', weight='bold', size=16)

        # User Layer
        fig.text(x(178.5), y(434),
                 'Browser Based\nApps',
                 fontproperties=font2,
                 linespacing=1.2,
                 horizontalalignment='center',
                 verticalalignment='center')
        fig.text(x(CENTRE), y(428),
                 'Desktop Apps',
                 fontproperties=font2,
                 linespacing=1.2,
                 horizontalalignment='center',
                 verticalalignment='center')
        fig.text(x(535.7), y(434),
                 'Script Based\nApps',
                 fontproperties=font2,
                 linespacing=1.2,
                 horizontalalignment='center',
                 verticalalignment='center')

        # Resource Layer
        fig.text(x(181), y(72),
                 'Storage',
                 fontproperties=font2,
                 horizontalalignment='center',
                 verticalalignment='center')
        fig.text(x(CENTRE), y(84),
                 'Data and Metadata Collection',
                 fontproperties=font2,
                 horizontalalignment='center',
                 verticalalignment='center')
        fig.text(x(545), y(72),
                 'Computation',
                 fontproperties=font2,
                 linespacing=1.2,
                 horizontalalignment='center',
                 verticalalignment='center')

        # VO Core
        fig.text(x(CENTRE), y(334),
                 'VO Query\nLanguages',
                 fontproperties=font2,
                 horizontalalignment='center',
                 verticalalignment='center')
        offset = {1: 0, 2: 276-263}[level]
        fig.text(x(485), y(263 + offset),
                 'Data Models'.replace(' ', '\n'),
                 fontproperties=font2,
                 horizontalalignment='center',
                 verticalalignment='center')
        fig.text(x(CENTRE), y(186),
                 'Formats',
                 fontproperties=font2,
                 horizontalalignment='center',
                 verticalalignment='center')
        fig.text(x(243), y(268),
                 'Semantics',
                 fontproperties=font2,
                 horizontalalignment='center',
                 verticalalignment='center')


    font = find_matplotlib_font(family='Arial', style='normal', variant='normal', weight='bold', size=12)
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

    font = find_matplotlib_font(family='Arial', style='normal', variant='normal', weight='bold', size=10)
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
    if target:
        target.savefig(fig, transparent=True)
        plt.close()
    return

    if False:
        with open('foobar.pdf', 'wb') as pdf:
            f = io.BytesIO()
            fig.savefig(f, format='pdf', transparent=True)
            fig.savefig(f, format='pdf')
            f.seek(0)
            f.seek(0)
            pdfstream = f.getvalue()
            pdf.write(pdfstream)
        

if __name__=='__main__':
    main()
