#ifndef MYHELPER_H
#define MYHELPER_H

#include <QtCore>
#include <QtGui>
#include <QtNetwork>
#if (QT_VERSION > QT_VERSION_CHECK(5,0,0))
#include <QtWidgets>
#endif

class myHelper: public QObject
{

public:

    //获取选择的文件
    static QString GetFileName(QString filter) {
        return QFileDialog::getOpenFileName(0, "选择文件", QCoreApplication::applicationDirPath(), filter);
    }

    //获取选择的文件集合 - 用于打开多个文件
    static QStringList GetFileNames(QString filter) {
        return QFileDialog::getOpenFileNames(0, "选择文件", QCoreApplication::applicationDirPath(), filter);
    }

//    //获取选择的目录
//    static QString GetFolderName() {
//        return QFileDialog::getExistingDirectory();;
//    }

//    //获取文件名,含拓展名
//    static QString GetFileNameWithExtension(QString strFilePath) {
//        QFileInfo fileInfo(strFilePath);
//        return fileInfo.fileName();
//    }

//    //获取选择文件夹中的文件
//    static QStringList GetFolderFileNames(QStringList filter) {
//        QStringList fileList;
//        QString strFolder = QFileDialog::getExistingDirectory();
//        if (!strFolder.length() == 0) {
//            QDir myFolder(strFolder);
//            if (myFolder.exists()) {
//                fileList = myFolder.entryList(filter);
//            }
//        }
//        return fileList;
//    }

//    //文件夹是否存在
//    static bool FolderIsExist(QString strFolder) {
//        QDir tempFolder(strFolder);
//        return tempFolder.exists();
//    }

//    //文件是否存在
//    static bool FileIsExist(QString strFile) {
//        QFile tempFile(strFile);
//        return tempFile.exists();
//    }

//    //复制文件
//    static bool CopyFile(QString sourceFile, QString targetFile) {
//        bool ok;
//        ok = QFile::copy(sourceFile, targetFile);
//        //将复制过去的文件只读属性取消
//        ok = QFile::setPermissions(targetFile, QFile::WriteOwner);
//        return ok;
//    }
};

#endif // MYHELPER_H
