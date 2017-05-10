import csv
from BeautifulSoup import BeautifulSoup
pws = {}
reader = csv.reader(open('DamHazardbyState.csv'), delimiter=",")
for row in reader:
    try:
        #full_fips = row[0] + row[1]
        count = float( row[1].strip() )
        pws[row[0]] = count
    except:
        pass
svg = open('USstates.svg', 'r').read()
soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])
paths = soup.findAll('path')
colors = ["#F1EEF6", "#D7B5D8", "#DF65B0", "#DD1C77", "#980043"]
path_style = 'fill:#d0d0d0;fill-rule:nonzero;stroke:#000000;stroke-width:0.178287;fill:'
for p in paths:

    if p['id'] not in ["State_Lines", "separator"]:

        try:
             count = pws[p['id']]
        except:
            continue
        #print str(float(len(colors)-1) * float(count - 0) / float(119 - 0))

        # if count > 120:
        #     color_class = 4
        if count> 1000:
            color_class = 5
        # elif count > 90:
        #     color_class = 3
        elif count > 400:
            color_class = 4
        # elif count > 60:
        #     color_class = 2
        elif count> 200:
            color_class = 3
        # elif count > 30:
        #     color_class = 1
        elif count> 100:
            color_class = 2
        else:
            color_class = 1


        color = colors[color_class]
        p['style'] = path_style + color

print soup.prettify()
