#coding:utf-8
from PySide2 import QtWidgets ,QtGui,QtCore
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import hou
import math
import json
import os

class anLineEdit(QLineEdit):
    editedSignal = Signal()
    
    def __init__(self):
        super(anLineEdit,self).__init__()

    def emitEditedSignal(self):
        self.editedSignal.emit()

class lightTable(QTableWidget):
    def __init__(self,render):
        super(lightTable,self).__init__()
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.setSelectionMode(QAbstractItemView.NoSelection)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setObjectName("hHeader")
        self.hbarValue = self.horizontalScrollBar().value()
        self.vbarValue = self.verticalScrollBar().value()

        self.render = render
        self.param = None
        self.iconPath = os.path.split(os.path.realpath(__file__))[0] + "/icons/"
        self.iconPath = self.iconPath.replace("\\","/")

        self.size = 23
        self.setStyle()

    def initUI(self):
        if self.render == "Redshift":
            self.initRS()
        elif self.render == "Arnold":
            self.initAR()
        elif self.render == "Mantra":
            self.initMR()
        elif self.render == "Octane":
            self.initOR()

    def initRS(self):
        self.setColumnCount(len(self.param))
        self.setHorizontalHeaderLabels(self.param)

        myDict ={}
        for idx , i in enumerate(self.param):
            myDict[i] = idx

        #set size
        if " " in self.param:
            self.setColumnWidth(myDict[" "],31)
        if "Type" in self.param:
            self.setColumnWidth(myDict["Type"],100)
        if "Color" in self.param:
            self.setColumnWidth(myDict["Color"],50)
        if "Intensity" in self.param:
            self.setColumnWidth(myDict["Intensity"],200)
        if "Exposure" in self.param:
            self.setColumnWidth(myDict["Exposure"],200)
        if "Enable" in self.param:
            self.setColumnWidth(myDict["Enable"],80)
        if "Viewport" in self.param:
            self.setColumnWidth(myDict["Viewport"],80)
        if "Samples" in self.param:
            self.setColumnWidth(myDict["Samples"],80)
        if "Mode" in self.param:
            self.setColumnWidth(myDict["Mode"],100)
        if "Temperature" in self.param:
            self.setColumnWidth(myDict["Temperature"],100)
        if "Volume Contribution" in self.param:
            self.setColumnWidth(myDict["Volume Contribution"],130)
        if "Volume Sample" in self.param:
            self.setColumnWidth(myDict["Volume Sample"],120)
        if "Light Group" in self.param:
            self.setColumnWidth(myDict["Light Group"],200)
        if "Look At" in self.param:
            self.setColumnWidth(myDict["Look At"],150)
        if "Look At Up Vector" in self.param:
            self.setColumnWidth(myDict["Look At Up Vector"],150)

    def initAR(self):
        self.setColumnCount(len(self.param))
        self.setHorizontalHeaderLabels(self.param)

        myDict ={}
        for idx , i in enumerate(self.param):
            myDict[i] = idx

        #set size
        if " " in self.param:
            self.setColumnWidth(myDict[" "],31)
        if "Type" in self.param:
            self.setColumnWidth(myDict["Type"],100)
        if "Color" in self.param:
            self.setColumnWidth(myDict["Color"],50)
        if "Intensity" in self.param:
            self.setColumnWidth(myDict["Intensity"],200)
        if "Exposure" in self.param:
            self.setColumnWidth(myDict["Exposure"],200)
        if "Enable" in self.param:
            self.setColumnWidth(myDict["Enable"],80)
        if "Viewport" in self.param:
            self.setColumnWidth(myDict["Viewport"],80)
        if "Samples" in self.param:
            self.setColumnWidth(myDict["Samples"],80)
        if "Normalize" in self.param:
            self.setColumnWidth(myDict["Normalize"],100)
        if "Volume Sample" in self.param:
            self.setColumnWidth(myDict["Volume Sample"],150)
        if "Light Group" in self.param:
            self.setColumnWidth(myDict["Light Group"],200)
        if "Look At" in self.param:
            self.setColumnWidth(myDict["Look At"],150)
        if "Look At Up Vector" in self.param:
            self.setColumnWidth(myDict["Look At Up Vector"],150)

    def initMR(self):
        self.setColumnCount(len(self.param))
        self.setHorizontalHeaderLabels(self.param)

        myDict ={}
        for idx , i in enumerate(self.param):
            myDict[i] = idx
        #set size
        if " " in self.param:
            self.setColumnWidth(myDict[" "],31)
        if "Type" in self.param:
            self.setColumnWidth(myDict["Type"],100)
        if "Color" in self.param:
            self.setColumnWidth(myDict["Color"],50)
        if "Intensity" in self.param:
            self.setColumnWidth(myDict["Intensity"],200)
        if "Exposure" in self.param:
            self.setColumnWidth(myDict["Exposure"],200)
        if "Enable" in self.param:
            self.setColumnWidth(myDict["Enable"],80)
        if "Viewport" in self.param:
            self.setColumnWidth(myDict["Viewport"],80)
        if "Samples" in self.param:
            self.setColumnWidth(myDict["Samples"],80)
        if "Shadow Intensity" in self.param:
            self.setColumnWidth(myDict["Shadow Intensity"],150)
        if "Look At" in self.param:
            self.setColumnWidth(myDict["Look At"],150)
        if "Look At Up Vector" in self.param:
            self.setColumnWidth(myDict["Look At Up Vector"],150)

    def initOR(self,):
        self.setColumnCount(len(self.param))
        self.setHorizontalHeaderLabels(self.param)

        myDict ={}
        for idx , i in enumerate(self.param):
            myDict[i] = idx
        #set size
        if " " in self.param:
            self.setColumnWidth(myDict[" "],31)
        if "Type" in self.param:
            self.setColumnWidth(myDict["Type"],100)
        if "Color" in self.param:
            self.setColumnWidth(myDict["Color"],50)
        if "Intensity" in self.param:
            self.setColumnWidth(myDict["Intensity"],200)
        if "Enable" in self.param:
            self.setColumnWidth(myDict["Enable"],80)
        if "Viewport" in self.param:
            self.setColumnWidth(myDict["Viewport"],80)
        if "Emission Type" in self.param:
            self.setColumnWidth(myDict["Emission Type"],100)
        if "Samples" in self.param:
            self.setColumnWidth(myDict["Visibility"],80)
        if "Shadow Intensity" in self.param:
            self.setColumnWidth(myDict["Temperature"],150)
        if "Look At" in self.param:
            self.setColumnWidth(myDict["Look At"],150)
        if "Look At Up Vector" in self.param:
            self.setColumnWidth(myDict["Look At Up Vector"],150)

    def addSlider(self,minV,maxV):
        slider = QWidget()
        slider.setStyleSheet("border: 0px solid red")

        slider_layout = QHBoxLayout()
        slider_value =  anLineEdit()
        slider_slider = QSlider(Qt.Horizontal)
        slider_layout.addWidget(slider_value)
        slider_layout.addWidget(slider_slider)
        slider.setLayout(slider_layout)

        slider_slider.count = 0
        slider_slider.setMinimum(minV*500)
        slider_slider.setMaximum(maxV*500)
        slider_slider.valueChanged.connect(lambda: slider_value.setText(self.evalFloat(maxV,slider_slider,slider_value)))
        slider_value.editingFinished.connect(lambda: slider_slider.setValue(float(self.toDigit(slider_value))*500.0))
        slider_value.editedSignal.connect(lambda: slider_slider.setValue(float(self.toDigit(slider_value))*500.0))

        slider_value.setMaximumWidth(80)
        slider_value.setStyleSheet("color:rgb(180,180,180);background-color:rgb(35,35,35)")
        slider_layout.setMargin(0)
        self.setSliderStyle(slider_slider)

        return slider ,slider_value 

    def addCombBox(self,names=[]):
        combBox = QComboBox()
        combBox.setStyleSheet("QComboBox{border:0.5px solid gray;}"
                "QComboBox QAbstractItemView::item{height:25px;}"
                "QComboBox::drop-down{border:0px;}")
        combBox.addItems(names)
        combBox.setStyleSheet("border:0px")

        return combBox

    def evalFloat(self,maxV,slider,slider_value):
        value = float(slider_value.text())

        if value>maxV and slider.count == 0:
            slider.count = 1
            return str(value)
        else:
            slider.count = 0
            return str('%.2f'%(slider.value()/500.0))

    def setColorStyle(self,myColor,color):
        myColor.setStyleSheet('''
        QPushButton{
            background-color: rgb(%s, %s, %s);
            border: 10px rgb(40,40,40)
        }
        QPushButton:pressed{
            border: 3px solid gray
        }
        ''' %(color[0]*255.0,color[1]*255.0,color[2]*255.0))

    def toDigit(self,textLine):
        if not textLine.text()[0].isdigit() or not textLine.text()[-1].isdigit():
            textLine.setText("0")
            return 0
        return textLine.text()

    def setSliderStyle(self,slider):
        slider.setStyleSheet('''  
            QSlider::add-page:Horizontal
            {     
                background-color: rgb(87, 97, 106);
                height:4px;
            }
            QSlider::sub-page:Horizontal 
            {
                background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(231,80,229, 255), stop:1 rgba(7,208,255, 255));
                height:4px;
            }
            QSlider::groove:Horizontal 
            {
                background:transparent;
                height:6px;
            }
        ''')

    def setStyle(self):
        self.setStyleSheet('''
        QPushButton{
            color:rgb(180,180,180);
            background-color:rgb(65,65,65);
            border:0px;
        }
        QPushButton:pressed{
            background-color:rgb(80,80,80);
        }
        QTableView{
            gridline-color: rgb(80,80,80);
        }
        QHeaderView#hHeader::section {
            gridline-color: rgb(80,80,80);
            color: rgb(170,170,170);
            height : 11px;
            font : 13px
        }
        ''')

    def setColor(self,parm,myColor):
        default =  hou.Color(parm.eval()[0],parm.eval()[1],parm.eval()[2])
        col =  hou.ui.selectColor(default)
        if col:
            col = col.rgb()
            parm.set(col)
            self.setColorStyle(myColor,col)

    def setNode(self,parm,myButton):
        nodePath = hou.ui.selectNode(initial_node = hou.node("/obj"),node_type_filter = hou.nodeTypeFilter.Obj)
        if nodePath:
            parm.set(nodePath)
            myButton.setText(nodePath)

    def readRS(self,node):
        tpName = node.type().name()
        
        myIcon = QLabel()
        myName = QPushButton()
        myType = QLabel()
        myColor = QPushButton()
        myInten ,myInten_value = self.addSlider(0,10) 
        myExpose ,myExpose_value = self.addSlider(0,2) 
        myEnable = QCheckBox()
        myViewport = QCheckBox()
        mySample = QLineEdit()
        myTemperature = QLineEdit()
        myMode = self.addCombBox()
        myLightType = self.addCombBox()
        myVC = QLineEdit()
        myVS = QLineEdit()
        myGroup = QLineEdit()

        count = self.rowCount()
        self.insertRow(count)
        index = 0

        #attribute
        tp = ""
        color = (255.0,255.0,255.0)
        intensity = 100
        multiply = 1
        exposure = 0
        sampleValue = 0
        volumeC = node.evalParm("RSL_volumeScale")
        volumeS = node.evalParm("RSL_volumeSamples")
        myLookAt = QPushButton()
        myUp = self.addCombBox()

        inten_name = None
        expose_name = None
        temperature_name = None
        mode_name = None
        color_name = "light_color"

        #add type
        if(tpName == "rslight"):
            tp = node.parm("light_type").evalAsString()
            myLightType.addItems(["Distant","Point","Spot","Area"])
            myLightType.setCurrentIndex(int(node.evalParm("light_type")))
            myLightType.currentIndexChanged.connect(lambda:node.parm("light_type").set(myLightType.currentIndex()))

            color = node.parmTuple("light_color").eval()
            intensity = node.evalParm("RSL_intensityMultiplier")
            inten_name = "RSL_intensityMultiplier"
            multiply = 100
            exposure = node.evalParm("Light1_exposure")
            expose_name = "Light1_exposure"
            myMode.addItems(["Color","Temperature","Temperature And Color"])
            myMode.setCurrentIndex(int(node.evalParm("Light1_colorMode")))
            mode_name = "Light1_colorMode"
            myTemperature.setText(str(node.evalParm("Light1_temperature")))
            temperature_name = "Light1_temperature"
            sampleValue = node.evalParm("RSL_samples")

        elif("rslightdome" in tpName):
            tp = "dome"
            color = node.parmTuple("light_color").eval()
            intensity = node.evalParm("light_intensity")
            inten_name = "light_intensity"
            exposure = node.evalParm("RSL_exposure")
            expose_name = "RSL_exposure"
            sampleValue = node.evalParm("RSL_samples")

        elif("ies" in tpName):
            tp = "ies"
            color = node.parmTuple("color").eval()
            color_name = "color"
            intensity = node.evalParm("multiplier")
            inten_name = "multiplier"
            exposure = node.evalParm("Light_IES1_exposure")
            expose_name = "Light_IES1_exposure"
            myMode.addItems(["Color","Temperature"])
            myMode.setCurrentIndex(int(node.evalParm("colorMode")))
            mode_name = "colorMode"
            myTemperature.setText(str(node.evalParm("temperature")))
            temperature_name = "temperature"

        elif("portal" in tpName):
            tp = "portal"
            color = node.parmTuple("Light_Portal1_tint_color").eval()
            color_name = "Light_Portal1_tint_color"
            intensity = node.evalParm("Light_Portal1_multiplier")
            inten_name = "Light_Portal1_multiplier"
            exposure = node.evalParm("Light_Portal1_exposure")
            expose_name = "Light_Portal1_exposure"
            sampleValue = node.evalParm("RSL_samples")

        elif("sun" in tpName):
            tp = "sun"
            color = node.parmTuple("PhysicalSky1_ground_color").eval()
            color_name = "PhysicalSky1_ground_color"
            intensity = node.evalParm("PhysicalSun1_multiplier")
            inten_name = "PhysicalSun1_multiplier"
            exposure = node.evalParm("PhysicalSun1_sun_disk_scale")
            expose_name = "PhysicalSun1_sun_disk_scale"

        #============================
        tp = tp.capitalize() 

        #add icon
        if " " in self.param:
            tex = self.iconPath + "rs.png"
            pixMap = QPixmap(tex).scaled(self.size,self.size)
            myIcon.setPixmap(pixMap)
            self.setCellWidget(count,index,myIcon)
            index += 1

        #add name
        if "Name" in self.param:
            myName.setText(node.name())
            myName.clicked.connect(lambda: node.setCurrent(1,1))
            myName.setStyleSheet("Text-align:left")
            self.setCellWidget(count,index,myName)
            index += 1

        #add type
        if "Type" in self.param:
            if(tpName == "rslight"):
                self.setCellWidget(count,index,myLightType)
            else:   
                myType.setText(tp)
                myType.setStyleSheet("Text-align:left")
                self.setCellWidget(count,index,myType)
            index += 1

        #add color
        if "Color" in self.param:
            self.setColorStyle(myColor,color)
            self.setCellWidget(count,index,myColor)
            myColor.clicked.connect(lambda:self.setColor(node.parmTuple(color_name),myColor))
            index += 1

        #add intensity
        if "Intensity" in self.param:
            self.setCellWidget(count,index,myInten)
            myInten_value.setText(str(intensity/multiply))
            myInten_value.emitEditedSignal()
            myInten_value.textChanged.connect(lambda: node.parm(inten_name).set(float(myInten_value.text())*multiply))
            index += 1
        
        #add exposure
        if "Exposure" in self.param:
            self.setCellWidget(count,index,myExpose)
            myExpose_value.setText(str(exposure))
            myExpose_value.emitEditedSignal()
            myExpose_value.textChanged.connect(lambda: node.parm(expose_name).set(float(myExpose_value.text())))
            index += 1

        #add myEnable
        if "Enable" in self.param:
            self.setCellWidget(count,index,myEnable)
            myEnable.setChecked(node.evalParm("light_enabled"))
            myEnable.stateChanged.connect(lambda:node.parm("light_enabled").set(myEnable.isChecked()))
            index += 1

        #add myViewport
        if "Viewport" in self.param:
            self.setCellWidget(count,index,myViewport)
            self.updateGeometries()
            myViewport.setChecked(node.evalParm("ogl_enablelight"))
            myViewport.stateChanged.connect(lambda:node.parm("ogl_enablelight").set(myViewport.isChecked()))
            index += 1

        #add sample
        if "Samples" in self.param:
            if tp == "Portal" or tp == "Dome" or tp == "Area":
                mySample.setText(str(sampleValue))
                self.setCellWidget(count,index,mySample)
                mySample.editingFinished.connect(lambda:node.parm("RSL_samples").set(math.floor(float(self.toDigit(mySample)))))
            index += 1

        #add mode
        if "Mode" in self.param:
            if tpName == "rslight" or tp == "Ies":
                myMode.currentIndexChanged.connect(lambda:node.parm(mode_name).set(str(myMode.currentIndex())))
                self.setCellWidget(count,index,myMode)
            index += 1

        #add temperature
        if "Temperature" in self.param:
            if tpName == "rslight" or tp == "Ies":
                myTemperature.editingFinished.connect(lambda:node.parm(temperature_name).set(float(self.toDigit(myTemperature))))
                self.setCellWidget(count,index,myTemperature)
            index += 1

        #add volumeC
        if "Volume Contribution" in self.param:
            myVC.setText(str(volumeC))
            self.setCellWidget(count,index,myVC)
            myVC.editingFinished.connect(lambda:node.parm("RSL_volumeScale").set(float(self.toDigit(myVC))))
            index += 1

        #add volumeS
        if "Volume Sample" in self.param:
            myVS.setText(str(volumeS))
            self.setCellWidget(count,index,myVS)
            myVS.editingFinished.connect(lambda:node.parm("RSL_volumeSamples").set(math.floor(float(self.toDigit(myVS)))))
            index += 1

        #add group
        if "Light Group" in self.param:
            if tp != "Portal":
                myGroup.setText(node.parm("RSL_lightGroup").evalAsString())
                myGroup.editingFinished.connect(lambda:node.parm("RSL_lightGroup").set(myGroup.text()))
                self.setCellWidget(count,index,myGroup)
            index += 1

        #add target
        if "Look At" in self.param:
            if node.parm("lookatpath") is not None:
                myLookAt.setText(node.parm("lookatpath").evalAsString())
                myLookAt.clicked.connect(lambda:self.setNode(node.parm("lookatpath"),myLookAt))
                self.setCellWidget(count,index,myLookAt)
            index += 1

        #add upvector
        if "Look At Up Vector" in self.param:
            if node.parm("lookup") is not None:
                myUp.addItems(["Don't Use Up Vector","Use Up Vector","Use Quaternions","Use Global Position","Use Up Object"])
                upDict = {"off":0,"on":1,"quat":2,"pos":3,"obj":4}
                upList  = ["off","on","quat","pos","obj"]
                if node.parm("lookup").eval() != "":
                    myUp.setCurrentIndex(upDict[node.parm("lookup").eval()])
                    myUp.currentIndexChanged.connect(lambda:node.parm("lookup").set(upList[myUp.currentIndex()]))
                self.setCellWidget(count,index,myUp)

    def readAR(self,node):
        myIcon = QLabel()
        myName = QPushButton()
        myType = self.addCombBox()
        myColor = QPushButton()
        myInten ,myInten_value = self.addSlider(0,10) 
        myExpose ,myExpose_value = self.addSlider(0,2) 
        myEnable = QCheckBox()
        myViewport = QCheckBox()
        mySample = QLineEdit()
        myNormalize = QCheckBox()
        myVS = QLineEdit()
        myGroup = QLineEdit()
        myLookAt = QPushButton()
        myUp = self.addCombBox()

        count = self.rowCount()
        self.insertRow(count)
        index = 0

        #add icon
        if " " in self.param:
            tex = self.iconPath + "ar.png"
            pixMap = QPixmap(tex).scaled(self.size,self.size)
            myIcon.setPixmap(pixMap)
            self.setCellWidget(count,index,myIcon)
            index += 1

        #add name
        if "Name" in self.param:
            myName.setText(node.name())
            myName.clicked.connect(lambda: node.setCurrent(1,1))
            myName.setStyleSheet("Text-align:left")
            self.setCellWidget(count,index,myName)
            index += 1

        #add type
        if "Type" in self.param:
            myType.addItems(["Point","Distant","Spot","Quad","Disk","Cylinder","Skydom","Mesh","Photometric"])
            myType.setCurrentIndex(node.parm("ar_light_type").eval())
            myType.currentIndexChanged.connect(lambda:node.parm("ar_light_type").set(myType.currentIndex()))
            self.setCellWidget(count,index,myType)
            index += 1

        #add color
        if "Color" in self.param:
            color = node.parmTuple("ar_color").eval()
            self.setColorStyle(myColor,color)
            self.setCellWidget(count,index,myColor)
            myColor.clicked.connect(lambda:self.setColor(node.parmTuple("ar_color"),myColor))
            index += 1

        #add intensity
        if "Intensity" in self.param:
            self.setCellWidget(count,index,myInten)
            myInten_value.setText(str(node.parm("ar_intensity").eval()))
            myInten_value.emitEditedSignal()
            myInten_value.textChanged.connect(lambda: node.parm("ar_intensity").set(float(myInten_value.text())))
            index += 1


        #add exposure
        if "Exposure" in self.param:
            self.setCellWidget(count,index,myExpose)
            myExpose_value.setText(str(node.parm("ar_exposure").eval()))
            myExpose_value.emitEditedSignal()
            myExpose_value.textChanged.connect(lambda: node.parm("ar_exposure").set(float(myExpose_value.text())))
            index += 1


        #add myEnable
        if "Enable" in self.param:
            self.setCellWidget(count,index,myEnable)
            myEnable.setChecked(node.evalParm("light_enable"))
            myEnable.stateChanged.connect(lambda:node.parm("light_enable").set(myEnable.isChecked()))
            index += 1


        #add myViewport
        if "Viewport" in self.param:
            self.setCellWidget(count,index,myViewport)
            self.updateGeometries()
            myViewport.setChecked(node.evalParm("ogl_enablelight"))
            myViewport.stateChanged.connect(lambda:node.parm("ogl_enablelight").set(myViewport.isChecked()))
            index += 1

        #add sample
        if "Samples" in self.param:
            mySample.setText(str(node.parm("ar_samples").eval()))
            self.setCellWidget(count,index,mySample)
            mySample.editingFinished.connect(lambda:node.parm("ar_samples").set(math.floor(float(self.toDigit(mySample)))))
            index += 1

        #add normalize
        if "Normalize" in self.param:
            self.setCellWidget(count,index,myNormalize)
            self.updateGeometries()
            myNormalize.setChecked(node.evalParm("ar_normalize"))
            myNormalize.stateChanged.connect(lambda:node.parm("ar_normalize").set(myNormalize.isChecked()))
            index += 1

        #add volumeS
        if "Volume Sample" in self.param:
            myVS.setText(str(node.parm("ar_volume_samples").eval()))
            self.setCellWidget(count,index,myVS)
            myVS.editingFinished.connect(lambda:node.parm("ar_volume_samples").set(math.floor(float(self.toDigit(myVS)))))
            index += 1

        #add group
        if "Light Group" in self.param:
            myGroup.setText(node.parm("ar_aov").evalAsString())
            myGroup.editingFinished.connect(lambda:node.parm("ar_aov").set(myGroup.text()))
            self.setCellWidget(count,index,myGroup)
            index += 1

        #add target
        if "Look At" in self.param:
            myLookAt.setText(node.parm("lookatpath").evalAsString())
            myLookAt.clicked.connect(lambda:self.setNode(node.parm("lookatpath"),myLookAt))
            self.setCellWidget(count,index,myLookAt)
            index += 1

        #add upvector
        if "Look At Up Vector" in self.param:
            myUp.addItems(["Don't Use Up Vector","Use Up Vector","Use Quaternions","Use Global Position","Use Up Object"])
            upDict = {"off":0,"on":1,"quat":2,"pos":3,"obj":4}
            upList  = ["off","on","quat","pos","obj"]
            myUp.setCurrentIndex(upDict[node.parm("lookup").eval()])
            myUp.currentIndexChanged.connect(lambda:node.parm("lookup").set(upList[myUp.currentIndex()]))
            self.setCellWidget(count,index,myUp)

    def readMR(self,node):
        myIcon = QLabel()
        myName = QPushButton()
        myType = self.addCombBox()
        myType2 = QLabel()
        myColor = QPushButton()
        myInten ,myInten_value = self.addSlider(0,10) 
        myExpose ,myExpose_value = self.addSlider(0,2) 
        myEnable = QCheckBox()
        myViewport = QCheckBox()
        mySample = QLineEdit()
        myShadow = QLineEdit()
        myLookAt = QPushButton()
        myUp = self.addCombBox()

        count = self.rowCount()
        self.insertRow(count)
        tp = node.type().name()
        index = 0

        #add icon
        if " " in self.param:
            tex = self.iconPath + "mr.png"
            pixMap = QPixmap(tex).scaled(self.size,self.size)
            myIcon.setPixmap(pixMap)
            self.setCellWidget(count,index,myIcon)
            index += 1

        #add name
        if "Name" in self.param:
            myName.setText(node.name())
            myName.clicked.connect(lambda: node.setCurrent(1,1))
            myName.setStyleSheet("Text-align:left")
            self.setCellWidget(count,index,myName)
            index += 1

        #add type
        if "Type" in self.param:
            if tp == "envlight":
                myType2.setText("Environment")
                self.setCellWidget(count,index,myType2)
            elif tp == "ambient":
                myType2.setText("Ambient")
                self.setCellWidget(count,index,myType2)
            elif tp =="indirectlight":
                myType.addItems(["Indirect Global Photo Map","Direct Global Photo Map","Caustic Photo Map","Irradiance Only"])
                typeDict = {"indirectglobal":0,"global":1,"caustic":2,"indirect":3}
                typeList  = ["indirectglobal","global","caustic","indirect"]
                myType.setCurrentIndex(typeDict[node.parm("light_type").eval()])
                myType.currentIndexChanged.connect(lambda:node.parm("light_type").set(typeList[myType.currentIndex()]))
                self.setCellWidget(count,index,myType)
            else:
                myType.addItems(["Point","Line","Grid","Disk","Sphere","Tube","Geometry","Distant","Sun"])
                myType.setCurrentIndex(node.parm("light_type").eval())
                myType.currentIndexChanged.connect(lambda:node.parm("light_type").set(myType.currentIndex()))
                self.setCellWidget(count,index,myType)
            index += 1

        #add color
        if "Color" in self.param:
            color = node.parmTuple("light_color").eval()
            self.setColorStyle(myColor,color)
            self.setCellWidget(count,index,myColor)
            myColor.clicked.connect(lambda:self.setColor(node.parmTuple("light_color"),myColor))
            index += 1

        #add intensity
        if "Intensity" in self.param:
            self.setCellWidget(count,index,myInten)
            myInten_value.setText(str(node.parm("light_intensity").eval()))
            myInten_value.emitEditedSignal()
            myInten_value.textChanged.connect(lambda: node.parm("light_intensity").set(float(myInten_value.text())))
            index += 1

        #add exposure
        if "Exposure" in self.param:
            if tp != "ambient":
                self.setCellWidget(count,index,myExpose)
                myExpose_value.setText(str(node.parm("light_exposure").eval()))
                myExpose_value.emitEditedSignal()
                myExpose_value.textChanged.connect(lambda: node.parm("light_exposure").set(float(myExpose_value.text())))
            index += 1

        #add myEnable
        if "Enable" in self.param:
            self.setCellWidget(count,index,myEnable)
            myEnable.setChecked(node.evalParm("light_enable"))
            myEnable.stateChanged.connect(lambda:node.parm("light_enable").set(myEnable.isChecked()))
            index += 1

        #add myViewport
        if "Viewport" in self.param:
            self.setCellWidget(count,index,myViewport)
            self.updateGeometries()
            myViewport.setChecked(node.evalParm("ogl_enablelight"))
            myViewport.stateChanged.connect(lambda:node.parm("ogl_enablelight").set(myViewport.isChecked()))
            index += 1

        #add sample
        if "Samples" in self.param:
            if tp != "ambient":
                mySample.setText(str(node.parm("vm_samplingquality").eval()))
                self.setCellWidget(count,index,mySample)
                mySample.editingFinished.connect(lambda:node.parm("vm_samplingquality").set(math.floor(float(self.toDigit(mySample)))))
            index += 1

        #add shadow
        if "Shadow Intensity" in self.param:
            if tp != "ambient" and tp != "indirectlight":
                myShadow.setText(str(node.parm("shadow_intensity").eval()))
                self.setCellWidget(count,index,myShadow)
                myShadow.editingFinished.connect(lambda:node.parm("shadow_intensity").set(math.floor(float(self.toDigit(myShadow)))))
            index += 1

        #add target
        if "Look At" in self.param:
            if node.parm("lookatpath") is not None:
                myLookAt.setText(node.parm("lookatpath").evalAsString())
                myLookAt.clicked.connect(lambda:self.setNode(node.parm("lookatpath"),myLookAt))
                self.setCellWidget(count,index,myLookAt)
            index += 1

        #add upvector
        if "Look At Up Vector" in self.param:
            if node.parm("lookup") is not None:
                myUp.addItems(["Don't Use Up Vector","Use Up Vector","Use Quaternions","Use Global Position","Use Up Object"])
                upDict = {"off":0,"on":1,"quat":2,"pos":3,"obj":4}
                upList  = ["off","on","quat","pos","obj"]
                if node.parm("lookup").eval() in upList:
                    myUp.setCurrentIndex(upDict[node.parm("lookup").eval()])
                    myUp.currentIndexChanged.connect(lambda:node.parm("lookup").set(upList[myUp.currentIndex()]))
                self.setCellWidget(count,index,myUp)

    def readOR(self,node):
        myIcon = QLabel()
        myName = QPushButton()
        myType = self.addCombBox()
        myEmissionType = self.addCombBox()
        myColor = QPushButton()
        myInten ,myInten_value = self.addSlider(0,10) 
        myEnable = QCheckBox()
        myViewport = QCheckBox()
        mySample = QLineEdit()
        myVis = QLineEdit()
        myTemperature = QLineEdit()
        myLookAt = QPushButton()
        myUp = self.addCombBox()

        count = self.rowCount()
        self.insertRow(count)
        index = 0
        tp = node.type().name()

        #attribute
        inten_name = "NT_EMIS_BLACKBODY1_power"
        sample_name = "NT_EMIS_BLACKBODY1_sampling_rate"
        color_name = "NT_MAT_DIFFUSE1_diffuse"

        if node.parm("switch") is not None and node.parm("switch").eval() == 1:#texture
            inten_name = "NT_EMIS_TEXTURE1_power"
            sample_name = "NT_EMIS_TEXTURE1_sampling_rate"

        if tp == "octane_toonLight":
            inten_name = "light_intensity"
            color_name = "light_color"
            

        #add icon
        if " " in self.param:
            tex = self.iconPath + "or.png"
            pixMap = QPixmap(tex).scaled(self.size,self.size)
            myIcon.setPixmap(pixMap)
            self.setCellWidget(count,index,myIcon)
            index += 1

        #add name
        if "Name" in self.param:
            myName.setText(node.name())
            myName.clicked.connect(lambda: node.setCurrent(1,1))
            myName.setStyleSheet("Text-align:left")
            self.setCellWidget(count,index,myName)
            index += 1

        #add type
        if "Type" in self.param:
            if tp == "octane_toonLight":
                myType.addItems(["Distant","Point"])
                myType.setCurrentIndex(node.parm("light_type").eval())
                myType.currentIndexChanged.connect(lambda:node.parm("light_type").set(myType.currentIndex()))
            else:
                myType.addItems(["Quad","Circle","Sphere","Torus","Tube","Sportlight"])
                myType.setCurrentIndex(node.parm("light_type").eval())
                myType.currentIndexChanged.connect(lambda:node.parm("light_type").set(myType.currentIndex()))
            self.setCellWidget(count,index,myType)
            index += 1

        
        #add color
        if "Color" in self.param:
            color = node.parmTuple(color_name).eval()
            self.setColorStyle(myColor,color)
            self.setCellWidget(count,index,myColor)
            myColor.clicked.connect(lambda:self.setColor(node.parmTuple(color_name),myColor))
            index += 1

        #add intensity
        if "Intensity" in self.param:
            self.setCellWidget(count,index,myInten)
            myInten_value.setText(str(node.parm(inten_name).eval()))
            myInten_value.emitEditedSignal()
            myInten_value.textChanged.connect(lambda: node.parm(inten_name).set(float(myInten_value.text())))
            index += 1


        #add myEnable
        if "Enable" in self.param:
            self.setCellWidget(count,index,myEnable)
            myEnable.setChecked(node.evalParm("light_enable"))
            myEnable.stateChanged.connect(lambda:node.parm("light_enabled").set(myEnable.isChecked()))
            index += 1


        #add myViewport
        if "Viewport" in self.param:
            self.setCellWidget(count,index,myViewport)
            self.updateGeometries()
            myViewport.setChecked(node.evalParm("ogl_enablelight"))
            myViewport.stateChanged.connect(lambda:node.parm("ogl_enablelight").set(myViewport.isChecked()))
            index += 1

        
        #add emission type
        if "Emission Type" in self.param:
            if tp != "octane_toonLight":
                myEmissionType.addItems(["BlackBody","Texture"])
                myEmissionType.setCurrentIndex(node.parm("switch").eval())
                myEmissionType.currentIndexChanged.connect(lambda:node.parm("switch").set(myEmissionType.currentIndex()))
                self.setCellWidget(count,index,myEmissionType)
            index += 1

        #add sample
        if "Samples" in self.param:
            if tp != "octane_toonLight":
                mySample.setText(str(node.parm(sample_name).eval()))
                self.setCellWidget(count,index,mySample)
                mySample.editingFinished.connect(lambda:node.parm(sample_name).set(math.floor(float(self.toDigit(mySample)))))
            index += 1

        #add visibality
        if "Visibility" in self.param:
            if tp != "octane_toonLight":
                myVis.setText(str(node.parm("octane_objprop_generalVis").eval()))
                self.setCellWidget(count,index,myVis)
                myVis.editingFinished.connect(lambda:node.parm("octane_objprop_generalVis").set(float(self.toDigit(myVis))))
            index += 1

        #add temperature
        if "Temperature" in self.param:
            if tp != "octane_toonLight" and node.parm("switch").eval() == 0:
                myTemperature.setText(str(node.parm("NT_EMIS_BLACKBODY1_temperature").eval()))
                self.setCellWidget(count,index,myTemperature)
                myTemperature.editingFinished.connect(lambda:node.parm("NT_EMIS_BLACKBODY1_temperature").set(math.floor(float(self.toDigit(myTemperature)))))
            index += 1

        #add target
        if "Look At" in self.param:
            myLookAt.setText(node.parm("lookatpath").evalAsString())
            myLookAt.clicked.connect(lambda:self.setNode(node.parm("lookatpath"),myLookAt))
            self.setCellWidget(count,index,myLookAt)
            index += 1

        #add upvector
        if "Look At Up Vector" in self.param:
            myUp.addItems(["Don't Use Up Vector","Use Up Vector","Use Quaternions","Use Global Position","Use Up Object"])
            upDict = {"off":0,"on":1,"quat":2,"pos":3,"obj":4}
            upList  = ["off","on","quat","pos","obj"]
            myUp.setCurrentIndex(upDict[node.parm("lookup").eval()])
            myUp.currentIndexChanged.connect(lambda:node.parm("lookup").set(upList[myUp.currentIndex()]))
            self.setCellWidget(count,index,myUp)

    def update(self,changeColumn = True):
        self.hbarValue = self.horizontalScrollBar().value()
        self.vbarValue = self.verticalScrollBar().value()
        #height = self.height()
        #width = self.width()

        self.clear()
        self.setRowCount(0)
        if changeColumn:
            self.setColumnCount(0)
            self.initUI()
        else:
            self.setColumnCount(len(self.param))
            self.setHorizontalHeaderLabels(self.param)

        self.horizontalScrollBar().setValue(self.hbarValue)
        self.verticalScrollBar().setValue(self.vbarValue)
        #self.setGeometry(0,0,width,height)

