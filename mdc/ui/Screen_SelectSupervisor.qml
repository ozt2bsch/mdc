import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts

Item {
    id: screenSelectSupervisor

    Component.onCompleted: {
        svCtrl.initialize("selectSupervisor")
        console.log("Screen_SelectSupervisor loaded")
    }
    onVisibleChanged: {
        console.log("Screen_SelectSupervisor visibility changed: " + visible)
        visible ? svCtrl.initialize('selectSupervisor') : null }

     ScreenTitle {
        id: supervisorTitle
        prevTitle: "Home"
        mainTitle: "Select Supervisor"
        nextTitle: "Select Person"
    }
    ColumnLayout {
        anchors.top: supervisorTitle.bottom
        anchors.topMargin: 40
        anchors.horizontalCenter: parent.horizontalCenter
        width: parent.width - 400
        spacing: 20
        RowLayout {
            Layout.fillWidth: true
            Label { text: "Supervisor:" }
            ComboBox {
                id: cmbSupervisor
                Layout.fillWidth: true
                property string placeholderText: "Select a supervisor"
                model: svCtrl.lstSupervisors
                currentIndex: svCtrl.lstSupervisors.findIndex(sv => sv.name === svCtrl.sv_name && sv.company === svCtrl.sv_company)
                displayText: currentIndex === -1 ? placeholderText : svCtrl.lstSupervisors[currentIndex].name
                delegate: ItemDelegate {
                    width: parent.width
                    text: modelData.name + " (" + modelData.company + ")"
                }
                onActivated: {
                    svCtrl.load_supervisor([svCtrl.lstSupervisors[currentIndex].name, svCtrl.lstSupervisors[currentIndex].company])
                }
            }
        }
        RowLayout {
            Layout.fillWidth: true
            Label { text: "Company:" }
            Label {
                text: svCtrl.sv_company
                Layout.fillWidth: true
                horizontalAlignment: Text.AlignRight
                font.bold: true
                font.pointSize: 14
                color: BoschColors.magenta50
            }
        }
        RowLayout {
            Layout.fillWidth: true
            Button {
                text: "Back"
                onClicked: {
                    console.log("Back clicked")
                    mainStack.pop()
                }
            }
            Item { Layout.fillWidth: true }
            Button {
                text: "Add new"
                onClicked: {
                    console.log("Add new supervisor clicked")
                    mainStack.push("Screen_AddNewSupervisor.qml")
                }
            }
            Item { Layout.fillWidth: true }
            Button {
                text: "Select"
                onClicked: {
                    console.log("Select clicked")
                    svCtrl.select_supervisor()
                    //mainStack.push("Screen_SelectScenario.qml")
                }
            }
        }
    }
    Connections {
        target: svCtrl
        function onLoad_addNew_supervisor_screen() {
            mainStack.push("Screen_AddNewSupervisor.qml")
        }
    }
}