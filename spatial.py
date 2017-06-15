from fastkml import kml

def read(filename):
   with open(filename, 'rb') as kml_file:
      doc = kml_file.read()
#   doc = (fame).read()
   k = kml.KML()
   k.from_string(doc)
   return k

k = read("data/GIS/Licensed_Premises.kml")


features = list(k.features())
print(features)
f2 = list(features[0].features())
f3 = list(f2[0].features())
#print(f3[0].geometry.x)
#print(f3[0].geometry.y)

#f4 = list(f3[0].geometry())
#print(f4)