class LightMagager(QMainWindow):
    def __init__(self):
        super(LightMagager,self).__init__()
        self.setWindowTitle('ARNO_Light Manager')
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  
        self.resize(800,200)
        self.setStyle()

        self.initAttribute()
        self.initUI()
        self.update(True)

    def initAttribute(self):
        self.useRS = True
        self.useAR = True
        self.useMR = True
        self.useOR = True

        self.arParams = [" ","Name","Type","Color","Intensity",
        "Exposure","Enable","Viewport","Samples","Normalize",
        "Volume Sample","Light Group","Look At","Look At Up Vector"]
        self.arActions = []
        self.currentArParams = self.arParams

        self.rsParams = [" ","Name","Type","Color","Intensity",
        "Exposure","Enable","Viewport","Samples","Mode","Temperature",
        "Volume Contribution","Volume Sample","Light Group",
        "Look At","Look At Up Vector"]
        self.rsActions = []
        self.currentRsParams = self.rsParams

        self.orParams = [" ","Name","Type","Color","Intensity",
        "Enable","Viewport","Emission Type","Samples","Visibility",
        "Temperature","Look At","Look At Up Vector"]
        self.orActions = []
        self.currentOrParams = self.orParams

        self.mrParams = [" ","Name","Type","Color","Intensity",
        "Exposure","Enable","Viewport","Samples",
        "Shadow Intensity","Look At","Look At Up Vector"]
        self.mrActions = []
        self.currentMrParams = self.mrParams

    
    def setStyle(self):
        self.setStyleSheet("border:0px")

    def initUI(self):
        self.widget = QWidget()
        self.addMenuBar()
        self.onLoad()

        self.tables = []
        self.docks = []
        self.rsDock ,self.rsTable = self.addDock("Redshift")
        self.arDock ,self.arTable = self.addDock("Arnold")
        self.mrDock ,self.mrTable = self.addDock("Mantra")
        self.orDock ,self.orTable = self.addDock("Octane")

        self.splitDockWidget(self.rsDock,self.arDock,Qt.Vertical)
        self.splitDockWidget(self.arDock,self.mrDock,Qt.Vertical)
        self.splitDockWidget(self.mrDock,self.orDock,Qt.Vertical)

        self.rsTable.param = self.currentRsParams
        self.arTable.param = self.currentArParams
        self.orTable.param = self.currentOrParams
        self.mrTable.param = self.currentMrParams

    def addDock(self,name):
        table = lightTable(name)
        dock = QDockWidget(name, self)
        dock.setWidget(table)
        self.addDockWidget(Qt.TopDockWidgetArea, dock)
        self.tables.append(table)
        self.docks.append(dock)
        self.setDockNestingEnabled(True)
        return dock,table

    def addAction(self,name,menu):
        rd = QAction(name, self)
        rd.setCheckable(True)
        rd.setChecked(True)
        rd.triggered.connect(lambda: self.setUse(name,rd.isChecked()))
        menu.addAction(rd)
        return rd

    def addMenuBar(self):
        self.MenuBar = self.menuBar()
        self.MenuBar.setFixedHeight(30)
        fileMenu = self.MenuBar.addMenu('File')

        save = QAction("Save Settings", self)
        save.triggered.connect(self.onSave)
        fileMenu.addAction(save)
        load = QAction("Load Settings", self)
        load.triggered.connect(self.onLoad)
        fileMenu.addAction(load)

        renderMenu = self.MenuBar.addMenu('Renderer')
        self.useRSAction = self.addAction("Redshift",renderMenu)
        self.useARAction =self.addAction("Arnold",renderMenu)
        self.useMRAction =self.addAction("Mantra",renderMenu)
        self.useORAction =self.addAction("Octane",renderMenu)

        
        rsMenu = self.MenuBar.addMenu('Redshift')
        for i in self.rsParams:
            self.rsActions.append(self.addAction(i,rsMenu))

        arMenu = self.MenuBar.addMenu('Arnold')
        for i in self.arParams:
            self.arActions.append(self.addAction(i,arMenu))
        
        mrMenu = self.MenuBar.addMenu('Mantra')
        for i in self.mrParams:
            self.mrActions.append(self.addAction(i,mrMenu))

        orMenu = self.MenuBar.addMenu('Octane')
        for i in self.orParams:
            self.orActions.append(self.addAction(i,orMenu))

        refreshButton = QPushButton("Refresh",self.MenuBar)
        refreshButton.clicked.connect(self.update)
        self.MenuBar.setCornerWidget(refreshButton,Qt.TopRightCorner)

    def setUse(self,renderer,state):
        if(renderer == "Redshift"):
            self.useRS = state
            self.rsDock.setVisible(state)
        elif(renderer == "Arnold"):
            self.useAR = state
            self.arDock.setVisible(state)
        elif(renderer == "Mantra"):
            self.useMR = state
            self.mrDock.setVisible(state)
        elif(renderer == "Octane"):
            self.useOR = state
            self.orDock.setVisible(state)

        self.update(True)

    def setParams(self,actions,table):
        currentParams = []
        for i in actions:
            if i.isChecked():
                currentParams.append(i.text())
        table.param = currentParams
        return currentParams

    def loadParams(self,params,actions,currentParams):
        for idx,parm in enumerate(params):
                act = actions[idx]
                if parm not in currentParams:
                    act.setChecked(False)
                else:
                    act.setChecked(True)

    def onSave(self):
        file = hou.getenv("temp")+"/AN_LightManager.json"

        info = {}
        info["useRS"] = self.useRS
        info["useAR"] = self.useAR
        info["useMR"] = self.useMR
        info["useOR"] = self.useOR
        info["Redshift"] = self.currentRsParams
        info["Arnold"] = self.currentArParams
        info["Mantra"] = self.currentMrParams
        info["Octane"] = self.currentOrParams

        with open(file, "w") as f:
            f.write(json.dumps(info, indent=4))
            print "Save Successfully!"

    def onLoad(self):
        file = hou.getenv("temp")+"/AN_LightManager.json"

        if not os.path.exists(file):
            #print "Preference file dose not exist!"
            return

        with open(file, "r") as f:
            info = json.loads(f.read())
            self.useRS = info["useRS"]
            self.useRSAction.setChecked(self.useRS)
            self.useAR = info["useAR"]
            self.useARAction.setChecked(self.useAR)
            self.useMR = info["useMR"]
            self.useMRAction.setChecked(self.useMR)
            self.useOR = info["useOR"]
            self.useORAction.setChecked(self.useOR)

            self.currentRsParams = info["Redshift"]
            self.currentArParams = info["Arnold"]
            self.currentMrParams = info["Mantra"]
            self.currentOrParams = info["Octane"]

            self.loadParams(self.rsParams,self.rsActions,self.currentRsParams)
            self.loadParams(self.arParams,self.arActions,self.currentArParams)
            self.loadParams(self.mrParams,self.mrActions,self.currentMrParams)
            self.loadParams(self.orParams,self.orActions,self.currentOrParams)
   
    def update(self,changeColumn = False):
        self.currentRsParams = self.setParams(self.rsActions,self.rsTable)
        self.currentArParams = self.setParams(self.arActions,self.arTable)
        self.currentMrParams = self.setParams(self.mrActions,self.mrTable)
        self.currentOrParams = self.setParams(self.orActions,self.orTable)

        for table in self.tables:
            table.update(changeColumn = changeColumn)
        for dock in self.docks:
            dock.setVisible(False)
        
        mantraTypes = ["hlight","hlight::2.0","envlight","ambient","indirectlight"]
        octaneTypes = ["octane_light","octane_toonLight"]

        nodes = list(hou.node("/obj/").children())

        for i in nodes:
            tpName = i.type().name()
            if "rslight" in tpName and self.useRS:
                self.rsDock.setVisible(True)
                self.rsTable.readRS(i)
            elif "arnold_light" == tpName and self.useAR:
                self.arDock.setVisible(True)
                self.arTable.readAR(i)
            elif tpName in mantraTypes and self.useMR:
                self.mrDock.setVisible(True)
                self.mrTable.readMR(i)
            elif tpName in octaneTypes and self.useOR:
                self.orDock.setVisible(True)
                self.orTable.readOR(i)

def LoadWindow():
    window = LightMagager()
    hou.session.hdri_haven = window 
    window.show()        
    