import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts


Item {
    id: screenSelectSupervisor

    Component.onCompleted: {
        console.log("Screen_SelectScenario loaded")
    }
     ScreenTitle {
        id: supervisorTitle
        prevTitle: "Supervisor selection"
        mainTitle: "Scenario selection"
        nextTitle: "Boarding"
    }
    ColumnLayout {
        anchors.top: supervisorTitle.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.topMargin: 8
        width: parent.width - 30
        spacing: 20

        RowLayout {
            Layout.fillWidth: true
            Layout.topMargin: 20
            Button {
                text: "Back"
                onClicked: {
                    console.log("Step back clicked")
                    mainStack.pop()
                }
            }
            Item { Layout.fillWidth: true }
            Button {
                text: "Next"
                onClicked: {
                    console.log("Scenario Next clicked")
                    //mainStack.push("Screen_SelectScenario.qml")
                }
            }
        }
    }
}