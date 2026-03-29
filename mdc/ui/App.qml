import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts
import QtQuick.Dialogs
import QtQuick.Window

ApplicationWindow {
    id: mainwindow
    property alias mainStack: stackView

    // High DPI scaling properties for 4K monitor support
    readonly property real dpiFactor: Screen.logicalPixelDensity / 96
    readonly property real scaleFactor: Math.max(1.0, dpiFactor)

    Material.theme: Material.Dark
    Material.accent: Material.Purple

    visible: true
    width: 900 * scaleFactor
    height: 1000 * scaleFactor
    title: "MetaDataCollector"
    color: BoschColors.gray70



    Image {
        id: imgBoschStrip
        height: 8 * mainwindow.scaleFactor
        width: parent.width
        source: "../assets/images/boschDesign.png"
    }
    ButtonGroup {id: sideMenuButtonGroup}
    Rectangle {
        id: sideBar
        anchors.top: imgBoschStrip.bottom
        width: 50 * mainwindow.scaleFactor
        height: parent.height - imgBoschStrip.height
        color: BoschColors.gray80
        ColumnLayout {
            height: parent.height
            spacing: 3 * mainwindow.scaleFactor
            ToolButton {
                Layout.alignment: Qt.AlignHCenter
                ButtonGroup.group: sideMenuButtonGroup
                display: AbstractButton.IconOnly
                icon.source: "../assets/images/supervisor.svg"
                icon.color: BoschColors.gray30
                checkable: true
                ToolTip {
                    id: ttSupervisor
                    visible: false
                    timeout: 300
                    text: "Select Supervisor"
                }
                onHoveredChanged: {
                    hovered ? ttSupervisor.visible = true : ttSupervisor.visible = false
                }
                onCheckedChanged: {
                    checked ? icon.color = BoschColors.gray60 : icon.color = BoschColors.gray30
                }
            }
            ToolButton {
                Layout.alignment: Qt.AlignHCenter
                Layout.topMargin: -10 * mainwindow.scaleFactor
                ButtonGroup.group: sideMenuButtonGroup
                display: AbstractButton.IconOnly
                icon.source: "../assets/images/person.svg"
                icon.color: BoschColors.gray30
                checkable: true
                ToolTip {
                    id: ttNewPerson
                    visible: false
                    timeout: 300
                    text: "Add new person"
                }
                onHoveredChanged: {
                    hovered ? ttNewPerson.visible = true : ttNewPerson.visible = false
                }
                onCheckedChanged: {
                    if (checked) {
                        icon.color = BoschColors.gray60
                        console.log("do action person")
                    } else {
                        icon.color = BoschColors.gray30
                    }
                }
            }
            Rectangle {
                Layout.fillHeight: true
            }

        }

    }
    StackView {
        id: stackView
        x: sideBar.width
        y: imgBoschStrip.height
        width: parent.width - sideBar.width
        height: parent.height - imgBoschStrip.height
        initialItem: ("Screen_SelectSupervisor.qml")
    }


}
