import tmt
from os.path import join

class Project(tmt.EclipseProject):
	def configure(self):
		tmt.EclipseProject.configure(self)
		tmt.Server.addPlugin(self)
		self.nonJavaSrcDeps += [ 'tnoodleServerHandler/scrambler-interface/' ]

Project(tmt.projectName(), description="A generic competition scramble generator interface.")