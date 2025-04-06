from description_harvester.plugins import Plugin

class MyPlugin(Plugin):
	plugin_name = "manifests"

	def __init__(self):
		print (f"Setup {self.plugin_name} plugin for reading digital object data from IIIF manifests.")

		# Set up any prerequisites or checks here


	def read_data(self, dao):
		#print (f"reading data from {dao.identifier}")

		print (dao.identifier)
		
		# Add or override dao here
		# dao.metadata = {}

		return dao
