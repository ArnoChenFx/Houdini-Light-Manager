#ARNO
#Created by ARNO on 2018.6
#ARNO_Light Manager V1.0
from PySide2 import (QtCore,QtWidgets,QtGui)
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QWidget, QSlider, QVBoxLayout,QHBoxLayout,QColorDialog,QSpinBox,QDoubleSpinBox,QLineEdit)
from PySide2.QtGui import QPixmap
import os
import hou
 
class LightM(QWidget):
    def __init__(self):
        super(LightM,self).__init__()
        #create main layout
        self.setWindowTitle('ARNO_Light Manager')
        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        #set background color & font
        color = QtGui.QColor(QtGui.QColor(58, 58, 58)).name()
        self.setStyleSheet("QLabel{background-color:%s}""QWidget{background-color:%s}"  
                   "QLabel{color:rgb(170,160,150,250);font-size:20px;font-family:Vegur Bold;}"  
                   "QLabel:hover{color:rgb(100,100,100,250);}" % (color,color))  

        #custom val
        self.LightManger=0
            #path
        script_path = os.path.realpath(__file__)
        script_dir = os.path.dirname(script_path)
        self.icon = script_dir+"/icons/"
        #add items
        self.addAllitems()

    def addAllitems(self):    
        #create parm
        width = 800
        self.addMenu(width)

        path = ["/obj"]
        obj = hou.nodes(path)
        lights = obj[0].children()
        num=0
        for i in lights:
            if i.parmTuple("light_color") is not None or i.parmTuple("PhysicalSky1_night_color") is not None:
                num+=1
                name = i.name()
                self.createItem(name,width)

        self.resize(width,num*30+10)
        self.mainLayout.addStretch(1)

    def addMenu(self,width):
        w = (width-150)/2-5
        hbox1 = QHBoxLayout()
        refresh=QtWidgets.QPushButton(self)
        refresh.setStyleSheet("background-color: rgb(89, 89, 92);")
        refresh.setMinimumSize(QtCore.QSize(20, 20))
        refresh.setMaximumSize(QtCore.QSize(20, 20))
        refresh.setText("R")

        name=QtWidgets.QLabel(self)
        name.setText("|Name")
        name.setMaximumWidth(155)
        name.setMinimumWidth(155)

        lighttype=QtWidgets.QLabel(self)
        lighttype.setText("|LightType")
        lighttype.setMaximumWidth(102)
        lighttype.setMinimumWidth(102)

        color=QtWidgets.QLabel(self)
        color.setText("|Cd")
        color.setMaximumWidth(38)
        color.setMinimumWidth(38)

        inten=QtWidgets.QLabel(self)
        inten.setText("|Intensity")
        inten.setMaximumWidth(w)
        inten.setMinimumWidth(w)

        expo=QtWidgets.QLabel(self)
        expo.setText("|Exposure")
        expo.setMaximumWidth(w)
        expo.setMinimumWidth(w)

        enable=QtWidgets.QLabel(self)
        enable.setText("|On")
        enable.setMaximumWidth(30)
        enable.setMinimumWidth(30)

        viewport=QtWidgets.QLabel(self)
        viewport.setText("|VP")
        viewport.setMaximumWidth(30)
        viewport.setMinimumWidth(30)

        #set alien
        name.setAlignment(Qt.AlignLeft) 
        #add item
        hbox1.addWidget(refresh)
        hbox1.addWidget(name)
        hbox1.addWidget(lighttype)
        hbox1.addWidget(color)
        hbox1.addWidget(inten)
        hbox1.addWidget(expo)
        hbox1.addWidget(enable)
        hbox1.addWidget(viewport)
         
        hbox1.addStretch(1)
        self.mainLayout.addLayout(hbox1)
        refresh.clicked.connect(self.refreshLayout)

    def createItem(self,name,width):
        #create items
        hbox = QHBoxLayout()

        icon=QtWidgets.QLabel(self)
        txt=QtWidgets.QPushButton(self)
        lcolor = QtWidgets.QPushButton(self)
        lcd = QLineEdit(self)
        slider = QSlider(Qt.Horizontal,self)
        lcd1 =  QLineEdit(self)
        slider1 = QSlider(Qt.Horizontal,self)
        enable = QtWidgets.QCheckBox(self)
        view = QtWidgets.QCheckBox(self)
        lighttype=QtWidgets.QLabel(self)
        
        #get light type
        w = (width-150)/2-70
        path = '/obj/'+name
        light = hou.node(path)
        ltype = 3#"rs"
        inten = 1
        valmulty = 1
        exposure = 0
        rstype = 1
        tex = ""
        color = {1,1,1}
        enableV = 1
        vp = light.evalParm("ogl_enablelight")
        typeName = ""
        #get light type
        mantra = ["Point","Line","Grid","Disk","Sphere","Tube","Geometry","Distant","Sun"]
        arnold = ["Point","Distant","Spot","Quad","Disk","Cylinder","Skydome","Mesh","Photometric"]
        redshift = ["Distant","Point","Spot","Area"]
        #"mantra"
        if light.parm("light_intensity") != None:
            if light.parm("light_contrib") != None:
                tex = "amantra.png"  
                inten = light.evalParm("light_intensity")
                exposure = light.evalParm("light_exposure")
                ltype = 1#"mantra"
                color = light.parmTuple("light_color").eval()
                enableV = light.evalParm("light_enable")
                if light.parm("light_type") != None:
                    idx = light.evalParm("light_type")
                    typeName = mantra[idx]
                else:
                    typeName = "sky/Env"

        #"ar"
        if light.parm("ar_intensity") != None:
            tex = "aar.png"
            inten = light.evalParm("ar_intensity")
            exposure = light.evalParm("ar_exposure")
            ltype = 2#"ar"
            color = light.parmTuple("ar_color").eval()
            enableV = light.evalParm("light_enable")
            idx = light.evalParm("ar_light_type")
            typeName = arnold[idx]
        #"rs"
        if light.parm("RSL_intensityMultiplier") != None:
            tex = "ars.png"
            inten = light.evalParm("RSL_intensityMultiplier")
            exposure = light.evalParm("Light1_exposure")
            ltype = 3#"rs"
            valmulty = 100
            rstype = 1#normal
            color = light.parmTuple("light_color").eval()
            enableV = light.evalParm("light_enabled")
            if light.parm("light_type") != None:
                idx = light.evalParm("light_type")
                typeName = redshift[idx]

        if light.parm("PhysicalSun1_multiplier") != None:
            tex = "ars.png"
            inten = light.evalParm("PhysicalSun1_multiplier")
            exposure = light.evalParm("PhysicalSun1_sun_disk_scale")
            ltype = 3#"rs"
            rstype = 2#sun
            color = light.parmTuple("PhysicalSky1_ground_color").eval()
            enableV = light.evalParm("light_enabled")
            typeName = "Sun"
        if light.parm("multiplier") != None:
            tex = "ars.png"
            inten = light.evalParm("multiplier")
            exposure = light.evalParm("Light_IES1_exposure")
            ltype = 3#"rs"
            rstype = 3#ies
            color = light.parmTuple("color").eval()
            enableV = light.evalParm("light_enabled")
            typeName = "Ies"
        if light.parm("RSL_exposure") != None:
            tex = "ars.png" 
            inten = light.evalParm("light_intensity")
            exposure = light.evalParm("RSL_exposure")
            ltype = 3#"rs"
            rstype = 4#dome
            color = light.parmTuple("light_color").eval()
            enableV = light.evalParm("light_enabled")
            typeName = "Dome"

        #set defalt value
        tex =self.icon+tex
        size = 25 
        #icon
        icon.setMinimumSize(QtCore.QSize(size, size))
        icon.setMaximumSize(QtCore.QSize(size, size))
        pixMap = QPixmap(tex).scaled(icon.width(),icon.height())
        icon.setPixmap(pixMap)
        #name
        txt.setText(name)
        txt.setStyleSheet("font: 11pt \"Vegur Bold\";""text-align:left")
        txt.setMinimumSize(QtCore.QSize(150, size+5))
        txt.setMaximumSize(QtCore.QSize(150, size+5))
        #ltype
        lighttype.setText("|"+typeName)
        lighttype.setMaximumWidth(105)
        lighttype.setMinimumWidth(105)
        #color
        lcolor.setStyleSheet("background-color: rgb(%s, %s, %s);"% (color[0]*255.0,color[1]*255.0,color[2]*255.0))
        lcolor.setMinimumSize(QtCore.QSize(40, size))
        lcolor.setMaximumSize(QtCore.QSize(40, size))
        #iten
        lcd.setText(str(inten/valmulty))
        lcd.setMaxLength(5) 
        lcd.setMaximumWidth(60)
        lcd.setMinimumWidth(60)
        #lcd.setSingleStep(0.01)
        lcd.setStyleSheet("selection-background-color: rgb(100, 100,100);"
"background-color:rgb(58, 58, 58);"
"font: 10pt \"Vegur Bold\";")
        slider.setMaximum(5000)
        slider.setValue(500*inten/valmulty)
        slider.setMaximumWidth(w)
        slider.setMinimumWidth(w)
        #exposure
        lcd1.setText(str(exposure))
        lcd1.setMaxLength(5) 
        lcd1.setMaximumWidth(60)
        lcd1.setMinimumWidth(60)
        lcd1.setStyleSheet("selection-background-color: rgb(100, 100,100);"
"background-color:rgb(58, 58, 58);"
"font: 10pt \"Vegur Bold\";")
        slider1.setMinimum(-5000)
        slider1.setMaximum(5000)
        slider1.setValue(500*exposure)
        slider1.setMaximumWidth(w)
        slider1.setMinimumWidth(w)
        #enable
        enable.setMinimumSize(QtCore.QSize(30, size))
        enable.setMaximumSize(QtCore.QSize(30, size))
        enable.setStyleSheet("QCheckBox::indicator { width: 25px; height: 25px;}")
        enable.setChecked(enableV)
        #view
        view.setMinimumSize(QtCore.QSize(30, size))
        view.setMaximumSize(QtCore.QSize(30, size))
        view.setStyleSheet("QCheckBox::indicator { width: 25px; height: 25px;}")
        view.setChecked(vp)

        #add item to mainLayout
        hbox.addWidget(icon)
        hbox.addWidget(txt)
        hbox.addWidget(lighttype)
        hbox.addWidget(lcolor)
        #iten
        hbox.addWidget(lcd)
        hbox.addWidget(slider)
        #exposure
        hbox.addWidget(lcd1)
        hbox.addWidget(slider1)
        #enalbe
        hbox.addWidget(enable)
        #view
        hbox.addWidget(view)

        hbox.addStretch(1)
        self.mainLayout.addLayout(hbox)

        #creat connections
        txt.clicked.connect(lambda: self.selectLight(light))
        #color
        lcolor.clicked.connect(lambda: self.selectColor(light,ltype,rstype))
        #iten
        lcd.returnPressed.connect(lambda: slider.setValue(float(lcd.text())*500.0))
        slider.valueChanged.connect(lambda: lcd.setText(str('%.2f'%(slider.value()/500.0))))
        slider.valueChanged.connect(lambda: self.setLightIntensity(float('%.2f'%(slider.value()/500.0)),light,ltype,rstype))
             #slider.valueChanged.connect(lambda: self.selectLight(light))
        #exposure
        lcd1.returnPressed.connect(lambda: slider1.setValue(float(lcd1.text())*500.0))
        slider1.valueChanged.connect(lambda: lcd1.setText(str('%.2f'%(slider1.value()/500.0))))
        slider1.valueChanged.connect(lambda: self.setLightExposure(float('%.2f'%(slider1.value()/500.0)),light,ltype,rstype))
             #slider1.valueChanged.connect(lambda: self.selectLight(light))
        #enable
        enable.stateChanged.connect(lambda: self.setEnable(enable.isChecked(),light,ltype,rstype))
        #viewport
        view.stateChanged.connect(lambda: self.setViewPort(view.isChecked(),light))

    def selectColor(self,light,ltype,rstype):
        #col = hou.ui.selectColor()
        col=QColorDialog.getColor()
        r = col.red()/255.0
        g = col.green()/255.0
        b = col.blue()/255.0
        col = (r,g,b)
        self.setColor(col,light,ltype,rstype)
        
    def setColor(self,color,light,ltype,rstype):
        if ltype==1:#"mantra"
            light.parmTuple("light_color").set(color)
        if ltype==2:#"ar"
            light.parmTuple("ar_color").set(color)
        if ltype==3:#"rs"
            if rstype==1:
                light.parmTuple("light_color").set(color)
            if rstype==2:
                light.light.parmTuple("PhysicalSky1_ground_color").set(color)
            if rstype==3:
                light.parmTuple("color").set(color)
            if rstype==4:
                light.parmTuple("light_color").set(color)
        self.refreshLayout()

    def setLightIntensity(self,data,light,ltype,rstype):
        #print light.name()
        if ltype==1:#"mantra"
            light.setParms({"light_intensity":data})
        if ltype==2:#"ar"
            light.setParms({"ar_intensity":data})
        if ltype==3:#"rs"
            if rstype==1:
                light.setParms({"RSL_intensityMultiplier":data*100.0})
            if rstype==2:
                light.setParms({"PhysicalSun1_multiplier":data})
            if rstype==3:
                light.setParms({"multiplier":data})
            if rstype==4:
                light.setParms({"light_intensity":data})

    def setLightExposure(self,data,light,ltype,rstype):
        if ltype==1:#"mantra"
            light.setParms({"light_exposure":data})
        if ltype==2:#"ar"
            light.setParms({"ar_exposure":data})
        if ltype==3:#"rs"
            if rstype==1:
                light.setParms({"Light1_exposure":data})
            if rstype==2:
                light.setParms({"PhysicalSun1_sun_disk_scale":data})
            if rstype==3:
                light.setParms({"Light_IES1_exposure":data})
            if rstype==4:
                light.setParms({"RSL_exposure":data})

    def setEnable(self,data,light,ltype,rstype):
        if ltype==1:#"mantra"
            light.setParms({"light_enable":data})
        if ltype==2:#"ar"
            light.setParms({"light_enable":data})
        if ltype==3:#"rs"
            light.setParms({"light_enabled":data})
            if rstype==1:
                light.setParms({"Light1_on":data})
            if rstype==2:
                light.setParms({"PhysicalSun1_on":data,"PhysicalSky1_on":data})
            if rstype==3:
                light.setParms({"on":data})
            if rstype==4:
                light.setParms({"on":data})

    def setViewPort(self,data,light):
        light.setParms({"ogl_enablelight":data})
                
    def selectLight(self,light):
        light.setCurrent(1,1)
        #self.refreshLayout()

    def refreshLayout(self):
        def deleteItems(layout):
            if layout is not None:
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()
                    else:
                        deleteItems(item.layout())
        deleteItems(self.mainLayout)
        self.addAllitems()

    def closeEvent(self,event):
        self.setParent(None)

def refreshWindow():
    windows = hou.qt.mainWindow().children()
    for window in windows:
        if isinstance(window,QWidget):
            if hasattr(window, "LightManger"):
                window.close()

    window = LightM()
    window.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)
    window.show()