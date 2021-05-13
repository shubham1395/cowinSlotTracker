/****************************************************************************
**
** Copyright (C) 2020 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of Qt Quick 3D.
**
** $QT_BEGIN_LICENSE:GPL$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 3 or (at your option) any later version
** approved by the KDE Free Qt Foundation. The licenses are as published by
** the Free Software Foundation and appearing in the file LICENSE.GPL3
** included in the packaging of this file. Please review the following
** information to ensure the GNU General Public License requirements will
** be met: https://www.gnu.org/licenses/gpl-3.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/

import QtQuick
import QtQuick3D
import QtQuick3D.Effects

Effect {
    property real shoulderSlope: 1.0   // 0.0 - 3.0
    property real shoulderEmphasis: 0  // -1.0 - 1.0
    property real toeSlope: 1.0        // 0.0 - 3.0
    property real toeEmphasis: 0       // -1.0 - 1.0
    property real contrastBoost: 0     // -1.0 - 2.0
    property real saturationLevel: 1   // 0.0 - 2.0
    property real gammaValue: 2.2      // 0.1 - 8.0
    property bool useExposure: false
    property real whitePoint: 1.0      // 0.01 - 128.0
    property real exposureValue: 1.0   // 0.01 - 16.0

    Shader {
        id: tonemapShader
        stage: Shader.Fragment
        shader: "qrc:/qtquick3deffects/shaders/scurvetonemap.frag"
    }

    Buffer {
        // LDR output
        id: defaultOutput
        format: Buffer.RGBA8
    }

    passes: [
        Pass {
            shaders: tonemapShader
            output: defaultOutput
        }
    ]
}
