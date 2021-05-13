/****************************************************************************
**
** Copyright (C) 2020 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the Qt Quick Controls 2 module of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL3$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see http://www.qt.io/terms-conditions. For further
** information use the contact form at http://www.qt.io/contact-us.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 3 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPLv3 included in the
** packaging of this file. Please review the following information to
** ensure the GNU Lesser General Public License version 3 requirements
** will be met: https://www.gnu.org/licenses/lgpl.html.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 2.0 or later as published by the Free
** Software Foundation and appearing in the file LICENSE.GPL included in
** the packaging of this file. Please review the following information to
** ensure the GNU General Public License version 2.0 requirements will be
** met: http://www.gnu.org/licenses/gpl-2.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/

import QtQuick
import QtQuick.Controls.impl
import QtQuick.Templates as T
import QtQuick.NativeStyle as NativeStyle

T.Button {
    id: control

    readonly property bool __nativeBackground: background instanceof NativeStyle.StyleItem

    // Since QQuickControl will subtract the insets from the control size to
    // figure out the background size, we need to reverse that here, otherwise
    // the control ends up too big.
    implicitWidth: implicitBackgroundWidth + leftInset + rightInset
    implicitHeight: implicitBackgroundHeight + topInset + bottomInset

    font.pixelSize: __nativeBackground ? background.styleFont(control).pixelSize : undefined

    leftPadding: __nativeBackground ? background.contentPadding.left : 5
    rightPadding: __nativeBackground ? background.contentPadding.right : 5
    topPadding: __nativeBackground ? background.contentPadding.top : 5
    bottomPadding: __nativeBackground ? background.contentPadding.bottom : 5

    background: NativeStyle.Button {
        control: control
        contentWidth: contentItem.implicitWidth
        contentHeight: contentItem.implicitHeight
        useNinePatchImage: false
        overrideState: NativeStyle.StyleItem.NeverHovered
    }

    NativeStyle.Button {
        control: control
        x: background.x
        y: background.y
        width: background.width
        height: background.height
        useNinePatchImage: false
        overrideState: NativeStyle.StyleItem.AlwaysHovered
        opacity: control.hovered ? 1 : 0
        Behavior on opacity { NumberAnimation { duration: parent.transitionDuration } }
    }

    icon.width: 24
    icon.height: 24
    icon.color: control.checked || control.highlighted ? control.palette.brightText :
                control.flat && !control.down ? (control.visualFocus ? control.palette.highlight : control.palette.windowText) : control.palette.buttonText

    contentItem: IconLabel {
        spacing: control.spacing
        mirrored: control.mirrored
        display: control.display

        icon: control.icon
        text: control.text
        font: control.font
        color: control.flat && !control.down ? (control.visualFocus ? control.palette.highlight : control.palette.windowText) : control.palette.buttonText
    }
}
