import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts

Window {
    id: main
    title: "Error"
    flags: Qt.Dialog
    maximumWidth: 450
    minimumWidth: maximumWidth
    minimumHeight: column.implicitHeight
    maximumHeight: minimumHeight
    color: "#4b4b4b"
    visible: true
    Component.onCompleted: {
        eCtrl.init_screen()
    }

    Material.theme: Material.Dark
    Material.accent: Material.Purple
    Column {
        id: column
        Rectangle {
            id: title
            width: main.width
            height: 50
            color: "#2c2c2c"
            Text {
                id: titleText
                color: "#dedede"
                anchors.left: parent.left
                anchors.leftMargin: 11
                font.pointSize: 15
                text: eCtrl.titleText
                anchors.verticalCenter: parent.verticalCenter
            }
        }
        Rectangle {
            id: content
            height: errorText.implicitHeight>500 ? 500 : errorText.implicitHeight
            width: main.width
            color: "transparent"
            ScrollView {
                id: sView
                anchors.fill: parent
                clip: true
                TextArea {
                    id: errorText
                    color: "#bcbaba"
                    text: eCtrl.errorText
                    selectByMouse: true
                    wrapMode: Text.WordWrap
                    topPadding: 16
                    clip: true
                    readOnly: true
                    font.pointSize: 12
                }
            }
        }
        Button {
            id: btnOK
            text: "OK"
            anchors.right: parent.right
            anchors.rightMargin: 20
            onClicked: Qt.quit()
        }
    }
}
