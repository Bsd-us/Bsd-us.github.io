import json
import re

from pathlib import Path

toHeight = 8
backgroundWidth = 1920
backgroundHeight = 1080

# Loading flex coordinates from json file containing the coordinates of each img of each type of svg
with open('coordinates.json', 'r') as coosFile:
    coos = json.load(coosFile)
    
# Creating the result svg file
with open('../images/background.svg', 'w') as resultSvgFile:
    resultSvgFile.write(f'<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{backgroundWidth}" height="{backgroundHeight}">\n')
    sumUse = ""

    # Going through each svg file
    for svgFile in Path('svg/').iterdir():
        lenCoos = len(coos[svgFile.stem][0])
        assert lenCoos == len(coos[svgFile.stem][1])

        with open(svgFile, 'r', encoding='utf-8') as f:
            svgLines = f.read()

        # Getting the initial size of the svg
        width = re.findall(r'width="[\d\.]+"', svgLines)[0][7:-1]
        height = re.findall(r'height="[\d\.]+"', svgLines)[0][8:-1]

        # Writing to the result file, the svg to be used as a symbol
        svgLines = re.sub(r'<svg.*xmlns:v="https://vecta.io/nano"', f'\t<symbol id="{svgFile.stem}" viewBox="0 0 {width} {height}"', svgLines)
        svgLines = svgLines.replace('</svg>', '</symbol>\n')
        resultSvgFile.write(svgLines)

        # Going through each occurence of the svg
        for i in range(lenCoos):
            # Offsetting a bit the coordinates since flex didn't take into account outer borders
            x = coos[svgFile.stem][0][i] + toHeight / 2
            y = coos[svgFile.stem][1][i] + toHeight / 2

            # Since the background is 1920x1080, we only keep the occurences that are in the background because we used a random amount of images to completely fill it
            # We don't bother with checking if the occurence outside width because flex-wrap ensures that
            if y < backgroundHeight:

                # Adapting initial svg size to the target height, keeping the ratio
                newWidth = (float(width) * toHeight) / float(height)

                # For each occurence of the svg, adding a use tag with the corresponding coordinates
                sumUse += f'\t<use xlink:href="#{svgFile.stem}" x="{x}" y="{y}" width="{newWidth}" height="{toHeight}"/>\n'
    
    # Tracing limits of the background to help visualize (add more backgroundHeight to see the bottom border)
    # resultSvgFile.write(f'\t<svg><rect x="0" y="0" width="{backgroundWidth}" height="{backgroundHeight}" fill="none" stroke="white"/></svg>\n')

    # Writing the uses to the result file
    resultSvgFile.write(sumUse)
    resultSvgFile.write('</svg>')
