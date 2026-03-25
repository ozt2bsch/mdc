import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


Item {
    id: screenTitle
    property string prevTitle: "prevTitle"
    property string mainTitle: "MainTitle"
    property string nextTitle: "nextTitle"

    implicitWidth: parent.width
    implicitHeight: childrenRect.height

    Text {
        id: mainTitleText
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top
        anchors.topMargin: 10
        text: screenTitle.mainTitle
        font.pixelSize: 24
        font.bold: true
        color: BoschColors.gray00
    }
    RowLayout {
        id: rlNavigationTitle
        width: parent.width
        //height: mainTitleText.height
        anchors.top: mainTitleText.bottom
        anchors.topMargin: - 8
        Text {
            text: prevTitle
            color: BoschColors.gray20
            Layout.leftMargin: 20
            Layout.alignment: Qt.AlignLeft | Qt.AlignBottom
            font.pointSize: 10
        }
        Text {
            text: nextTitle
            color: BoschColors.gray20
            Layout.rightMargin: 20
            Layout.alignment: Qt.AlignRight | Qt.AlignBottom
            font.pointSize: 10
        }
    }
    Rectangle {
        width: parent.width - 30
        height: 1
        anchors.top: rlNavigationTitle.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        border.width: 1
        border.color: BoschColors.gray30
    }
}