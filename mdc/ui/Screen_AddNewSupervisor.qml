import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts

Item {
    id: screenAddNewSupervisor

    Component.onCompleted: {
        console.log("Screen_AddNewSupervisor loaded")
    }
     ScreenTitle {
        id: supervisorTitle
        prevTitle: "Select Supervisor"
        mainTitle: "Add New Supervisor"
        nextTitle: ""
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
            }
            TextField {
                id: tfSupervisor
                Layout.fillWidth: true
                width: 400
                placeholderText: "Enter supervisor name"
            }
        }
        RowLayout {
            Layout.fillWidth: true
            Label {
                text: "Company:"
            }
            ComboBox {
                id: cbCompany
                Layout.leftMargin: 5
                Layout.fillWidth: true
                model: ["Bosch", "Company A", "Company B"]
            }
        }
        RowLayout {
            Layout.fillWidth: true
            Layout.topMargin: 20
            Button {
                text: "Back"
                Layout.leftMargin: 20
                Layout.rightMargin: 20
                //Layout.fillWidth: true
                onClicked: {
                    mainStack.pop()
                    console.log("Back clicked")
                }
            }
            Item {Layout.fillWidth: true}
            Button {
                text: "Add"
                Layout.leftMargin: 20
                Layout.rightMargin: 20
                //Layout.fillWidth: true
                onClicked: {
                    console.log("Add clicked")
                }
            }
        }
    }
}