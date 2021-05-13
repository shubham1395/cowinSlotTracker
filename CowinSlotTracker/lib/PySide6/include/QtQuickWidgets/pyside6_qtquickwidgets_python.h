/****************************************************************************
**
** Copyright (C) 2016 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of Qt for Python.
**
** $QT_BEGIN_LICENSE:LGPL$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 3 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPL3 included in the
** packaging of this file. Please review the following information to
** ensure the GNU Lesser General Public License version 3 requirements
** will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 2.0 or (at your option) the GNU General
** Public license version 3 or any later version approved by the KDE Free
** Qt Foundation. The licenses are as published by the Free Software
** Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
** included in the packaging of this file. Please review the following
** information to ensure the GNU General Public License requirements will
** be met: https://www.gnu.org/licenses/gpl-2.0.html and
** https://www.gnu.org/licenses/gpl-3.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/


#ifndef SBK_QTQUICKWIDGETS_PYTHON_H
#define SBK_QTQUICKWIDGETS_PYTHON_H

#include <sbkpython.h>
#include <sbkconverter.h>
// Module Includes
#include <pyside6_qtcore_python.h>
#include <pyside6_qtgui_python.h>
#include <pyside6_qtquick_python.h>
#include <pyside6_qtnetwork_python.h>
#include <pyside6_qtqml_python.h>
#include <pyside6_qtwidgets_python.h>

// Bound library includes
#include <QtQuickWidgets/qquickwidget.h>
// Conversion Includes - Primitive Types
#include <wtypes.h>
#include <qabstractitemmodel.h>
#include <QString>
#include <QStringList>
#include <QStringView>
#include <signalmanager.h>

// Conversion Includes - Container Types
#include <pysideqflags.h>
#include <QList>
#include <QMap>
#include <QMultiMap>
#include <QPair>
#include <QQueue>
#include <QSet>
#include <QStack>

// Type indices
enum : int {
    SBK_QQUICKWIDGET_RESIZEMODE_IDX                          = 1,
    SBK_QQUICKWIDGET_STATUS_IDX                              = 2,
    SBK_QQUICKWIDGET_IDX                                     = 0,
    SBK_QtQuickWidgets_IDX_COUNT                             = 3
};
// This variable stores all Python types exported by this module.
extern PyTypeObject **SbkPySide6_QtQuickWidgetsTypes;

// This variable stores the Python module object exported by this module.
extern PyObject *SbkPySide6_QtQuickWidgetsModuleObject;

// This variable stores all type converters exported by this module.
extern SbkConverter **SbkPySide6_QtQuickWidgetsTypeConverters;

// Converter indices
enum : int {
    SBK_QTQUICKWIDGETS_QLIST_QACTIONPTR_IDX                  = 0, // QList<QAction* >
    SBK_QTQUICKWIDGETS_QLIST_QQMLERROR_IDX                   = 1, // QList<QQmlError >
    SBK_QTQUICKWIDGETS_QLIST_QVARIANT_IDX                    = 2, // QList<QVariant >
    SBK_QTQUICKWIDGETS_QLIST_QSTRING_IDX                     = 3, // QList<QString >
    SBK_QTQUICKWIDGETS_QMAP_QSTRING_QVARIANT_IDX             = 4, // QMap<QString,QVariant >
    SBK_QtQuickWidgets_CONVERTERS_IDX_COUNT                  = 5
};
// Macros for type check

namespace Shiboken
{

// PyType functions, to get the PyObjectType for a type T
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
template<> inline PyTypeObject *SbkType< ::QQuickWidget::ResizeMode >() { return SbkPySide6_QtQuickWidgetsTypes[SBK_QQUICKWIDGET_RESIZEMODE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QQuickWidget::Status >() { return SbkPySide6_QtQuickWidgetsTypes[SBK_QQUICKWIDGET_STATUS_IDX]; }
template<> inline PyTypeObject *SbkType< ::QQuickWidget >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtQuickWidgetsTypes[SBK_QQUICKWIDGET_IDX]); }
QT_WARNING_POP

} // namespace Shiboken

#endif // SBK_QTQUICKWIDGETS_PYTHON_H

