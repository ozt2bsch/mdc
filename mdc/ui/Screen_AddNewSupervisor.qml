import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts

Item {
    id: screenAddNewSupervisor

    Component.onCompleted: {
        console.log("Screen_AddNewSupervisor loaded")
        svCtrl.initialize("addNewSupervisor")
    }
     ScreenTitle {
        id: supervisorTitle
        prevTitle: "Select Supervisor"
        mainTitle: "Add New Supervisor"
        nextTitle: ""
    }
    ColumnLayout {
        anchors.top: supervisorTitle.bottom
        anchors.topMargin: 50
        anchors.horizontalCenter: parent.horizontalCenter
        width: parent.width - 400
        spacing: 20
        RowLayout {
            anchors.topMargin: 20
            Layout.fillWidth: true
            Label {
                text: "Supervisor:"
            }
            TextField {
                id: tfSupervisor
                Layout.fillWidth: true
                placeholderText: "Enter supervisor name"
                onTextChanged: {
                    svCtrl.sv_name = text
                }
            }
        }
        RowLayout {
            Layout.fillWidth: true
            Label {
                text: "Company:"
            }
            ComboBox {
                id: cbCompany
                property string placeholderText: "Select a company"
                Layout.leftMargin: 5
                Layout.fillWidth: true
                model: svCtrl.lstCampaignSuppliers
                currentIndex: svCtrl.lstCampaignSuppliers.indexOf(svCtrl.sv_company)
                displayText: currentIndex === -1 ? placeholderText : currentText
                onActivated: {
                    svCtrl.sv_company = currentText
                }
            }
        }
        RowLayout {
            Layout.fillWidth: true
            Layout.topMargin: 30
            Button {
                text: "Back"
                onClicked: {
                    mainStack.pop()
                    console.log("Back clicked")
                }
            }
            Item {Layout.fillWidth: true}
            Button {
                text: "Add"
                onClicked: {
                    svCtrl.add_new_supervisor()
                    console.log("Add new supervisor clicked")
                }
            }
        }
    }
    Connections {
        target: svCtrl
        function onPop_screen() {
            mainStack.pop()
        }
    }
}