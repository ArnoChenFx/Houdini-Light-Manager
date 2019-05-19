from AN_LightManager import LightManager
reload(LightManager)
LightWindow = LightManager.LightManagerWindow()
hou.session.lightManager = LightWindow 
LightWindow.show()
