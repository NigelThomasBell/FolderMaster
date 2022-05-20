# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FolderMaster.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
import sys
import collections
import re
import platform
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets

basedir = os.path.dirname(__file__)
try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

"""
    TODO LIST:
    * Regarding same name but different case usage: 
        * If the folder doesn't exist, choose which version to use
            * Store each varient in a list in a dictionary (eg {apple: [Apple, apple]})
        * If the file does exist, find all instances of the same name (maybe turn them into lower case), and make duplicate folders using the original folder name
    * Pop up boxes to handle:
        * Faulty names
        * Same name (choose which one to use) 
    * handle tabs
"""
reservedCharacters = []
subfolderDividers = []
reservedFileNames = []
if platform.system() == "Windows":
    reservedCharacters = ["<", ">", ":", "|", "?", "*"] #Note: "\" and "/" are also reserved, but are used to create subfolders.
    subfolderDividers = ["\\", "/"]
    reservedFileNames = [
        "CON", 
        "PRN", 
        "AUX", "NUL", 
        "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", 
        "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"
    ]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.directory = str(os.getcwd()[0].upper()) + str(os.getcwd()[1:])

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 520)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 520))
        MainWindow.setMaximumSize(QtCore.QSize(400, 520))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(basedir, 'images', "app_logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.sourceButton = QtWidgets.QPushButton(self.centralwidget)
        self.sourceButton.setGeometry(QtCore.QRect(355, 15, 30, 30))
        self.sourceButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(os.path.join(basedir, 'images', "folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sourceButton.setIcon(icon1)
        self.sourceButton.setObjectName("sourceButton")
        self.sourceButton.clicked.connect(MainWindow.chooseDirectory)

        self.directoryTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.directoryTextbox.setGeometry(QtCore.QRect(72, 15, 280, 30))
        self.directoryTextbox.setObjectName("directoryTextbox")
        self.directoryTextbox.setText(self.directory)

        self.folderNames = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.folderNames.setGeometry(QtCore.QRect(20, 109, 364, 331))
        self.folderNames.setObjectName("folderNames")

        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setGeometry(QtCore.QRect(274, 455, 111, 31))
        self.createButton.setObjectName("createButton")
        self.createButton.clicked.connect(MainWindow.createFolders)

        self.directoryLabel = QtWidgets.QLabel(self.centralwidget)
        self.directoryLabel.setGeometry(QtCore.QRect(20, 23, 47, 13))
        self.directoryLabel.setObjectName("directoryLabel")

        self.folderNamesLabel = QtWidgets.QLabel(self.centralwidget)
        self.folderNamesLabel.setGeometry(QtCore.QRect(20, 60, 71, 16))
        self.folderNamesLabel.setObjectName("folderNamesLabel")

        self.duplicateFoldersCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.duplicateFoldersCheckbox.setGeometry(QtCore.QRect(20, 83, 200, 17))
        self.duplicateFoldersCheckbox.setObjectName("duplicateFoldersCheckbox")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        MainWindow.setMenuBar(self.menubar)
        self.actionOpenNameListFile = QtWidgets.QAction(MainWindow)
        self.actionOpenNameListFile.setObjectName("actionOpenNameListFile")
        self.actionOpenNameListFile.triggered.connect(MainWindow.openNameListFile)
        self.actionSaveNameListFile = QtWidgets.QAction(MainWindow)
        self.actionSaveNameListFile.setObjectName("actionSaveNameListFile")
        self.actionSaveNameListFile.triggered.connect(MainWindow.saveNameListFile)

        self.menuFile.addAction(self.actionOpenNameListFile)
        self.menuFile.addAction(self.actionSaveNameListFile)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FolderMaster"))
        self.createButton.setText(_translate("MainWindow", "Create Folders"))
        self.directoryLabel.setText(_translate("MainWindow", "Directory:"))
        self.folderNamesLabel.setText(_translate("MainWindow", "Folder Names:"))
        self.duplicateFoldersCheckbox.setText(_translate("MainWindow", "Create cumulative duplicate folders"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpenNameListFile.setText(_translate("MainWindow", "Open name list file"))
        self.actionOpenNameListFile.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSaveNameListFile.setText(_translate("MainWindow", "Save name list file"))
        self.actionSaveNameListFile.setShortcut(_translate("MainWindow", "Ctrl+S"))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.directory = self.ui.directoryTextbox.text()
    
    def openWindow(self, namecases):
        w = CaseStyleWindow(namecases)
        w.exec_()
        return w.selectedCase

    def chooseDirectory(self):
        previousDirectoryTextCopy = self.ui.directoryTextbox.text()
        folder = QtWidgets.QFileDialog.getExistingDirectory(
            self, 
            "Choose Directory to Insert Files"
        )
        if folder == "":
            folder = previousDirectoryTextCopy
        folder = folder.replace("/", "\\")
        self.ui.directoryTextbox.setText(folder)

    def createFolders(self):
        #print("Current directory content", os.listdir())
        if self.directory == "":
            QtWidgets.QMessageBox.question(
                self, 
                'No Source Folder',
                "Please provide a source folder",
                QtWidgets.QMessageBox.Ok
            )
            return
        if not os.path.exists(self.directory):
            QtWidgets.QMessageBox.question(
                self, 
                'Folder does not exist',
                "Please provide an existing source folder",
                QtWidgets.QMessageBox.Ok
            )
            return
        rawNamesList = self.ui.folderNames.toPlainText()
        despacedNamesList = [
            x.strip()
            for x in rawNamesList.split("\n") 
            if x.strip()
        ]
        #print(despacedNamesList)
        validNamesList = []
        validLeadingNamesList = []
        subfoldersList = []
        #faultyNamesList = []
        originalOrderDict = {}
        letterCasesDict = {}
        subfoldersDict = {}
        for i in range(len(despacedNamesList)): #Windows filename properties
            isSublist = False
            currentName = despacedNamesList[i]
            #print(currentName)

            if currentName[0] in ["/"] or currentName[-1] in ["/"]:
                #print("With:", currentName)
                currentName = currentName.strip("/")
                #print("Without:", currentName)
            if currentName[0] in ["\\"] or currentName[-1] in ["\\"]:
                #print("With:", currentName)
                currentName = currentName.strip("\\")
                #print("Without:", currentName)
            
            #Note: Maybe handle cancelations
            if currentName[-1] == ".":
                #print("With:", currentName)
                currentName = currentName.rstrip(".")
                #print("Without:", currentName)
            
            #NOTE: Collect faulty names
            if currentName.upper() in reservedFileNames: #don't add them
                #print("Reserved File Name:", currentName)
                continue
            if any(char in currentName for char in reservedCharacters):
                #print("Contains reserved characters:", currentName)
                continue

            if any(char in currentName for char in subfolderDividers):
                isSublist = True
            
            if isSublist:
                subfolders = re.split("[/\\\\]+", currentName)
                #subfoldersList.append(subfolders)
                currentName = subfolders[0]
                if currentName.lower() not in originalOrderDict:
                    originalOrderDict[currentName.lower()] = []
                if currentName.lower() not in subfoldersDict:
                    subfoldersDict[currentName.lower()] = []
                subfoldersDict[currentName.lower()].append(subfolders)
                originalOrderDict[currentName.lower()].append(subfolders)
            else:
                if currentName.lower() not in originalOrderDict:
                    originalOrderDict[currentName.lower()] = []
                if currentName.lower() not in letterCasesDict:
                    letterCasesDict[currentName.lower()] = []
                letterCasesDict[currentName.lower()].append(currentName)
                originalOrderDict[currentName.lower()].append(currentName)
        
        orderedLetterCasesDict = collections.OrderedDict(sorted(letterCasesDict.items()))
        keyUnionSet = set(orderedLetterCasesDict.keys()).union(set(subfoldersDict.keys()))
        keyUnionDict = collections.OrderedDict.fromkeys(sorted(keyUnionSet), None)

        #print("subfoldersList", subfoldersList)
        #print("orderedLetterCasesDict:", orderedLetterCasesDict)
        #print("subfoldersDict", subfoldersDict)
        print("originalOrderDict", originalOrderDict)

        #print("keyUnionSet:", keyUnionSet)
        #print("keyUnionDict:", keyUnionDict)

        combinedDict = {}
        combinedNameCases = {}
        combinedUniqueNameCases = {}
        chosenNamecasesList = []
        chosenNamecasesDict = {}

        for key in keyUnionDict.keys():
            #print("key:", key)
            combinedDict[key] = []
            combinedNameCases[key] = []
            if key in orderedLetterCasesDict.keys():
                combinedDict[key].extend(orderedLetterCasesDict[key])
                combinedNameCases[key].extend(orderedLetterCasesDict[key])
            if key in subfoldersDict.keys():
                combinedDict[key].extend(subfoldersDict[key])
                combinedNameCases[key].extend([a[0] for a in subfoldersDict[key]])
            combinedUniqueNameCases[key] = set(combinedNameCases[key])
            #print("\tResult combinedDict[key]", combinedDict[key])
            #print("\tResult combinedNameCases[key]", combinedNameCases[key])
            #print("\tResult combinedUniqueNameCases[key]", combinedUniqueNameCases[key])

        #print("combinedDict", combinedDict)
        #print("combinedNameCases", combinedNameCases)
        #print("combinedUniqueNameCases", combinedUniqueNameCases)

        validNamesDict = {}
        for key in originalOrderDict.keys():
            namecaseList = originalOrderDict[key]
            leadingNamecaseList = combinedNameCases[key]
            namecaseSet = set(leadingNamecaseList)

            validNamesDict[key] = []
            
            print(namecaseSet)
            if len(namecaseSet) > 1:
                chosenNamecase = self.openWindow(namecaseSet)
                #print("chosenNamecase", chosenNamecase)
                if chosenNamecase != "":
                    #print("case set:", combinedDict[key])
                    for case in originalOrderDict[key]:
                        print("case:", case)
                        if type(case) == list:
                            case[0] = chosenNamecase
                            #print("updatedCase:", case)
                            validNamesList.append(case)
                            print("A1", case)
                            validNamesDict[key].append(case)
                            validLeadingNamesList.append(case[0])
                        else:
                            validNamesList.append(chosenNamecase)
                            print("A2", chosenNamecase)
                            validNamesDict[key].append(chosenNamecase)
                            validLeadingNamesList.append(chosenNamecase)
                    chosenNamecasesList.append(chosenNamecase)
            else:
                #print("originalOrderDict", originalOrderDict[key])
                chosenNamecase = originalOrderDict[key][0]
                #print("chosenNamecase", chosenNamecase)
                #print(namecaseList, len(namecaseList))
                #for i in range(len(namecaseList)):
                for case in originalOrderDict[key]:
                    if type(chosenNamecase) == list:
                        #print("updatedCase:", case)
                        validNamesList.append(chosenNamecase)
                        print("A3", chosenNamecase)
                        validNamesDict[key].append(chosenNamecase)
                        validLeadingNamesList.append(chosenNamecase[0])
                        chosenNamecase = chosenNamecase[0]
                    else:
                        validNamesList.append(chosenNamecase)
                        print("A4", chosenNamecase)
                        validNamesDict[key].append(chosenNamecase)
                        validLeadingNamesList.append(chosenNamecase)
                    chosenNamecasesList.append(chosenNamecase)
            #print("chosenNamecasesList", chosenNamecasesList)
            if chosenNamecase != "":
                chosenNamecasesDict[chosenNamecase.lower()] = chosenNamecase

        #for key in subfoldersDict.keys():
        print("validNamesList:", validNamesList)
        print("validNamesDict:", validNamesDict)
        print("validLeadingNamesList:", validLeadingNamesList)
        print("chosenNamecasesList:", chosenNamecasesList)
        #print("chosenNamecasesDict:", chosenNamecasesDict)

        #print("faultyNamesList:", faultyNamesList)
       
        #print("subfoldersList:", subfoldersList)
        #validNamesSet = set(validNamesList)
        counterList = collections.Counter(validLeadingNamesList)
        #print("validNamesSet:", validNamesSet)
        print("counterList:", counterList)
    
        """
        for item in os.listdir(self.directory):
            if (
                item in validNamesSet 
                and not self.duplicateFoldersCheckbox.isChecked()
            ):
                validNamesSet.remove(item)
        """
        cumulativeList = []
        for item in os.listdir(self.directory):
            if item.lower() in chosenNamecasesDict.keys():
                #print(chosenNamecasesDict[item.lower()])
                os.rename(item, chosenNamecasesDict[item.lower()])
                continue
            parser = re.findall('[(]Copy [0-9]+[)]', item)
            if (parser != []):
                strippedItem = item.replace(parser[-1], "").strip()
                if strippedItem.lower() in chosenNamecasesDict.keys():
                    #print(parser)
                    #print("strippedItem:", strippedItem)
                    cumulativeList.append(chosenNamecasesDict[strippedItem.lower()])
                    #print("chosenNamecasesDict item:", chosenNamecasesDict[strippedItem.lower()].split())
                    os.rename(item, chosenNamecasesDict[strippedItem.lower()] + " " + parser[-1])
        cumulativeCounterList = collections.Counter(cumulativeList)
        print("cumulativeList:", cumulativeList)
        print("cumulativeCounterList:", cumulativeCounterList)

        finalNamesList = []
        for item in validNamesDict.keys(): #chosenNamecasesList:
            if(
                self.ui.duplicateFoldersCheckbox.isChecked() 
                and counterList[item] > 0
            ):
                print("item:", item)
                if(item not in os.listdir(self.directory)):
                    currentValidName = validNamesList[len(finalNamesList)]
                    if type(currentValidName) == list:
                        currentValidName[0] = item
                        print("B1", currentValidName)
                        finalNamesList.append(currentValidName)
                    else:
                        print("B2", currentValidName)
                        finalNamesList.append(item)
                    for i in range(2, counterList[item] + 1): 
                        newItem = item + " " + "(Copy " + str(i + cumulativeCounterList[item] - 1) + ")"
                        currentValidName = validNamesList[len(finalNamesList)]
                        if type(currentValidName) == list:
                            currentValidName[0] = newItem
                            print("B3", currentValidName)
                            finalNamesList.append(currentValidName)
                        else:
                            currentValidName = validNamesList[len(finalNamesList)] = newItem
                            print("B4", currentValidName)
                            finalNamesList.append(currentValidName)
                else:
                    for i in range(1, counterList[item] + 1):
                        newItem = item + " " + "(Copy " + str(i + cumulativeCounterList[item]) + ")"
                        print(newItem)
                        print(validNamesList, finalNamesList)
                        currentValidName = validNamesList[len(finalNamesList)]
                        if type(currentValidName) == list:
                            currentValidName[0] = newItem
                            print("B5", currentValidName)
                            finalNamesList.append(currentValidName)
                        else:
                            currentValidName = validNamesList[len(finalNamesList)] = newItem
                            print("B6", currentValidName)
                            finalNamesList.append(currentValidName)
            else:
                finalNamesList.append(item)
                #print(len(finalNamesList))

        """
        finalNamesList = []
        for item in chosenNamecasesList: #validNamesSet:
            if((
                self.duplicateFoldersCheckbox.isChecked() 
                and counterList[item] > 0
            )):
                print("item:", item)
                if(item not in os.listdir(self.directory)):
                    finalNamesList.append(item)
                    for i in range(2, counterList[item] + 1):
                        finalNamesList.append(item + " " + "(Copy " + str(i + cumulativeCounterList[item] - 1) + ")")
                else:
                    for i in range(1, counterList[item] + 1):
                        finalNamesList.append(item + " " + "(Copy " + str(i + cumulativeCounterList[item]) + ")")
            else:
                finalNamesList.append(item)
        """

        """
        for i in range(len(validNamesList)):
            if validNamesList[i] == finalNamesList[i]:
                continue
            else:
                if type(validNamesList[i]) == list:
                    validNamesList[i][0].replace(validNamesList[i][0], finalNamesList[i], 1)
                else:
                    validNamesList[i].replace(validNamesList[i], finalNamesList[i], 1)
        """

        """
        if self.duplicateFoldersCheckbox.isChecked():
            for i in range(len(subfoldersList)):
                subfoldersList[i][0] = finalNamesList[i]
        """
        print("finalNamesList", finalNamesList)
        print("validNamesList", validNamesList)

        #if not self.duplicateFoldersCheckbox.isChecked():
        #    firstInstancesDict = {}    

        namesList = finalNamesList if not self.ui.duplicateFoldersCheckbox.isChecked() else validNamesList
        
        if not self.ui.duplicateFoldersCheckbox.isChecked(): 
            for name in namesList:
                nameFromDict = validNamesDict[name.lower()][0]
                if type(nameFromDict) == list:
                    if name in os.listdir(self.directory):
                        folderDirectory = os.path.join(self.directory, nameFromDict[0])
                        shutil.rmtree(folderDirectory)
                    os.makedirs(self.directory + "\\" + "\\".join(nameFromDict))
                else:
                    if name in os.listdir(self.directory):
                        folderDirectory = os.path.join(self.directory, name)
                        if len(os.listdir(folderDirectory)) > 0:
                            shutil.rmtree(folderDirectory)
                        else:
                            continue
                    os.mkdir(self.directory + "\\" + validNamesDict[name.lower()][0])
        else:
            for name in namesList:
                if type(name) == list:
                    #print("Before:", finalNamesList[i], "|", validNamesList[i])
                    #validNamesList[i][0] = finalNamesList[i]
                    #finalNamesList[i] = validNamesList[i]
                    #print("After:", finalNamesList[i], "|", validNamesList[i])
                    print("name", name)
                    os.makedirs(self.directory + "\\" + "\\".join(name))
                else: 
                    os.mkdir(self.directory + "\\" + name)

        print("finalNamesList", finalNamesList)
        print("~~~Complete!")

    def openNameListFile(self):
        #print("open")
        """ To provide an option for """ #self.ui.folderNames.clear()
        fileToOpen = QtWidgets.QFileDialog.getOpenFileName(
            self, 
            "Open Name List Text File",
            self.ui.directoryTextbox.text(),
            "Text Files (*.txt)"
        )
        if (fileToOpen[0] != ""):
            with open(fileToOpen[0], "r") as fileContents:
                for name in fileContents:
                    #print(name.strip("\n"))
                    self.ui.folderNames.appendPlainText(name.strip("\n"))
            fileContents.close()

    def saveNameListFile(self):
        #print("save")
        fileToSave = QtWidgets.QFileDialog.getSaveFileName(
            self, 
            "Save Name List Text File",
            self.ui.directoryTextbox.text(),
            "Text Files (*.txt)"
        )
        if (fileToSave[0] != ""):
            with open(fileToSave[0], "w") as fileContents:
                folderNames = self.ui.folderNames.toPlainText()
                #print(folderNames)
                fileContents.write(folderNames)
            fileContents.close()

class Ui_CaseStyleWindow(object):
    def setupUi(self, CaseStyleWindow):
        CaseStyleWindow.setObjectName("CaseStyleWindow")
        CaseStyleWindow.resize(300, 420)
        self.centralwidget = QtWidgets.QWidget(CaseStyleWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 300, 418))
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 40, 260, 300))
        self.listWidget.setObjectName("listWidget")
        self.chooseCasesLabel = QtWidgets.QLabel(self.centralwidget)
        self.chooseCasesLabel.setGeometry(QtCore.QRect(20, 15, 241, 16))
        self.chooseCasesLabel.setObjectName("chooseCasesLabel")
        self.cancelLabel = QtWidgets.QLabel(self.centralwidget)
        self.cancelLabel.setGeometry(QtCore.QRect(20, 350, 241, 21))
        self.cancelLabel.setObjectName("cancelLabel")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(130, 380, 150, 25))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.retranslateUi(CaseStyleWindow)
        QtCore.QMetaObject.connectSlotsByName(CaseStyleWindow)

    def retranslateUi(self, CaseStyleWindow):
        _translate = QtCore.QCoreApplication.translate
        CaseStyleWindow.setWindowTitle(_translate("CaseStyleWindow", "Choose a case style"))
        self.chooseCasesLabel.setText(_translate("CaseStyleWindow", "Choose the case style to use:"))
        self.cancelLabel.setText(_translate("CaseStyleWindow", "Click \'Cancel\' in order to use none of them."))

class CaseStyleWindow(QtWidgets.QDialog):
    def __init__(self, namecases):
        #super(Ui_CaseStyleWindow, self).__init__()
        super(CaseStyleWindow, self).__init__()
        self.ui = Ui_CaseStyleWindow()
        self.ui.setupUi(self)
        self.namecases = namecases
        self.selectedCase = ""
        self.ui.listWidget.addItems(sorted(self.namecases, key=str.swapcase))
        self.ui.listWidget.itemSelectionChanged.connect(self.selectionChanged)
        self.ui.buttonBox.accepted.connect(self.closeWithCaseStyle)
        self.ui.buttonBox.rejected.connect(self.closeWithoutCaseStyle)

    def selectionChanged(self):
        self.selectedCase = self.ui.listWidget.currentItem().text()
        #print("Selected item:", self.selectedCase)

    def closeWithCaseStyle(self):
        if self.selectedCase != "":
            self.selectedCase = self.ui.listWidget.currentItem().text()
            #print("Chosen item:", self.selectedCase)
            QtWidgets.QDialog.close(self)
        else:
            QtWidgets.QMessageBox.question(
                self, 
                'No Case Style Selected',
                "Please select a case style. If you don't want any case, click 'Cancel'",
                QtWidgets.QMessageBox.Ok
            )

    def closeWithoutCaseStyle(self):
        self.selectedCase = ""
        #print("No item chosen:")
        QtWidgets.QDialog.close(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'images', 'app_logo.ico')))
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())