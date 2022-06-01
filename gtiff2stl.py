import sys
import numpy
from osgeo import gdal
from stl import mesh

base = 1
population_scale = 640


def make_cube(h):
    # Define the 8 vertices of the cube
    vertices = numpy.array([
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, h + base],
        [1, 0, h + base],
        [1, 1, h + base],
        [0, 1, h + base]])
    # Define the 12 triangles composing the cube
    faces = numpy.array([
        [0, 3, 1],
        [1, 3, 2],
        [0, 4, 7],
        [0, 7, 3],
        [4, 5, 6],
        [4, 6, 7],
        [5, 1, 2],
        [5, 2, 6],
        [2, 3, 6],
        [3, 7, 6],
        [0, 1, 5],
        [0, 5, 4]])

    # Create the mesh
    cube = mesh.Mesh(numpy.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            cube.vectors[i][j] = vertices[f[j], :]

    return cube


if len(sys.argv) < 2:
    print('Usage: {} <file.stl>'.format(sys.argv[0]))
    exit(1)

dataset = gdal.Open(sys.argv[1])

print('Opening {}'.format(sys.argv[1]))

if not dataset:
    print('Failed to open: {}'.format(sys.argv[1]))
    exit(1)

print('Driver: {}/{}'.format(dataset.GetDriver().ShortName,
      dataset.GetDriver().LongName))

band = dataset.GetRasterBand(1)

data = band.ReadAsArray()  # data = gdal_array.LoadFile(sys.argv[1])
nodata = band.GetNoDataValue()
max_population = numpy.amax(data)

print('Size is: {} x {} x {}'.format(dataset.RasterXSize,
      dataset.RasterYSize, int(max_population / population_scale)))
print('Max population: {}'.format(max_population))

# replace nodata wiht 0
data[data == nodata] = 0

# create a base
data[data == 0] = base

columns = len(data[0])
rows = len(data)

vertices = []
for x in range(rows):
    for y in range(columns):
        h = data[x][y] / population_scale
        m = make_cube(h)
        m.y += y
        m.x += x
        vertices.append(m.data.copy())

m = mesh.Mesh(numpy.concatenate(vertices))

m.save(sys.argv[1] + '.stl')

dataset = None
