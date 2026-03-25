import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts

Item {
    id: screenSelectSupervisor

    Component.onCompleted: {
        console.log("Screen_SelectSupervisor loaded")
    }
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
        width: 400
        spacing: 20
        RowLayout {
            anchors.topMargin: 20
            Layout.fillWidth: true
            Label {
                text: "Supervisor:"
                Layout.topMargin: 20
            }
            ComboBox {
                id: cbSupervisor
                Layout.topMargin: 20
                Layout.leftMargin: 20
                Layout.rightMargin: 20
                Layout.fillWidth: true
                model: ["Supervisor 1", "Supervisor 2", "Supervisor 3"]
            }
        }
        RowLayout {
            Layout.fillWidth: true
            Label {
                text: "Company:"
                Layout.topMargin: 20
            }
            Label {
                text: "Bosch"
                Layout.topMargin: 20
                Layout.leftMargin: 20
                Layout.rightMargin: 20
                Layout.fillWidth: true
                horizontalAlignment: Text.AlignRight
                font.bold: true
                font.pointSize: 14
                color: BoschColors.magenta50
            }
        }
        RowLayout {
            Layout.fillWidth: true
            Layout.topMargin: 20
            Button {
                text: "Back"
                Layout.leftMargin: 20
                Layout.rightMargin: 20
                Layout.fillWidth: true
                onClicked: {
                    console.log("Back clicked")
                    mainStack.pop()
                }
            }
            Button {
                text: "Add new"
                Layout.leftMargin: 20
                Layout.rightMargin: 20
                Layout.fillWidth: true
                onClicked: {
                    console.log("Add new supervisor clicked")
                    mainStack.push("Screen_AddNewSupervisor.qml")
                }
            }
            Button {
                text: "Select"
                Layout.leftMargin: 20
                Layout.rightMargin: 20
                Layout.fillWidth: true
                onClicked: {
                    console.log("Select clicked")
                }
            }
        }
    }
}