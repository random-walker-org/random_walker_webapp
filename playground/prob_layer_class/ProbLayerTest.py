import ProbLayer as pl
import matplotlib.pyplot as plt
import numpy as np

nRand = 50
zoom = 10
## Center in Auckland
center = {'lat': -36.85764758564406, 'lng': 174.76226806640625}
## Center in Taipei 
# center = {'lat': 25.0483397, 'lng': 121.5375121}
bounds = {'southWest': {'lat': -37.13842453422676, 'lng': 174.05914306640625}, 
          'northEast': {'lat': -36.57583533849175, 'lng': 175.46539306640625}}
size = {'lat': 512, 'lng': 1024}
learningPoints = {'lat': np.random.uniform(bounds['northEast']['lat'], 
                                           bounds['southWest']['lat'], nRand),
                  'lng': np.random.uniform(bounds['northEast']['lng'], 
                                           bounds['southWest']['lng'], nRand)}

## Create new grid
newGrid = pl.Grid(center, bounds, size)

## Create prior layer
priorLayer = pl.createPriorLayer(newGrid, 20)
plt.imshow(priorLayer.probLayer)
plt.show()

## Create Learning layer
learningLayer = pl.createLearningLayer(newGrid, 'normal', 0.3, learningPoints)
ymax, ymin, xmax, xmin = bounds['northEast']['lat'], bounds['southWest']['lat'], bounds['northEast']['lng'], bounds['southWest']['lng']

fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(learningLayer.probLayer, #cmap=plt.cm.gist_earth_r,
          extent=[xmin, xmax, ymin, ymax])
ax.plot(learningPoints['lng'], learningPoints['lat'], 'k.', markersize=10)
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])
plt.show()


## Create Feasible Layer
feasibleLayer = pl.createFeasibleLayer(newGrid, zoom)
plt.imshow(feasibleLayer.probLayer)
plt.show()


## Create final Layer
finalLayer = priorLayer * learningLayer * feasibleLayer
plt.imshow(finalLayer.probLayer)
plt.show()
