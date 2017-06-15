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

latitudes = []
longitudes = []
k = read("data/GIS/Licensed_Premises.kml")
getLatLon(k,latitudes,longitudes)
print(latitudes)
print(longitudes)
