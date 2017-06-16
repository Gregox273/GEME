from fastkml import kml

def read(filename):
    with open(filename, 'rb') as kml_file:
        doc = kml_file.read()
#   doc = (fame).read()
    k = kml.KML()
    k.from_string(doc)
    return k

def getLatLon(k, y, x, count=0):
    if count > 20:
        raise RuntimeError('Reached 20 recursions of getLatLon')
    if not getattr(k, 'geometry',0):
        #x,y = getLatLon(k.features, count+1)
        for feature in k.features():
            getLatLon(feature, y, x, count+1)
    else:
        x.append(k.geometry.x)
        y.append(k.geometry.y)
    return

x1 = []
y1 = []
x2 = []
y2 = []
k1 = read("data/GIS/Schools.kml")
getLatLon(k1,y1,x1)
print(y1)
print(x1)
k2 = read("data/GIS/Licensed_Premises.kml")
getLatLon(k2,y2,x2)
