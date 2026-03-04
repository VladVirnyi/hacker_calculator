import QtQuick
import QtQuick.Controls

Window {
    visible: true
    width: 600
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
                id: resultLabel
                property string finalResult: calculator.result
                property string charSet: "01ABCDEFGH#!?@$%" // characters for "glitch" effect
                
                anchors.horizontalCenter: parent.horizontalCenter
                color: "#2bff00"
                font.family: "Hack"
                font.pixelSize: 22
                
                text: "READY TO EXPLOIT..."

                onFinalResultChanged: {
                    decryptTimer.count = 0
                    decryptTimer.start()
                }

                Timer {
                    id: decryptTimer
                    interval: 50
                    repeat: true
                    property int count: 0
                    property int maxTicks: 10

                    onTriggered: {
                        if (count < maxTicks) {
                            // generate random "glitch" string
                            let randomStr = ""
                            for (let i = 0; i < resultLabel.finalResult.length; i++) {
                                randomStr += resultLabel.charSet.charAt(Math.floor(Math.random() * resultLabel.charSet.length))
                            }
                            resultLabel.text = randomStr
                            count++
                        } else {
                            resultLabel.text = resultLabel.finalResult
                            stop()
                        }
                    }
                }

                background: Rectangle {
                    color: "transparent"
                    border.color: "#2bff00"
                    border.width: 1
                    opacity: 0.3
                    
                    SequentialAnimation on opacity {
                        loops: Animation.Infinite
                        NumberAnimation { from: 0.1; to: 0.5; duration: 1000 }
                        NumberAnimation { from: 0.5; to: 0.1; duration: 1000 }
                    }
                }
            }
        }
    }