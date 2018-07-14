import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()

wm.title = 'Populations of NA countries'

wm.add('North America', {'ca':43126000,'us':309349000,'mx':113423000})
wm.render_to_file('na_populations.svg')