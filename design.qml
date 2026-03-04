import QtQuick
import QtQuick.Controls

Window {
    visible: true
    width: 400
    height: 500
    title: "Hacker Calculator"
    color: "#0d0d0d"

    Column {
        anchors.centerIn: parent
        spacing: 15
        width: parent.width * 0.8

        TextField {
            id: num1
            placeholderText: "ENTER Y0UR F1RST NUMB3R"
            width: parent.width
            color: "#2bff00"
            background: Rectangle { color: "#1a1a1a"; border.color: "#2bff00" }
        }

        TextField {
            id: num2
            placeholderText: "ENTER SECOND NUMB3R"
            width: parent.width
            color: "#2bff00"
            background: Rectangle { color: "#1a1a1a"; border.color: "#2bff00" }
        }

        TextField {
            id: op
            placeholderText: "OP (+, -, *, /)"
            width: parent.width
            color: "#2bff00"
            background: Rectangle { color: "#1a1a1a"; border.color: "#2bff00" }
        }

        Button {
            text: "RUN EXPLOIT"
            background:
                Rectangle {
                    color: "#1a1a1a"
                    border.color: '#ffffff'
                }
            contentItem: Text {
                text: parent.text
                color: "#2bff00"
                font.family: "Hack"
                font.pixelSize: 16
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }
            width: parent.width
            onClicked: calculator.calculate(num1.text, num2.text, op.text)
        }

        Label {
            text: calculator.result
            color: "#2bff00"
            font.family: "Hack"
            font.pixelSize: 18
            anchors.horizontalCenter: parent.horizontalCenter
            onTextChanged: resultFade.restart()

            SequentialAnimation on opacity {
                id: resultFade
                running: false
                NumberAnimation { from: 0; to: 1; duration: 600; easing.type: Easing.OutCubic }
                }
            }
        }
    }